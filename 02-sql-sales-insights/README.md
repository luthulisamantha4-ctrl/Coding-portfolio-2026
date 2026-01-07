# Project 02 — SQL Sales Insights (PostgreSQL)

This project reproduces the key metrics from Project 01 using SQL queries in PostgreSQL.

## What it demonstrates
- Loading CSV data into PostgreSQL
- Writing aggregate queries (SUM, GROUP BY)
- Cleaning messy text data (TRIM, NULLIF, COALESCE)
- Producing business insights directly in SQL

## How to run
1) Start PostgreSQL:
brew services start postgresql@14

2) Open psql:
psql portfolio

3) Run the queries:
\i 02-sql-sales-insights/queries.sql

## Notes
This project assumes the `sales_raw` table already exists and has been populated from:
01-python-sales-insights/data/sales.csv
