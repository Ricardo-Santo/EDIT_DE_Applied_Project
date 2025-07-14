with empresa_staging as (
    select count(distinct id_empresa) as staging_count
    from {{ ref('stg__dim_empresa') }}
),
empresa_geo as (
    select count(distinct id_empresa) as geo_count
    from {{ ref('int__empresa_geolocation') }}
)

select *
from empresa_staging
cross join empresa_geo
where staging_count != geo_count