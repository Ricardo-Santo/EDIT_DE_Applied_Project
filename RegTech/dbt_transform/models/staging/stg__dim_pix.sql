WITH dim_pix_source AS (
    SELECT *
    FROM {{ source('dbt_transform', 'dim_pix') }}
),

stg__dim_empresa AS (
    SELECT *
    FROM {{ ref('stg__dim_empresa') }}
)

SELECT
    "Nome Reduzido" AS nome_reduzido,
    "ISPB" AS ispb,
    REPLACE(REPLACE(SUBSTRING("CNPJ" FROM 1 FOR POSITION('/' IN "CNPJ") - 1), '.', ''), '-', '') AS cnpj,
    "Tipo de Instituição" AS tipo_de_instituicao,
    "Autorizada pelo BCB" AS autorizada_bcb,
    "Tipo de Participação no SPI" AS tipo_participacao_spi,
    "Tipo de Participação no Pix" AS tipo_participacao_pix,
    "Modalidade de Participação no Pix" AS mod_participacao_pix,
    "Status em produção" AS status_producao,
    "Iniciação de Transação de Pagamento" AS inic_transacao_pagamento,
    "Facilitador de serviço de Saque e Troco (FSS)" AS facilitador_saque_troco
FROM dim_pix_source dp
INNER JOIN stg__dim_empresa de
    ON REPLACE(REPLACE(SUBSTRING("CNPJ" FROM 1 FOR POSITION('/' IN "CNPJ") - 1), '.', ''), '-', '') = de.cnpj
    WHERE "Tipo de Instituição" = 'Sociedade de Crédito Direto'
