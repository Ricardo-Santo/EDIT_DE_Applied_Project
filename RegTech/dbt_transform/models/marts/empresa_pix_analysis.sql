SELECT *
FROM {{ ref('int__empresa_pix') }}
WHERE autorizada_bcb = 'Sim'
