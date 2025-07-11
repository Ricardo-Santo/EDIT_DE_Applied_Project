SELECT 
  c.id_cliente,
  c.nome,
  c.email,
  c.cargo,
  e.id_empresa,
  e.nome_empresa,
  e.estado,
  e.cidade,
  e.pais,
  e.situacao
FROM {{ ref('stg__dim_cliente') }} c
JOIN {{ ref('stg__dim_empresa') }} e
  ON c.id_empresa = e.id_empresa
