with source as (
    select * from {{ source('ecommerce', 'customers') }}
),

renamed as (
    select
        customer_id,
        signup_date::date as signup_date,
        country
    from source
)

select * from renamed