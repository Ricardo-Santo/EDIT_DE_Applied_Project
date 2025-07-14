with staging_count as (
    select count(distinct id_cliente) as count_staging
    from {{ ref('stg__dim_client') }}
),
final_count as (
    select count(distinct id_cliente) as count_final
    from {{ ref('dim_clientes_final') }}
)

select *
from staging_count
cross join final_count
where count_staging != count_final