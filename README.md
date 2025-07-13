# RegTech ETL Pipeline

A complete data engineering project that extracts, transforms, and loads data from a SaaS solution of a Regulatory Technologic solution using Python and other open source software. It integrates with a PostgreSQL database and supports dbt for transformation and Streamlit for visualization.

**Developed by:**

Ricardo Espírito Santo

Rodolfo Fernandes

# ANALYTICS ENGINEERING PROJECT

This project demonstrates the Data Engineering workflow using dbt (data build tool) for data transformation within an ELT pipeline. The data is extracted from a cloud using an API and then loaded into a PostgreSQL database with storage in the render.com cloud and modeled to support stakeholder-driven decision-making — specifically tailored to answer key business questions from the CEO of the RegTech company.

---

## Project Overview

The goal of this project is to simulate a real-world approach: delivering clean, modeled data to support business KPIs. Using dbt, we transform client data into actionable insights, helping stakeholders understand performance trends and operational metrics.

---

## Project Structure

```text
RegTech/
├── data/
|   ├── dim_cliente.csv
|   ├── dim_empresa.csv
|   ├── dim_pix.csv
|   └── fato_contato.csv        
|
├── src/
|   ├── app.py
|   ├── Extract.py
|   ├── Load.py
|   └── Transform.py
|
└── dbt_transform/
    ├── models/
    │   ├── staging/
    │   │   ├── stg__dim_cliente.sql
    │   │   ├── stg__dim_empresa.sql
    │   │   ├── stg__dim_pix.sql
    │   │   └── stg__fato_contato.sql
    │   ├── intermediate/
    │   │   ├── int__cliente_empresa.sql
    │   │   ├── int__empresa_geolocation.sql
    │   │   ├── int__empresa_pix.sql
    │   │   └── int__fato_contato_enriched.sql
    │   └── marts/
    │       ├── dim_clientes_final.sql
    │       ├── empresa_pix_analysis.sql
    │       └── fato_contato_final.sql
    └── seeds/
```

---
### Technologies Used

- **Python 3.12** to help prepare data for visualization
- **PostgreSQL** hosted locally
- **dbt** for transformations and models
- **Streamlit** for data visualization
---

### ELT Pipeline

1. **Extract**: Data that is...
2. **Load**: ...
3. **Transform**: Using dbt, raw tables are cleaned, standardized, and transformed into analytics-ready models.
These models are organized by layers:
Staging models – Rename, cast, and clean raw source data
Intermediate models – ...
Mart models – Final business-focused tables used to answer stakeholder questions and KPIs ...
4. **Visualize** (optional): Use Streamlit to create an interactive dashboard for exploring key metrics and trends, such as most popular films, top-paying customers, or rental activity over time.
---

### Run the dashboard

```bash
# Run dashboard visualization
streamlit run src/app.py
```
