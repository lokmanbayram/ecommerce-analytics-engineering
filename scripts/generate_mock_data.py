import duckdb
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

num_customers = 10000
customer_ids = range(1, num_customers + 1)
signup_dates = [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_customers)]
countries = np.random.choice(['USA', 'UK', 'Germany', 'France', 'Turkey'], num_customers, p=[0.4, 0.2, 0.15, 0.15, 0.1])

customers_df = pd.DataFrame({
    'customer_id': customer_ids,
    'signup_date': signup_dates,
    'country': countries
})

num_orders = 50000
order_ids = range(1, num_orders + 1)
order_customer_ids = np.random.choice(customer_ids, num_orders)
order_dates = [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 300)) for _ in range(num_orders)]
order_amounts = np.random.uniform(10.0, 500.0, num_orders).round(2)
statuses = np.random.choice(['completed', 'returned', 'cancelled'], num_orders, p=[0.85, 0.10, 0.05])

orders_df = pd.DataFrame({
    'order_id': order_ids,
    'customer_id': order_customer_ids,
    'order_date': order_dates,
    'amount': order_amounts,
    'status': statuses
})

con = duckdb.connect('ecommerce.duckdb')

con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

con.execute("CREATE OR REPLACE TABLE raw.customers AS SELECT * FROM customers_df;")
con.execute("CREATE OR REPLACE TABLE raw.orders AS SELECT * FROM orders_df;")

con.close()