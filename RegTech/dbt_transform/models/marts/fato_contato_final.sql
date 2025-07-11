SELECT 
  *,
  COUNT(*) OVER (PARTITION BY id_cliente) AS total_contatos_cliente
FROM {{ ref('int__fato_contato_enriched') }}
