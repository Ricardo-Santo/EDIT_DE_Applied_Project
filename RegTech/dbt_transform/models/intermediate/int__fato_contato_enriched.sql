SELECT
  fc.id_contato,
  fc.data_contato,
  fc.etapa_funil,
  fc.canal,
  fc.responsavel,
  cl.id_cliente,
  cl.nome AS nome_cliente,
  cl.email,
  cl.cargo,
  em.nome_empresa,
  em.estado,
  em.cidade
FROM {{ ref('stg__fato_contato') }} fc
LEFT JOIN {{ ref('stg__dim_cliente') }} cl
  ON fc.id_cliente = cl.id_cliente
LEFT JOIN {{ ref('stg__dim_empresa') }} em
  ON fc.id_empresa = em.id_empresa
