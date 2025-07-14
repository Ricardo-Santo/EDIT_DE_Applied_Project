with invalid_emails as (
    select 
        id_cliente,
        nome,
        email
    from {{ ref('dim_clientes_final') }}
    where email not like '%@%'
       or email like '%@%@%'
       or email like '@%'
       or email like '%@'
       or length(email) < 5
)

select * from invalid_emails