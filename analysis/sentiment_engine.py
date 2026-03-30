import pandas as pd
from textblob import TextBlob
import os

def calculate_sentiment(text):
    if pd.isna(text):
        return 0.0
    blob = TextBlob(str(text))
    # Normalize polarity (-1 to 1) to a 0 to 1 scale for easier UI rendering
    return round((blob.sentiment.polarity + 1) / 2, 2)

def process_and_clean_data(input_path="data/raw_products.csv", output_path="data/cleaned_products.csv"):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return None

    df = pd.read_csv(input_path)
    
    # Apply sentiment analysis on the review text
    df['Sentiment_Score'] = df['Review_Text'].apply(calculate_sentiment)
    
    # Aggregate product data so we have one row per product for the dashboard
    # while averaging the sentiment of its underlying reviews.
    cleaned_df = df.groupby(['Brand', 'Product Title', 'Price', 'List Price', 'Discount', 'Rating', 'Review Count']).agg({
        'Sentiment_Score': 'mean'
    }).reset_index()

    cleaned_df.to_csv(output_path, index=False)
    print(f"Data cleaned and NLP sentiment applied. Saved to {output_path}")
    return cleaned_df

if __name__ == "__main__":
    process_and_clean_data()