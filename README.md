Rlist E-Commerce Intelligence Platform

Because raw data doesn't pay the bills. Clean, AI-powered insights do.

What is this?
You know that feeling when you open a CSV file with 100,000 rows and Excel just... gives up?
Yeah. I built the thing that doesn't give up.
This is a full end-to-end Data Engineering pipeline built on Databricks — ingesting messy real-world e-commerce data, cleaning it through three layers of architecture, and putting an AI brain on top that explains what the data is actually saying.
No demo data. No toy datasets. 300,000+ real transactions from Olist, Brazil's largest e-commerce marketplace.

The Architecture — aka The Three Rooms
Think of it like a restaurant kitchen:
   BRONZE    →       SILVER           →      GOLD
Raw ingredients    Cleaned & prepped    Ready to serve
(store as-is)     (joined & enriched)  (business KPIs)

What happens here?
Bronze - Raw data lands exactly as it arrives. No changes. No opinions.ecommerce.bronze.orders ecommerce.bronze.customers ecommerce.bronze.payments
Silver - Nulls handled. Dates fixed. Three tables joined into one powerful 98,816-row enriched dataset across 23 columns. Cancelled orders removed with documented reasoning.ecommerce.silver.orders_enriched
Gold - Business-ready aggregations. The stuff managers actually care about.ecommerce.gold.daily_revenue ecommerce.gold.revenue_by_state ecommerce.gold.delivery_performance
Every layer stored as Delta tables in Databricks Unity Catalog. Versioned. ACID compliant. Production-standard.

The AI Layer - This Is Where It Gets Fun
Three things the AI can do - none of which involve making things up:
1. Conversational Data Analyst
You  → "Which state has the best revenue growth potential?"
AI   → "Rio de Janeiro. Here's why — R$166 avg order value
        vs São Paulo's R$143, with 3x fewer orders.
        Untapped premium segment. Recommendation: ..."
2. Natural Language → SQL Engine
You type  → "Show me states with worst delivery performance"
AI writes → SELECT customer_state, avg_delay...
            FROM ecommerce.gold.delivery_performance
            ORDER BY avg_delay DESC LIMIT 10
Spark runs it → You get real results
3. Automated Anomaly Detector
Runs automatically across all Gold tables
Flags anything beyond 2 standard deviations
Sends anomalies to LLaMA 3
Gets back → What happened, Why it happened,
            Business impact, Recommended action
No hallucinations. Every answer comes from real Delta table data.

What The Pipeline Actually Found
These are not made-up numbers for a demo:

São Paulo generates R$5.94M — 37.5% of total platform revenue
Alagoas averages 21.4 days late on deliveries — 3σ above the national mean
Rio de Janeiro customers spend 16% more per order than São Paulo despite 3x fewer orders
The payments table has 4,445 more rows than the orders table — installment payment pattern hiding in plain sight

Tech Stack
pythonstack = {
    "Cloud Platform"    : "Databricks",
    "Storage"           : "Delta Lake + Unity Catalog",
    "Processing"        : "Apache Spark + PySpark",
    "Architecture"      : "Medallion (Bronze/Silver/Gold)",
    "LLM"               : "LLaMA 3 70B via Groq API",
    "ML Tracking"       : "MLflow",
    "Dashboard"         : "Streamlit + Plotly",
    "Language"          : "Python",
    "Dataset"           : "Olist Brazilian E-Commerce",
    "Version Control"   : "GitHub"
}

Project Structure
ecommerce-ai-pipeline/
│
├── notebooks/
│   ├── 01_bronze_ingestion.ipynb      ← Raw data → Delta tables
│   ├── 02_silver_transform.ipynb      ← Clean, join, enrich
│   ├── 03_gold_aggregation.ipynb      ← Business KPIs
│   ├── 04_llm_ai_features.ipynb       ← LLaMA 3 integration
│   └── 05_dashboard.ipynb             ← Visualization layer
│
├── app.py                             ← Streamlit dashboard
├── requirements.txt                   ← Dependencies
└── README.md                          ← You are here 👋

Things I learned building this

Data Engineering is not about moving files. It is about making data trustworthy at every layer.
Real data is never clean. The Silver layer is where the actual engineering happens.
Adding an LLM to a proper data pipeline is not a gimmick — it is what becomes possible when your data foundation is solid.
The payments table having more rows than the orders table is not a bug. It is a business model.
Databricks Unity Catalog is the future. File paths are the past.

🔗 Links
🌐 Live Dashboard - https://rlist-intelligence-data-engineering-platform.streamlit.app
💼 LinkedIn - https://www.linkedin.com/in/ramya-velmurugan-6251a0217/
🐙 GitHubhttps://github.com/RAMYA-V-7
