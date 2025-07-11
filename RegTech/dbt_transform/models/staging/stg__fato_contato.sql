WITH fato_contato_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'fato_contato') }}
),

dim_empresa AS (
    SELECT id_empresa
    FROM {{ ref('stg__dim_empresa') }}
)

SELECT
    fc.id_contato::INTEGER AS id_contato,
    fc.id_cliente::INTEGER AS id_cliente,
    fc.id_empresa::INTEGER AS id_empresa,
    fc.data_contato,
    fc.etapa_funil,
    fc.canal,
    fc.responsavel
FROM fato_contato_source  fc
INNER JOIN dim_empresa AS de
    ON fc.id_empresa = de.id_empresa