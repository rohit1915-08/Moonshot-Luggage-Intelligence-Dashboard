import streamlit as st
from analysis.agent_insights import generate_agent_insights

def render(df):
    st.title("Market Intelligence Overview")
    st.markdown("Aggregated analysis of Amazon India luggage listings.")

    # Top Level Metrics
   # Top Level Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Brands Tracked", df['Brand'].nunique())
    col2.metric("Total Products", len(df))
    col3.metric("Total Reviews Analyzed", df['Review Count'].sum())
    col4.metric("Avg Market Price", f"₹{df['Price'].mean():.2f}")
    col5.metric("Avg Sentiment", f"{df['Sentiment_Score'].mean():.2f}")

    st.markdown("---")
    st.subheader("Agent Insights")
    st.markdown("Automated strategic takeaways derived from unstructured data analysis.")
    
    insights = generate_agent_insights(df)
    for idx, insight in enumerate(insights, 1):
        st.info(f"**{idx}.** {insight}")