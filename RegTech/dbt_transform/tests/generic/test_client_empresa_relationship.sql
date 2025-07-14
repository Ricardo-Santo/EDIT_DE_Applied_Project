with client_empresa_check as (
    select 
        c.id_cliente,
        c.nome,
        c.id_empresa,
        e.nome_empresa
    from {{ ref('stg__dim_client') }} c
    left join {{ ref('stg__dim_empresa') }} e
        on c.id_empresa = e.id_cliente
    where e.nome_empresa is null
)

select * from client_empresa_check