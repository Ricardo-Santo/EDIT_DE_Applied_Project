# RegTech ETL Pipeline

A complete data engineering project that extracts, transforms, and loads data from a SaaS solution of a Regulatory Technologic solution using Python and other open source software. It integrates with a PostgreSQL database and supports dbt for transformation and Streamlit for visualization.

**Developed by:**

Ricardo Espírito Santo

Rodolfo Fernandes

## ANALYTICS ENGINEERING PROJECT

This project demonstrates the Data Engineering workflow using dbt (data build tool) for data transformation within an ELT pipeline. The data is extracted from a cloud using an API and then loaded into a PostgreSQL database with storage in the render.com cloud and modeled to support stakeholder-driven decision-making — specifically tailored to answer key business questions from the CEO of the RegTech company.

---

## Project Overview

The goal of this project is to simulate a real-world approach: delivering clean, modeled data to support business KPIs. Using dbt, we transform client data into actionable insights, helping stakeholders understand performance trends and operational metrics.

---

## Project Structure

```text
RegTech/
├── data/
│   ├── dim_cliente.csv <-- generated uppon running the Extract.py script from the source DB
│   ├── dim_empresa.csv <-- generated uppon running the Extract.py script from the source DB
│   ├── dim_pix.csv <-- generated uppon running the Extract.py script from the source DB
│   └── fato_contato.csv <-- generated uppon running the Extract.py script from the source DB
├── src/
│   ├── app.py <-- produce the dashboards by streamlit with relevant KPIs
│   ├── Extract.py <-- access the google cloud DB source files via API that is authenticate by credentials.json
│   ├── Load.py <-- Uploads the csv files on the data folder to the postgresql data base hosted on render cloud
│   └── Transform.py <-- apply transformation by dbt on a layering model to the data warehouse
├── dbt_transform/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg__dim_cliente.sql
│   │   │   ├── stg__dim_empresa.sql
│   │   │   ├── stg__dim_pix.sql
│   │   │   └── stg__fato_contato.sql
│   │   ├── intermediate/
│   │   │   ├── int__cliente_empresa.sql
│   │   │   ├── int__empresa_geolocation.sql
│   │   │   ├── int__empresa_pix.sql
│   │   │   └── int__fato_contato_enriched.sql
│   │   └── marts/
│   │       ├── dim_clientes_final.sql
│   │       ├── empresa_pix_analysis.sql
│   │       └── fato_contato_final.sql
│   ├── seeds/
│   │   └── geo_location_data.csv
│   └── tests/
│       ├── consistency/
│       │   ├── test_client_count_consistency.sql
│       │   ├── test_contact_enrichment_consistency.sql
│       │   ├── test_empresa_count_consistency.sql
│       │   └── test_total_contatos_calculation.sql
│       └── generic/
│           ├── test_total_contatos_calculation.sql
│           ├── test_email_format.sql
│           ├── test_geolocation_bounds.sql
│           └── test_pix_cnpj_consistency.sql
├── .env <-- Variables needed to access postgress DB and google drive sheet ID
├── credentials.json <-- API credentials to access the Google Cloud drive with the source data
├── README.md
└── requirements.txt
```

---

### Technologies Used

- **Python 3.12** to help prepare data for visualization
- **PostgreSQL** hosted locally
- **dbt** for transformations and models
- **Streamlit** for data visualization

---

### ELT Pipeline

1. **Extract**: Data that is in Google Cloud platform accessed via API
2. **Load**: Upload data into postgreSQL DB in Render cloud DataWarehouse
3. **Transform**: Using dbt, raw tables are cleaned, standardized, and transformed into analytics-ready models.
These models are organized by layers:
Staging models – Rename, cast, and clean raw source data
Intermediate models – Builds upon the staging layer by performing more complex transformations and aggregations. 
Mart models – Final business-focused tables used to answer stakeholder questions and KPIs .
4. **Visualize** (optional to the pipeline): Use Streamlit to create an interactive dashboard for exploring key metrics and trends.

---

### Run the dashboard

```bash
# Run dashboard visualization
streamlit run src/app.py
```
### Run the documentation

```bash
# Run dashboard visualization
dbt docs generate
dbt docs serve
```