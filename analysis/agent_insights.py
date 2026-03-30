import os
from groq import Groq
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_agent_insights(df_products):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return ["Error: GROQ_API_KEY not found in environment variables."]

    client = Groq(api_key=api_key)
    
    # Aggregate data for the LLM context
    brand_metrics = df_products.groupby('Brand').agg({
        'Price': 'mean',
        'Rating': 'mean',
        'Discount': 'mean',
        'Sentiment_Score': 'mean'
    }).round(2).to_dict(orient='records')

    prompt = f"""
    Analyze this competitive luggage data from Amazon India: 
    {brand_metrics}
    
    Provide exactly 5 short, non-obvious, strategic insights for a decision-maker (e.g., value vs sentiment traps, premium positioning success).
    Output ONLY a numbered list (1 to 5). Do not include any introductory or concluding text.
    """

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.3,
        )
        
        content = response.choices[0].message.content.strip()
        
        # Clean up the response into a python list
        insights = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Remove the numbering from the strings since Streamlit handles the formatting
        cleaned_insights = [insight.split('. ', 1)[-1] if '. ' in insight else insight for insight in insights]
        
        return cleaned_insights[:5]
        
    except Exception as e:
        return [f"Groq API Error: {str(e)}"]