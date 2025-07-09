{{ config(materialized='view') }}

WITH fato_contato_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'fato_contato') }}
)

SELECT
    id_contato::INTEGER AS id_contato,
    id_cliente::INTEGER AS id_cliente,
    id_empresa::INTEGER AS id_empresa,
    data_contato,
    etapa_funil,
    canal,
    responsavel
FROM fato_contato_source