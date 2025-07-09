{{ config(materialized='view') }}

WITH dim_client_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'dim_client') }}
)

SELECT
    id_cliente::INTEGER AS id_cliente,
    id_empresa::INTEGER AS id_empresa,
    nome,
    email,
    cargo
FROM dim_client_source