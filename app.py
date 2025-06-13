import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

st.set_page_config(page_title="Walmart Sales + Store Dashboard", layout="wide")
st.title("🛒 Walmart Store Sales + Forecast Dashboard")

# Upload files
sales_file = st.file_uploader("Upload Walmart Sales CSV", type=["csv"], key="sales")
store_file = st.file_uploader("Upload Walmart Store Location CSV", type=["csv"], key="store")

if sales_file and store_file:
    # Load & normalize sales data
    df_sales = pd.read_csv(sales_file)
    df_sales.columns = df_sales.columns.str.strip().str.lower()
    required_cols = {"store", "date", "weekly_sales"}
    if not required_cols.issubset(df_sales.columns):
        st.error("❌ Sales file must contain: 'Store', 'Date', 'Weekly_Sales'")
        st.write("Uploaded columns:", df_sales.columns.tolist())
        st.stop()
    df_sales.rename(columns={"store": "Store", "date": "Date", "weekly_sales": "Weekly_Sales"}, inplace=True)
    df_sales["Date"] = pd.to_datetime(df_sales["Date"], dayfirst=True)

    # Load & prepare store data
    df_store = pd.read_csv(store_file)
    df_store.columns = df_store.columns.str.strip().str.lower()
    if "url" in df_store.columns:
        df_store["Store"] = df_store["url"].str.extract(r'/store/(\d+)/', expand=False).astype(float).astype("Int64")

    # Merge on Store
    df_merged = pd.merge(df_sales, df_store, on="Store", how="inner")

    # Sidebar filter
    selected_store = st.sidebar.selectbox("📍 Select a Store", sorted(df_merged["Store"].unique()))
    df_selected = df_merged[df_merged["Store"] == selected_store]

    # 📈 Line chart
    st.subheader(f"📊 Weekly Sales - Store {selected_store}")
    fig = px.line(df_selected, x="Date", y="Weekly_Sales", title=f"Weekly Sales for Store {selected_store}")
    st.plotly_chart(fig, use_container_width=True)

    # 🔮 Prophet Forecast
    st.subheader("🔮 Forecast: Next 12 Weeks")
    df_prophet = df_selected.rename(columns={"Date": "ds", "Weekly_Sales": "y"})
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=12, freq="W")
    forecast = model.predict(future)
    fig_forecast = px.line(forecast, x="ds", y="yhat", title="Forecasted Sales")
    st.plotly_chart(fig_forecast, use_container_width=True)

    # 🗺️ Map
    if "latitude" in df_merged.columns and "longitude" in df_merged.columns:
        st.subheader("🗺️ Store Location Map")
        df_map = df_merged.drop_duplicates("Store")
        fig_map = px.scatter_mapbox(
            df_map,
            lat="latitude",
            lon="longitude",
            hover_name="name",
            zoom=3,
            mapbox_style="carto-positron"
        )
        st.plotly_chart(fig_map, use_container_width=True)

    st.success("✅ Dashboard loaded successfully.")

else:
    st.warning("📤 Please upload both the Walmart Sales and Store Location CSV files.")
