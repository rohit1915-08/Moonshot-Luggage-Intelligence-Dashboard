import streamlit as st

def apply_amazon_theme():
    st.markdown("""
        <style>
        /* Amazon Dark Blue Header */
        [data-testid="stHeader"] {
            background-color: #232F3E;
        }
        
        /* Buttons - Amazon Custom Styling */
        div.stButton > button:first-child {
            background-color: #FF9900 !important;
            color: #000000 !important;
            border: 1px solid #A88734 !important;
            border-radius: 4px;
        }
        div.stButton > button:first-child:hover {
            background-color: #FA8900 !important;
        }
        </style>
    """, unsafe_allow_html=True)