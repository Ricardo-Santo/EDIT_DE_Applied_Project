with manual_calculation as (
    select 
        id_cliente,
        nome_cliente,
        count(*) as calculated_total
    from {{ ref('int__fato_contato_enriched') }}
    group by id_cliente, nome_cliente
),
reported_totals as (
    select 
        id_cliente,
        nome_cliente,
        total_contatos_cliente
    from {{ ref('fato_contato_final') }}
),
comparison as (
    select 
        m.id_cliente,
        m.nome_cliente,
        m.calculated_total,
        r.total_contatos_cliente
    from manual_calculation m
    join reported_totals r
        on m.id_cliente = r.id_cliente
    where m.calculated_total != r.total_contatos_cliente
)

select * from comparison