# Transformation with DBT

## Staging Tables

For the staging tables we started with removing null rows, standardizing data types across all models (especially for joins), renamed columns for consistency and prepared the base for relationships in later layers.

### dim_cliente

For this table we changed the data types of ``id_cliente`` and ``id_empresa``, from **bigint** to **integer**, for coherente data types across data tables.

### dim_empresa

For this table we changed the data types of ``id_empresa`` and ``cnpj``, from **bigint** to **integer**, for coherente data types across data tables, and also removed a null row present in the table (one row was removed in this process). During our exploration we also found that this table mostly contains companies designated as *Sociedade de Crédito Direto*, so we had to exclude from table ``dim_pix`` entries that did not exist on ``dim_empresa``.

### dim_pix

For this table we changed the column names, which had spaces between them and had very long names, to columns with shorter names in **snake_case** and put the column names in **lower case**. Also in the ``cnpj`` column we removed all of the numbers to the right of backslash, and removed the dots present, example case: ``33.930.368/0001-08`` changed to ``33930368``, lastly we changed the data type of this columns from **text** to **integer**, to help with the relationship between this table and ``dim_empresa``. With this in mind and to have a relationship between ``cnpj`` from this table and ``cnpj`` from dim_empresa we had to find all the matching ``cnpj`` existing between these two tables, to create meaningfull insights.

### fato_contato

For this table we changed the data types of ``id_contato``, ``id_cliente`` and ``id_empresa``, from **bigint** to **integer**, for coherent data types across data tables. To remove unnecessary entries for this table, we went and applied an **INNER JOIN** by ``id_empresa``, with the table ``stg__dim_empresa`` that was already "curated" with nulls removed.

---

## Intermediate Tables

In the intermediate layer, we focused on enriching and joining the staging models to produce reusable, logic-ready datasets that could be leveraged by multiple marts.

### int__cliente_empresa

Joined ``stg__dim_cliente`` with ``stg__dim_empresa`` to bring company metadata into the client dimension. Allows filtering and segmenting clients by company-level attributes (like location or status). Serves as the base for ``dim_clientes_final``.

### int__empresa_pix

Joined ``stg__dim_empresa`` with ``stg__dim_pix`` using the cleaned cnpj key. Produces a unified view of companies with their PIX participation data. Useful for regulatory insights and PIX adoption analytics.

### int__empresa_geolocation

Enriched ``stg__dim_empresa`` with geolocation data (latitude and longitude) by joining with a seed file based on state(**estado**) geolocation. Enables spatial analysis for mapping and clustering companies. Acts as a bridge for geospatial enrichment in downstream models.

### int__fato_contato_enriched

Combined ``stg__fato_contato`` with client (``stg__dim_cliente``) and company (``stg__dim_empresa``) information. Resulting dataset includes full context on each contact: who was contacted, by whom, for what company, and where. Prepared for conversion analysis and segmentation logic.

---

## Seeds Table

We use seed files to enhance external context that’s not available in source systems.

### geo_location_data (CSV)

Contains geolocation metadata: state acronym (**state**), state name (**name**), state latitude (**lat**), state longitude (**lon**). Loaded into DBT via ``dbt seed`` and used in ``int__empresa_geolocation``. Assists in mapping companies to their geographic locations for regional analysis and visualization.

---

## Marts Tables

The marts layer represents our final, business-ready datasets for analytics, dashboards, and reporting.

### dim_clientes_final

Combines ``int__cliente_empresa`` with ``int__empresa_geolocation``. Adds geographic attributes to the client dimension. Enables segmentation by region and company profile.

### empresa_pix_analysis

Filters ``int__empresa_pix`` to only include companies where **autorizada_bcb = 'Sim'**. Used for reports on regulatory compliance and active participation in the PIX ecosystem.

### fato_contato_final

Based on ``int__fato_contato_enriched``. Adds an aggregated metric **total_contatos_cliente** via a window function, counting all contact events per client. Useful for funnel tracking, sales team performance, and lead prioritization.

---
