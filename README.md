# Moonshot AI Agent Internship: Luggage Competitive Intelligence

**Live Dashboard:** [https://moonshot-luggage-intelligence-dashboard-1.streamlit.app/]
**Walkthrough Video:** [(https://www.loom.com/share/922d2c11e3df477dbf92df89b7593a2a)]

---

## Project Objective

This project is a competitive intelligence dashboard designed to synthesize marketplace signals from Amazon India into a decision-ready interface. It tracks major luggage brands like Safari, Skybags, American Tourister, and VIP, analyzing pricing strategies, discount reliance, and customer sentiment to surface non-obvious market dynamics.

---

## Submission Deliverables Included

As per the assignment requirements, this submission package includes:

- **Working Dashboard:** Deployed live via Streamlit Cloud.
- **Source Code:** Modular architecture pushed to this repository.
- **README:** Documentation covering setup, approach, and limitations.
- **Cleaned Dataset:** Located in `data/cleaned_products.csv`.

---

## System Architecture & Approach

The pipeline is broken into four distinct layers:

1. **Scraping Layer** (`scraper/amazon_scraper.py`): Built with Playwright to render JavaScript-heavy Amazon India listings and reviews.
2. **Analysis Layer** (`analysis/sentiment_engine.py`): Utilizes Pandas and TextBlob for data cleaning and baseline NLP sentiment calculation.
3. **Intelligence Layer** (`analysis/agent_insights.py`): Integrates the Groq API (Llama 3) to automatically generate 5 non-obvious strategic conclusions from the data.
4. **Presentation Layer** (`app.py`): Built with Streamlit to provide a clean, interactive UI for decision-makers.

---

## Local Setup Instructions

### 1. Prerequisites

- Python 3.9+
- Groq API Key

### 2. Installation

Clone the repository:

```powershell
git clone https://github.com/rohit1915-08/Moonshot-Luggage-Intelligence-Dashboard.git
cd moonshot_luggage_dashboard
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
playwright install chromium
```

Configure environment variables — create a `.env` file in the root directory and add your API key:

```
GROQ_API_KEY="your_actual_api_key_here"
```

---

## Running the Data Pipeline

To execute the pipeline from scratch, run these commands in order:

**1. Scrape live data:**

```powershell
python scraper/amazon_scraper.py
```

**2. Clean data and apply NLP sentiment:**

```powershell
python analysis/sentiment_engine.py
```

**3. Launch the dashboard:**

```powershell
streamlit run app.py
```

---

## Limitations & Future Improvements

- **Bot Mitigation:** Current scraping is subject to Amazon's request limits; future versions could implement rotating proxies.
- **Aspect-Level Sentiment:** Expanding NLP to specifically analyze wheels, handles, and zippers for deeper durability insights.
- **Historical Trends:** Transitioning from a snapshot to a time-series database to track pricing fluctuations over time.
