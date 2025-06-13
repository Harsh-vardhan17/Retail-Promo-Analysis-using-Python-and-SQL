# Retail-Promo-Analysis-using-Python-and-SQL

### This project explores, visualizes, and forecasts Walmart's weekly sales performance across U.S. stores. It leverages **Google BigQuery (SQL)** for data retrieval, **Pandas/Plotly** for visualization, and **Prophet** for forecasting future sales trends. The final dashboard is deployed using **Streamlit**.
---
## 📦 Features

- 📊 Total and store-level weekly sales trends
- 🏆 Top 10 best-performing stores
- 🎯 Comparison of promotional vs non-promotional weeks
- 📍 Geographic store sales mapping
- 🔮 12-week sales forecast using Prophet
- ✅ Interactive Streamlit dashboard with file upload support
---
## 🚀 Tech Stack

| Technology      | Purpose                            |
|----------------|-------------------------------------|
| **Python**      | Data processing, modeling, dashboard |
| **Google BigQuery** | SQL-based data analysis           |
| **Prophet**     | Time-series forecasting             |
| **Plotly**      | Interactive charts & maps           |
| **Pandas**      | Data manipulation                   |
| **Streamlit**   | Web app for visualization           |

---
## 📁 File Overview

| File/Folder                 | Description                                 |
|----------------------------|---------------------------------------------|
| `Retail_Promo_Analysis_PRESENTABLE.ipynb` | Final EDA + SQL query notebook         |
| `app.py`                   | Streamlit dashboard app                     |
| `queries.sql`              | BigQuery SQL queries used                   |
| `Walmart_Sales.csv`        | Weekly sales dataset                        |
| `walmart_store_locaction.csv` | Store location info                        |
| `requirements.txt`         | App dependencies                            |

---
## 📊 Sample SQL Query (BigQuery)
```sql
SELECT Store, SUM(Weekly_Sales) AS Total_Sales
FROM `retail-1-462621.walmart_data_1.walmart_sales`
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;
