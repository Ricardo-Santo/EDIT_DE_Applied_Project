# Transformation with DBT

## Staging Tables

For the staging tables we started with removing null rows, and to change data types into matching formats, because of the existing relationships between tables.

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
