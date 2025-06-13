-- 1. Total Weekly Sales\
SELECT Date, SUM(Weekly_Sales) AS Total_Sales
FROM `project.dataset.walmart_sales`
GROUP BY Date
ORDER BY Date;

-- 2. Top Performing Stores\
SELECT Store, SUM(Weekly_Sales) AS Total_Sales
FROM `project.dataset.walmart_sales`
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;

-- 3. Promo vs Non-Promo\
SELECT Holiday_Flag, AVG(Weekly_Sales) AS Avg_Sales
FROM `project.dataset.walmart_sales`
GROUP BY Holiday_Flag;

-- 4. Store-wise Sales Over Time\
SELECT Date, Store, SUM(Weekly_Sales) AS Weekly_Sales
FROM `project.dataset.walmart_sales`
GROUP BY Date, Store
ORDER BY Date;
