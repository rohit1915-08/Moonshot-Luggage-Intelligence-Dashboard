# Moonshot AI Agent Internship: Luggage Competitive Intelligence

**Live Dashboard:** [Insert Your Streamlit Cloud Link Here]
**Walkthrough Video:** [Insert Your Loom Link Here]

## Project Objective

This project is a competitive intelligence dashboard designed to synthesize messy marketplace signals from Amazon India into a decision-ready interface. It tracks 6 major luggage brands (Safari, Skybags, American Tourister, VIP, Aristocrat, Nasher Miles), analyzing pricing strategies, discount reliance, and customer sentiment to surface non-obvious market dynamics.

## System Architecture & Approach

The pipeline is broken into four distinct layers:

1. **Scraping Layer (`scraper/amazon_scraper.py`):** - Built with **Playwright** (async) to render JavaScript-heavy Amazon pages.
   - Implements human-like delays, random user-agent rotation, and a smart-retry loop to bypass Amazon's 503 WAF (Web Application Firewall) blocks.
   - Extracts product titles, selling prices, list prices, discounts, ratings, and review counts.

2. **Analysis Layer (`analysis/sentiment_engine.py`):**
   - Utilizes **Pandas** for data cleaning and aggregation.
   - Implements **TextBlob** for baseline NLP sentiment calculation, normalizing polarity scores to a 0.0 - 1.0 scale to identify positive, neutral, and negative product reception.

3. **Intelligence Layer (`analysis/agent_insights.py`):**
   - Integrates the **Groq API (Llama 3)** to act as an autonomous agent.
   - Instead of static reporting, the LLM analyzes the aggregated statistical matrix to automatically generate 5 non-obvious strategic insights (e.g., Value vs. Sentiment Traps, Discount Elasticity).

4. **Presentation Layer (`app.py` & `views/`):**
   - Built entirely in **Streamlit**.
   - Features custom CSS mimicking Amazon's native UI (Dark Navy and Orange palette) to reduce cognitive load for e-commerce decision-makers.
   - Includes dynamic filtering (brand, price, rating, sentiment) and interactive Plotly visualization matrices.

## Local Setup Instructions

### Prerequisites

- Python 3.9+
- Groq API Key

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/rohit1915-08/Moonshot-Luggage-Intelligence-Dashboard]
   cd moonshot_luggage_dashboard
   ```
