with cnpj_comparison as (
    select 
        e.cnpj as empresa_cnpj,
        p.CNPJ as pix_cnpj,
        e.nome_empresa,
        p.nome_reduzido
    from {{ ref('int__empresa_geolocation') }} e
    join {{ ref('stg__dim_pix') }} p
        on trim(e.cnpj) = trim(p.CNPJ)
    where e.cnpj != p.CNPJ
)

select * from cnpj_comparison