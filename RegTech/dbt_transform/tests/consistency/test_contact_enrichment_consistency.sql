with base_contacts as (
    select count(*) as base_count
    from {{ ref('stg__fato_contacto') }}
),
enriched_contacts as (
    select count(*) as enriched_count
    from {{ ref('int__fato_contato_enriched') }}
),
final_contacts as (
    select count(*) as final_count
    from {{ ref('fato_contato_final') }}
)

select *
from base_contacts
cross join enriched_contacts
cross join final_contacts
where base_count != enriched_count 
   or enriched_count != final_count