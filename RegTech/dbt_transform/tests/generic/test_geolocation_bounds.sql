with invalid_coordinates as (
    select 
        id_empresa,
        nome_empresa,
        estado,
        lat,
        lon
    from {{ ref('int__empresa_geolocation') }}
    where lat < -35 or lat > 5 or lon < -75 or lon > -30
)

select * from invalid_coordinates