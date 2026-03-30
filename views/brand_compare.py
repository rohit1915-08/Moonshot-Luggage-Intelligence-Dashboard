import streamlit as st
import plotly.express as px

def render(df):
    st.title("Brand Comparison Matrix")
    
    brand_agg = df.groupby('Brand').agg({
        'Price': 'mean',
        'Discount': 'mean',
        'Sentiment_Score': 'mean',
        'Rating': 'mean'
    }).reset_index()

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Average Selling Price vs Brand")
        fig1 = px.bar(brand_agg, x='Brand', y='Price', color='Price', color_continuous_scale='Oranges')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("### Sentiment Score Benchmark")
        fig2 = px.bar(brand_agg, x='Brand', y='Sentiment_Score', color='Sentiment_Score', color_continuous_scale='Blues')
        st.plotly_chart(fig2, use_container_width=True)
        
    st.markdown("### Detailed Comparison Table")
    st.dataframe(brand_agg.style.format({
        'Price': '₹{:.2f}',
        'Discount': '{:.1f}%',
        'Sentiment_Score': '{:.2f}',
        'Rating': '{:.1f} ★'
    }), use_container_width=True)