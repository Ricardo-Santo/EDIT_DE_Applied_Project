SELECT
  e.*,
  g.lat,
  g.lon
FROM {{ ref('stg__dim_empresa') }} e
LEFT JOIN {{ ref('geo_location_data') }} g
  ON e.estado = g.state