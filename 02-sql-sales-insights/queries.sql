-- Project 02 — SQL Sales Insights (PostgreSQL)

-- 1) Sanity checks
SELECT COUNT(*) AS rows FROM sales_raw;
SELECT * FROM sales_raw LIMIT 5;

-- 2) Headline metrics (matches Python summary)
SELECT
  COUNT(*) AS rows_processed,
  SUM(quantity) AS total_quantity_sold,
  ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM sales_raw;

-- 3) Top product by revenue
SELECT
  product,
  ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales_raw
GROUP BY product
ORDER BY revenue DESC
LIMIT 1;

-- 4) Top city by revenue (clean blanks -> 'Unknown')
SELECT
  COALESCE(NULLIF(TRIM(city), ''), 'Unknown') AS city_clean,
  ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales_raw
GROUP BY city_clean
ORDER BY revenue DESC
LIMIT 1;

-- 5) Revenue by product (full breakdown)
SELECT
  product,
  SUM(quantity) AS quantity_sold,
  ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales_raw
GROUP BY product
ORDER BY revenue DESC;

-- 6) Revenue by channel (clean blanks -> 'Unknown')
SELECT
  COALESCE(NULLIF(TRIM(channel), ''), 'Unknown') AS channel_clean,
  ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales_raw
GROUP BY channel_clean
ORDER BY revenue DESC;
