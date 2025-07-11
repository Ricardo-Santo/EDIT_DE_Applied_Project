SELECT
  c.*,
  eg.lat,
  eg.lon
FROM {{ ref('int__cliente_empresa') }} c
LEFT JOIN {{ ref('int__empresa_geolocation') }} eg
  ON c.id_empresa = eg.id_empresa
