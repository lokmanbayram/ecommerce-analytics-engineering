# E-Commerce Analytics Engineering Project

## Overview
This project is an end-to-end Analytics Engineering portfolio piece demonstrating the modern data stack. It simulates a realistic data pipeline for an e-commerce company, focusing on data extraction, transformation, testing, and modeling using industry best practices.

The pipeline avoids the need for paid cloud data warehouses (like Snowflake or BigQuery) by leveraging **DuckDB** for lightning-fast, local data processing, highlighting a strong understanding of cost-optimization strategies. 

## Architecture & Tech Stack
*   **Data Generation & Ingestion:** Python (pandas, numpy)
*   **Data Warehouse:** DuckDB
*   **Data Transformation:** dbt (Data Build Tool)
*   **Development Environment:** VS Code on Windows

## Data Modeling Strategy
The project strictly follows the standard `raw -> staging -> marts` architecture:

1.  **Raw Layer (`raw`):** Simulated 10,000 customers and 50,000 relational orders generated via Python and ingested directly into DuckDB.
2.  **Staging Layer (`staging`):** Source configurations and initial data type casting (e.g., date formatting).
3.  **Marts Layer (`marts/core`):** 
    *   `fct_orders`: Centralized fact table joining orders with customer geography.
    *   `dim_customers`: Customer 360 dimension table utilizing advanced aggregations (first/last order dates, total lifetime value).

## Data Quality & Testing
Data reliability is ensured through dbt's generic tests defined in `core.yml`, enforcing primary key uniqueness, non-null constraints, and accepted values for critical categorical fields (e.g., order statuses).

## How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/lokmanbayram/ecommerce-analytics-engineering.git](https://github.com/lokmanbayram/ecommerce-analytics-engineering.git)
    cd ecommerce-analytics-engineering
    ```

2.  **Set up the Python Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Generate Mock Data and DuckDB Database:**
    ```bash
    python scripts/generate_mock_data.py
    ```

4.  **Run dbt Pipeline:**
    ```bash
    cd ecommerce_dbt
    dbt run --profiles-dir .
    dbt test --profiles-dir .
    ```