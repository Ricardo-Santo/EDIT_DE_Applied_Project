import streamlit as st
import pandas as pd
import plotly.express as px  # Needed for plotting
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Construct the database connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Query the data from your table
query = "SELECT estado as state, cidade as name, lat, lon FROM public_marts.dim_clientes_final;" 
df_raw = pd.read_sql(query, engine)

# Group of data por state
df = (
    df_raw.groupby(["state", "name", "lat", "lon"])
    .size()
    .reset_index(name="count") 
)

queryc = "SELECT etapa_funil, canal, estado as state, cargo FROM public_marts.fato_contato_final;"
df_raw_contact = pd.read_sql(queryc, engine)

# Group by 'cargo' and count occurrences
df_contact = (
    df_raw_contact.groupby("cargo")
    .size()
    .reset_index(name="count")
)

# Create frequency dict: cargo -> count
contact_freq = dict(zip(df_contact["cargo"], df_contact["count"]))


# Streamlit UI
st.title("RegTech main KPIs")



chart_type = st.radio(
    "Select Visualization Type",
    [
        "Geographic Distribution of Clients",
        "Clients per State",
        "Job roles  of Clients contacted",
        "Distribution of Communications"
    ]
)


states_available = sorted(df["state"].unique())
selected_states = st.multiselect("Filter by state(s):", states_available, default=states_available)
filtered_df = df[df["state"].isin(selected_states)]


if chart_type == "Geographic Distribution of Clients":
    
    fig = px.scatter_geo(
        filtered_df,
        lat="lat",
        lon="lon",
        hover_name="name",
        size="count", 
        color="count",
        color_continuous_scale="Turbo",
        scope="south america",
        title="Selected Brazilian States",
        hover_data={"lat": False, "lon": False}
    )

    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="LightGreen"
        ),
        title_x=0.5,
        coloraxis_colorbar=dict(title="Count"),
        width= 800, 
        height= 600  
    )

    st.plotly_chart(fig)

    if not filtered_df.empty:
        st.subheader("Returned Data")
        st.dataframe(filtered_df[["state", "name", "count"]].sort_values(by=["state", "count"], ascending=False))

    else:
        st.info("Select one or more states to see them on the map.")
elif chart_type == "Clients per State":
    bar_df = (
        filtered_df.groupby("state")["count"]
        .sum()
        .reset_index()
        .sort_values(by="count", ascending=False)
    )

    fig = px.bar(
        bar_df,
        x="state",
        y="count",
        color="count",
        title="Total Clients by State",
        labels={"state": "State", "count": "Number of Clients"},
        height=500
    )

    st.plotly_chart(fig)


    if not filtered_df.empty:
        st.subheader("Returned Data")
        st.dataframe(filtered_df[["state", "name", "count"]].sort_values(by=["state", "count"], ascending=False))

    else:
        st.info("Select one or more states to see them on the map.")

elif chart_type == "Job roles  of Clients contacted":
    
    st.subheader("Job roles of contacted Clients")

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="plasma"
    ).generate_from_frequencies(contact_freq)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout()

    st.pyplot(fig)

elif chart_type == "Distribution of Communications":
    st.subheader("Channel of reaching out to clients")

    filter_col = st.radio("Select filter type", ("etapa_funil", "state"))

    filter_values = df_raw_contact[filter_col].dropna().unique()
    selected_value = st.selectbox(f"Select {filter_col}", sorted(filter_values))

    filtered_df = df_raw_contact[df_raw_contact[filter_col] == selected_value]

    canal_counts = filtered_df['canal'].value_counts().reset_index()
    canal_counts.columns = ['canal', 'count']


    fig = px.pie(
        canal_counts,
        values='count',
        names='canal',
        title=f"Distribution Channel for {filter_col} when it is {selected_value}",
        hole=0.3,  
    )

    st.plotly_chart(fig, use_container_width=True)