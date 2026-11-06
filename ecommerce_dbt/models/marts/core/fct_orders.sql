with orders as (
    select * from {{ ref('stg_orders') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

final as (
    select
        orders.order_id,
        orders.customer_id,
        customers.country,
        orders.order_date,
        orders.amount,
        orders.status
    from orders
    left join customers
        on orders.customer_id = customers.customer_id
)

select * from final