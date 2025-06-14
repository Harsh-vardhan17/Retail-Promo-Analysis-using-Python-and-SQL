# Retail-Promo-Analysis-using-Python-and-SQL

### This project explores, visualizes, and forecasts Walmart's weekly sales performance across U.S. stores from 2010 to 2013. It leverages **Google BigQuery (SQL)** for data retrieval, **Pandas/Plotly** for visualization, and **Prophet** for forecasting future sales trends. The final dashboard is deployed using **Streamlit**.
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
```
---
## 📊 Sample Streamlit Dashboard
<img width="1710" alt="Screenshot 2025-06-13 at 11 21 12 AM" src="https://github.com/user-attachments/assets/d47332ae-d69d-4a68-90a5-cacba1207ebf" />

---

## 🤝 Acknowledgements
- Walmart Sales Dataset (public domain)

- Prophet by Meta for forecasting

- Streamlit for rapid dashboarding
---
## 🎯 Future Works
### Live BigQuery Integration
Replace static CSV uploads with real-time querying directly from Google BigQuery for dynamic, up-to-date analysis.

### Incorporate External Datasets
Enrich analysis with additional data like regional demographics, localized weather, and holiday calendars to uncover deeper patterns.

### Advanced Forecasting Models
Experiment with ARIMA, LSTM, or NeuralProphet to compare and improve forecasting accuracy beyond Prophet’s baseline.

### Interactive Dashboard Features
Add filters for state/store/category, KPI summary panels, and custom date range selectors for a more dynamic user experience.

### Promo Impact Prediction (ML)
Train a regression or classification model to predict whether promotional weeks will increase sales and by how much.

### Backend & Database Integration
Add a backend (e.g., Flask/FastAPI) and connect to cloud storage like Firebase or AWS S3 to store and retrieve data programmatically.
