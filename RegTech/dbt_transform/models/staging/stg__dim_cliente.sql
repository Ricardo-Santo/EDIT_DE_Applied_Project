{{ config(materialized = 'view') }} WITH dim_cliente_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'dim_cliente') }}
),
dim_empresa AS (
    SELECT *
    FROM {{ source('dbt_transform', 'dim_empresa') }}
)
SELECT c.id_cliente::INTEGER AS id_cliente,
    c.id_empresa::INTEGER AS id_empresa,
    c.nome,
    c.email,
    c.cargo
FROM dim_cliente c
    LEFT JOIN dim_empresa e ON c.id_empresa = e.id_empresa