import streamlit as st
import pandas as pd
from components.ui_styling import apply_amazon_theme
from views import overview, brand_compare, product_drilldown

# Initialize UI
st.set_page_config(page_title="Moonshot Luggage Intelligence", layout="wide")
apply_amazon_theme()

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg", width=150)
st.sidebar.title("Navigation")
view_selection = st.sidebar.radio("Select View", ["Overview", "Brand Comparison", "Product Drilldown"])

@st.cache_data
def load_data():
    try:
        data = pd.read_csv("data/cleaned_products.csv")
        return data
    except FileNotFoundError:
        st.error("Cleaned dataset not found. Please run the scraper and sentiment engine first.")
        st.stop()

df = load_data()

# Global Filters
st.sidebar.markdown("---")
st.sidebar.subheader("Filters")

# Brand Filter
selected_brands = st.sidebar.multiselect("Select Brands", df['Brand'].unique(), default=df['Brand'].unique())

# Price Filter
min_price, max_price = st.sidebar.slider(
    "Price Range (₹)", 
    min_value=float(df['Price'].min()), 
    max_value=float(df['Price'].max()), 
    value=(float(df['Price'].min()), float(df['Price'].max()))
)

# Rating Filter
min_rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 3.0, 0.1)

# Sentiment Filter
selected_sentiment = st.sidebar.selectbox("Sentiment", ["All", "Positive", "Neutral", "Negative"])

# Apply all filters
filtered_df = df[
    (df['Brand'].isin(selected_brands)) & 
    (df['Price'] >= min_price) & 
    (df['Price'] <= max_price) & 
    (df['Rating'] >= min_rating)
]

if selected_sentiment != "All":
    if selected_sentiment == "Positive":
        filtered_df = filtered_df[filtered_df['Sentiment_Score'] > 0.3]
    elif selected_sentiment == "Negative":
        filtered_df = filtered_df[filtered_df['Sentiment_Score'] < 0.0]
    else:
        filtered_df = filtered_df[(filtered_df['Sentiment_Score'] >= 0.0) & (filtered_df['Sentiment_Score'] <= 0.3)]


if view_selection == "Overview":
    overview.render(filtered_df)
elif view_selection == "Brand Comparison":
    brand_compare.render(filtered_df)
elif view_selection == "Product Drilldown":
    product_drilldown.render(filtered_df)