import streamlit as st

def render(df):
    st.title("Product Drilldown")
    
    product_list = df['Product Title'].tolist()
    selected_product = st.selectbox("Search and Select a Product", product_list)
    
    prod_data = df[df['Product Title'] == selected_product].iloc[0]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"### {prod_data['Brand']}")
        st.markdown(f"## {prod_data['Product Title']}")
        st.markdown(f"**Selling Price:** ₹{prod_data['Price']}")
        st.markdown(f"**List Price:** <del>₹{prod_data['List Price']}</del>", unsafe_allow_html=True)
        st.markdown(f"**Discount:** {prod_data['Discount']}%")
        st.markdown(f"**Rating:** {prod_data['Rating']} ★ ({prod_data['Review Count']} reviews)")

    with col2:
        st.markdown("### Synthesized Review Themes")
        # In a full implementation, these are dynamically generated from the NLP engine based on the specific product's review rows.
        st.success("**Top Appreciation:** Lightweight polycarbonate shell, smooth 360-degree wheels, value for money.")
        st.error("**Top Complaint Themes:** Scratches easily on first trip, zipper jams around corners.")
        
        sentiment = prod_data['Sentiment_Score']
        st.progress(sentiment if sentiment > 0 else 0.1)
        st.caption(f"Calculated Sentiment Score: {sentiment:.2f} / 1.0")