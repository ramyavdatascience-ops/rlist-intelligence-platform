# ◈ RList E-Commerce Intelligence Platform

> Because raw data doesn't pay the bills. Clean, AI-powered insights do.

---

## 🚀 What is this?

You know that feeling when you open a CSV file with 100,000 rows and Excel just... gives up?

Yeah. This is the system that **doesn’t give up**.

This project is a **full end-to-end Data Engineering pipeline** built on **Databricks**, designed to:

* Ingest messy real-world e-commerce data
* Transform it through a **Medallion Architecture (Bronze → Silver → Gold)**
* Power an **AI layer (LLaMA 3)** that explains what the data actually means

📦 **Dataset**: 300,000+ real transactions from Olist (Brazil’s largest e-commerce platform)
❌ No toy data. No mock dashboards.

---

## 🏗️ Architecture — The Three Layers

Think of it like a restaurant kitchen:

```
BRONZE  →  SILVER  →  GOLD
Raw        Clean       Business-ready
```

---

### 🥉 Bronze Layer — Raw Ingestion

* Data stored **as-is**
* No transformations, no assumptions

```
ecommerce.bronze.orders  
ecommerce.bronze.customers  
ecommerce.bronze.payments
```

---

### 🥈 Silver Layer — Data Engineering Core

* Null handling
* Data type corrections
* Table joins & enrichment
* Business logic applied

📊 Output:

* **98,816 rows**
* **23 columns**
* Cancelled orders removed (with reasoning)

```
ecommerce.silver.orders_enriched
```

---

### 🥇 Gold Layer — Business Intelligence

Aggregated, decision-ready datasets:

```
ecommerce.gold.daily_revenue  
ecommerce.gold.revenue_by_state  
ecommerce.gold.delivery_performance
```

---

### 💡 Storage & Governance

* Delta Lake tables
* Unity Catalog
* ACID compliant
* Fully versioned

---

## 🤖 AI Layer — Where It Gets Interesting

This is not a chatbot. This is a **data-aware AI system**.

---

### 1️⃣ Conversational Data Analyst

```
You: Which state has the best revenue growth potential?

AI: Rio de Janeiro.
    R$166 avg order value vs São Paulo's R$143,
    with 3x fewer orders → untapped premium segment.
```

---

### 2️⃣ Natural Language → SQL Engine

```
You: Show me states with worst delivery performance

AI generates:
SELECT customer_state, avg_delay
FROM ecommerce.gold.delivery_performance
ORDER BY avg_delay DESC
LIMIT 10;
```

Executed on Spark → returns real results.

---

### 3️⃣ Automated Anomaly Detection

* Detects deviations (> 2 standard deviations)
* Sends signals to LLaMA 3
* Returns:

  * What happened
  * Why it happened
  * Business impact
  * Recommended action

---

## 📊 Key Insights (Real Data)

* São Paulo generates **R$5.94M (37.5% of total revenue)**
* Alagoas has **21.4-day average delivery delay (3σ above mean)**
* Rio de Janeiro customers spend **16% more per order than SP**
* Payments table has **4,445 more rows than orders**
  → Indicates installment payment behavior

---

## 🛠️ Tech Stack

```python
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
```

---

## 📂 Project Structure

```
ecommerce-ai-pipeline/
│
├── notebooks/
│   ├── 01_bronze_ingestion.ipynb
│   ├── 02_silver_transform.ipynb
│   ├── 03_gold_aggregation.ipynb
│   ├── 04_llm_ai_features.ipynb
│   └── 05_dashboard.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Key Learnings

* Data Engineering is not about moving data — it's about making it **trustworthy**
* Real-world data is messy — the **Silver layer is where engineering matters**
* LLMs become powerful only when built on **clean, structured data**
* Extra rows in payments table ≠ bug → **business insight**
* Unity Catalog > file-based pipelines

---

## 🔗 Links

🌐 **Live Dashboard**
https://rlist-intelligence-data-engineering-platform.streamlit.app

💼 **LinkedIn**
https://www.linkedin.com/in/ramya-velmurugan-6251a0217/

🐙 **GitHub**
https://github.com/RAMYA-V-7

---

## ⭐ Final Note

This project demonstrates how **modern data engineering + AI** can move beyond dashboards and into **decision intelligence systems**.
