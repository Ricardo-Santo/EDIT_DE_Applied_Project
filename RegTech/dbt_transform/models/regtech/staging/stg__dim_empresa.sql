{{ config(materialized='view') }}

WITH dim_empresa_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'dim_empresa') }}
)

SELECT
    id_empresa::INTEGER AS id_empresa,
    cnpj,
    nome_empresa,
    estado,
    cidade,
    pais,
    site,
    situacao,
FROM dim_client_source
WHERE nome_empresa IS NOT NULL;