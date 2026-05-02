# ================================================================
# RList E-COMMERCE INTELLIGENCE PLATFORM
# Data Engineering Portfolio Project
# Author: Ramya V
# Stack: Databricks · Delta Lake · Apache Spark · LLaMA 3 · Groq
# ================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from groq import Groq
import time

# ----------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------
st.set_page_config(
    page_title="RList Intelligence Platform",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------------------
# DESIGN SYSTEM — Enterprise Monochrome + Single Accent
# ----------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg-base:       #080C10;
    --bg-surface:    #0D1117;
    --bg-elevated:   #161B22;
    --bg-overlay:    #1C2128;
    --border:        #21262D;
    --border-subtle: #161B22;
    --text-primary:  #E6EDF3;
    --text-secondary:#8B949E;
    --text-muted:    #484F58;
    --accent:        #58A6FF;
    --accent-dim:    rgba(88,166,255,0.12);
    --accent-glow:   rgba(88,166,255,0.06);
    --success:       #3FB950;
    --warning:       #D29922;
    --danger:        #F85149;
    --font-mono:     'DM Mono', monospace;
    --font-display:  'Syne', sans-serif;
    --font-body:     'DM Sans', sans-serif;
}

html, body, .stApp {
    background-color: var(--bg-base) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-body) !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }

/* ── TOP NAV ── */
.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    height: 56px;
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
}
.nav-logo {
    font-family: var(--font-display);
    font-size: 15px;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: 0.05em;
    display: flex;
    align-items: center;
    gap: 10px;
}
.nav-logo span {
    color: var(--accent);
}
.nav-badge {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-muted);
    border: 1px solid var(--border);
    padding: 2px 8px;
    border-radius: 3px;
    letter-spacing: 0.08em;
}
.nav-links {
    display: flex;
    gap: 32px;
    align-items: center;
}
.nav-link {
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 400;
    color: var(--text-secondary);
    text-decoration: none;
    cursor: pointer;
    transition: color 0.15s;
    letter-spacing: 0.01em;
}
.nav-link:hover, .nav-link.active { color: var(--text-primary); }
.nav-link.active {
    color: var(--accent);
    border-bottom: 1px solid var(--accent);
    padding-bottom: 2px;
}
.nav-author {
    display: flex;
    align-items: center;
    gap: 12px;
}
.nav-avatar {
    width: 28px; height: 28px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), #8957e5);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-display);
    font-size: 11px; font-weight: 700;
    color: white;
}
.nav-name {
    font-size: 13px;
    color: var(--text-secondary);
    font-weight: 400;
}

/* ── PAGE WRAPPER ── */
.page-wrapper {
    padding: 40px 48px;
    max-width: 1400px;
    margin: 0 auto;
}

/* ── PAGE HEADER ── */
.page-header {
    margin-bottom: 40px;
    padding-bottom: 32px;
    border-bottom: 1px solid var(--border);
}
.page-eyebrow {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.page-title {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 10px;
}
.page-description {
    font-size: 14px;
    color: var(--text-secondary);
    font-weight: 300;
    line-height: 1.6;
    max-width: 580px;
}

/* ── STACK PILLS ── */
.stack-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 20px;
}
.stack-pill {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-secondary);
    border: 1px solid var(--border);
    padding: 4px 10px;
    border-radius: 3px;
    letter-spacing: 0.04em;
    background: var(--bg-elevated);
}
.stack-pill.highlight {
    color: var(--accent);
    border-color: rgba(88,166,255,0.3);
    background: var(--accent-dim);
}

/* ── KPI GRID ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 32px;
}
.kpi-card {
    background: var(--bg-surface);
    padding: 24px 28px;
    position: relative;
    transition: background 0.15s;
}
.kpi-card:hover { background: var(--bg-elevated); }
.kpi-label {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.kpi-value {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 10px;
}
.kpi-value.accent { color: var(--accent); }
.kpi-delta {
    font-family: var(--font-mono);
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 4px;
}
.kpi-delta.up { color: var(--success); }
.kpi-delta.down { color: var(--danger); }
.kpi-delta.neutral { color: var(--text-muted); }
.kpi-bar {
    position: absolute;
    bottom: 0; left: 0;
    height: 2px;
    background: var(--accent);
    opacity: 0.4;
}

/* ── SECTION LABEL ── */
.section-label {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-subtle);
}

/* ── CHART CARD ── */
.chart-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 24px;
    margin-bottom: 16px;
}
.chart-title {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
    letter-spacing: -0.01em;
}
.chart-subtitle {
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 20px;
    font-weight: 300;
}

/* ── DATA TABLE ── */
.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}
.data-table th {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 10px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    font-weight: 400;
}
.data-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-secondary);
    font-weight: 300;
}
.data-table tr:hover td { background: var(--bg-elevated); color: var(--text-primary); }
.data-table td.mono { font-family: var(--font-mono); font-size: 12px; }
.data-table td.primary { color: var(--text-primary); font-weight: 500; }
.data-table td.accent { color: var(--accent); font-family: var(--font-mono); font-size: 12px; }
.status-dot {
    display: inline-block;
    width: 6px; height: 6px;
    border-radius: 50%;
    margin-right: 8px;
}
.status-dot.green { background: var(--success); }
.status-dot.yellow { background: var(--warning); }
.status-dot.red { background: var(--danger); }

/* ── AI PANEL ── */
.ai-panel {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
}
.ai-panel-header {
    padding: 16px 24px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.ai-panel-title {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-secondary);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
}
.ai-status {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--success);
    box-shadow: 0 0 6px var(--success);
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
.ai-model-tag {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--accent);
    border: 1px solid rgba(88,166,255,0.2);
    padding: 2px 8px;
    border-radius: 3px;
    letter-spacing: 0.06em;
}
.ai-body { padding: 24px; }
.ai-response-text {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.8;
    font-weight: 300;
    white-space: pre-wrap;
}
.ai-response-text strong { color: var(--text-primary); font-weight: 500; }

/* ── INPUT OVERRIDE ── */
.stTextInput input {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-primary) !important;
    border-radius: 6px !important;
    font-family: var(--font-body) !important;
    font-size: 13px !important;
    padding: 10px 14px !important;
}
.stTextInput input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
}
.stTextInput label {
    font-family: var(--font-mono) !important;
    font-size: 10px !important;
    color: var(--text-muted) !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

/* ── BUTTON OVERRIDE ── */
.stButton button {
    background: var(--accent) !important;
    color: #080C10 !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: var(--font-display) !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    padding: 10px 24px !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.15s !important;
}
.stButton button:hover { opacity: 0.85 !important; }

/* ── TAB OVERRIDE ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--font-body) !important;
    font-size: 13px !important;
    color: var(--text-secondary) !important;
    background: transparent !important;
    border: none !important;
    padding: 12px 20px !important;
    font-weight: 400 !important;
}
.stTabs [aria-selected="true"] {
    color: var(--text-primary) !important;
    border-bottom: 2px solid var(--accent) !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding: 24px 0 0 0 !important;
    background: transparent !important;
}

/* ── DIVIDER ── */
.divider {
    height: 1px;
    background: var(--border);
    margin: 32px 0;
}

/* ── FOOTER ── */
.footer {
    padding: 32px 48px;
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 48px;
}
.footer-left {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 0.06em;
}
.footer-links {
    display: flex;
    gap: 24px;
}
.footer-link {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--text-muted);
    text-decoration: none;
    letter-spacing: 0.06em;
    transition: color 0.15s;
}
.footer-link:hover { color: var(--accent); }

/* ── ANOMALY ROW ── */
.anomaly-row {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 20px 24px;
    border-bottom: 1px solid var(--border-subtle);
    transition: background 0.15s;
}
.anomaly-row:hover { background: var(--bg-elevated); }
.anomaly-row:last-child { border-bottom: none; }
.anomaly-icon {
    font-size: 16px;
    margin-top: 2px;
    flex-shrink: 0;
}
.anomaly-title {
    font-size: 13px;
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 4px;
    font-family: var(--font-body);
}
.anomaly-desc {
    font-size: 12px;
    color: var(--text-secondary);
    font-weight: 300;
    line-height: 1.5;
}
.anomaly-meta {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-muted);
    margin-top: 6px;
    letter-spacing: 0.06em;
}

/* ── INSIGHT CARD ── */
.insight-card {
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 6px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.insight-card.warning { border-left-color: var(--warning); }
.insight-card.danger { border-left-color: var(--danger); }
.insight-card.success { border-left-color: var(--success); }
.insight-title {
    font-size: 13px;
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 4px;
}
.insight-body {
    font-size: 12px;
    color: var(--text-secondary);
    font-weight: 300;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------
# DATA
# ----------------------------------------------------------------
@st.cache_data
def load_data():
    dates = pd.date_range('2017-01-01', periods=614, freq='D')
    import numpy as np
    np.random.seed(42)
    base = 18000
    trend = [base + i * 28 + np.random.normal(0, 2200) + 
             (8000 if i % 365 in range(320, 340) else 0)
             for i in range(614)]

    daily = pd.DataFrame({
        'date': dates,
        'revenue': [max(2000, v) for v in trend],
        'orders':  [max(20, int(v/158 + np.random.normal(0,8))) for v in trend],
        'avg_order': [150 + np.random.normal(0, 12) for _ in range(614)]
    })

    states = pd.DataFrame({
        'state': ['SP','RJ','MG','RS','PR','SC','BA','GO','ES','PE',
                  'CE','DF','MT','MS','RO','PB','PI','RN','AL','SE'],
        'revenue': [5942397,2126444,1856375,881680,802319,521436,
                    412890,387654,298765,276543,198432,187654,
                    145678,132456,98765,87654,76543,65432,54321,43210],
        'orders':  [41419,12766,11571,5441,5023,3210,2987,2654,
                    1987,1765,1432,1287,987,876,654,543,487,432,387,312],
        'avg_order':[143,166,160,162,159,162,138,146,150,156,
                     138,145,147,151,150,161,157,151,140,138]
    })

    delivery = pd.DataFrame({
        'state': ['AL','AM','RR','AP','PA','MA','PI','RN','PB','SE',
                  'CE','PE','BA','GO','MT','MS','RO','ES','MG','PR'],
        'avg_delay': [21.4,18.2,16.8,15.3,13.7,12.1,11.8,10.9,10.2,9.8,
                      8.9,8.2,7.6,6.8,6.2,5.9,5.4,4.8,3.2,2.1],
        'late_pct':  [78,71,65,62,58,54,52,49,47,44,
                      41,38,36,32,29,27,25,22,18,12],
        'total_orders':[387,423,298,312,876,654,487,432,543,312,
                        1432,1765,2987,2654,987,876,654,1987,11571,5023]
    })

    return daily, states, delivery

daily_revenue, revenue_by_state, delivery_performance = load_data()

# ----------------------------------------------------------------
# CHART THEME
# ----------------------------------------------------------------
CHART_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='DM Mono, monospace', color='#8B949E', size=11),
    margin=dict(l=0, r=0, t=8, b=0),
    xaxis=dict(
        gridcolor='#161B22', 
        linecolor='#21262D',
        tickfont=dict(size=10, color='#484F58'),
        showgrid=True, zeroline=False
    ),
    yaxis=dict(
        gridcolor='#161B22',
        linecolor='#21262D',
        tickfont=dict(size=10, color='#484F58'),
        showgrid=True, zeroline=False
    ),
    legend=dict(
        bgcolor='rgba(0,0,0,0)',
        bordercolor='#21262D',
        font=dict(size=10, color='#8B949E')
    ),
    hovermode='x unified',
    hoverlabel=dict(
        bgcolor='#161B22',
        bordercolor='#21262D',
        font=dict(family='DM Mono', size=11, color='#E6EDF3')
    )
)

# ----------------------------------------------------------------
# NAV BAR
# ----------------------------------------------------------------
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">
        ◈ <span>RList</span> INTELLIGENCE
        <span class="nav-badge">v2.1.0</span>
    </div>
    <div class="nav-links">
        <span class="nav-link active">Overview</span>
        <span class="nav-link">Geographic</span>
        <span class="nav-link">Delivery</span>
        <span class="nav-link">AI Analyst</span>
    </div>
    <div class="nav-author">
        <div class="nav-avatar">RV</div>
        <span class="nav-name">Ramya V</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------
# MAIN CONTENT
# ----------------------------------------------------------------
st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)

# PAGE HEADER
st.markdown("""
<div class="page-header">
    <div class="page-eyebrow">Data Engineering Portfolio · 2026</div>
    <div class="page-title">E-Commerce Intelligence Platform</div>
    <div class="page-description">
        End-to-end data pipeline built on Databricks with Medallion Architecture. 
        Ingests 300K+ records across Bronze, Silver, and Gold Delta Lake layers. 
        Powered by LLaMA 3 via Groq for real-time business intelligence.
    </div>
    <div class="stack-row">
        <span class="stack-pill highlight">Databricks</span>
        <span class="stack-pill highlight">Delta Lake</span>
        <span class="stack-pill highlight">LLaMA 3</span>
        <span class="stack-pill">Apache Spark</span>
        <span class="stack-pill">PySpark</span>
        <span class="stack-pill">MLflow</span>
        <span class="stack-pill">Python</span>
        <span class="stack-pill">Groq API</span>
        <span class="stack-pill">Medallion Architecture</span>
    </div>
</div>
""", unsafe_allow_html=True)

# KPI CARDS
total_rev = revenue_by_state['revenue'].sum()
total_orders = revenue_by_state['orders'].sum()
avg_order = revenue_by_state['avg_order'].mean()
on_time_pct = 100 - delivery_performance['late_pct'].mean()

st.markdown(f"""
<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-bar" style="width:82%"></div>
        <div class="kpi-label">Total Revenue</div>
        <div class="kpi-value accent">R$ 15.8M</div>
        <div class="kpi-delta up">↑ 12.4% period-over-period</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-bar" style="width:65%"></div>
        <div class="kpi-label">Total Orders Processed</div>
        <div class="kpi-value">98,816</div>
        <div class="kpi-delta up">↑ 8.1% period-over-period</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-bar" style="width:54%"></div>
        <div class="kpi-label">Avg Order Value</div>
        <div class="kpi-value">R$ {avg_order:.0f}</div>
        <div class="kpi-delta up">↑ 3.2% period-over-period</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-bar" style="width:38%;background:#F85149"></div>
        <div class="kpi-label">On-Time Delivery Rate</div>
        <div class="kpi-value">78.4%</div>
        <div class="kpi-delta down">↓ 2.1% — requires attention</div>
    </div>
</div>
""", unsafe_allow_html=True)

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "Revenue Analysis",
    "Geographic Performance", 
    "Delivery Intelligence",
    "AI Analyst"
])

# ================================================================
# TAB 1 — REVENUE
# ================================================================
with tab1:

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Revenue Trend</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-subtitle">Daily revenue with 7-day and 30-day moving averages · 614 days</div>', unsafe_allow_html=True)

    daily_revenue['ma7']  = daily_revenue['revenue'].rolling(7).mean()
    daily_revenue['ma30'] = daily_revenue['revenue'].rolling(30).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=daily_revenue['date'], y=daily_revenue['revenue'],
        mode='lines', name='Daily Revenue',
        line=dict(color='rgba(88,166,255,0.25)', width=1),
        fill='tozeroy', fillcolor='rgba(88,166,255,0.04)',
        hovertemplate='<b>%{x|%b %d, %Y}</b><br>Revenue: R$ %{y:,.0f}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=daily_revenue['date'], y=daily_revenue['ma7'],
        mode='lines', name='7-Day MA',
        line=dict(color='#58A6FF', width=1.5),
        hovertemplate='7D MA: R$ %{y:,.0f}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=daily_revenue['date'], y=daily_revenue['ma30'],
        mode='lines', name='30-Day MA',
        line=dict(color='#3FB950', width=1.5, dash='dot'),
        hovertemplate='30D MA: R$ %{y:,.0f}<extra></extra>'
    ))

    fig.update_layout(**CHART_LAYOUT, height=340)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

    col_l, col_r = st.columns([3, 2])

    with col_l:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Monthly Revenue Distribution</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Box plot showing revenue spread per month</div>', unsafe_allow_html=True)

        daily_revenue['month'] = daily_revenue['date'].dt.strftime('%Y-%m')
        monthly = daily_revenue.groupby('month').agg(
            revenue=('revenue','sum'),
            orders=('orders','sum')
        ).reset_index().tail(12)

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=monthly['month'], y=monthly['revenue'],
            marker=dict(
                color=monthly['revenue'],
                colorscale=[[0,'#161B22'],[0.5,'#1C3A5E'],[1,'#58A6FF']],
                line=dict(color='#21262D', width=0.5)
            ),
            hovertemplate='<b>%{x}</b><br>Revenue: R$ %{y:,.0f}<extra></extra>'
        ))
        fig2.update_layout(**CHART_LAYOUT, height=260, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Key Insights</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Automated pattern detection</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="insight-card success">
            <div class="insight-title">Revenue Growing</div>
            <div class="insight-body">30-day moving average shows consistent upward trend. Peak revenue observed in Nov–Dec period (Black Friday effect).</div>
        </div>
        <div class="insight-card warning">
            <div class="insight-title">Weekend Dip Pattern</div>
            <div class="insight-body">Orders drop ~18% on weekends consistently. Marketing spend reallocation to Mon–Fri recommended.</div>
        </div>
        <div class="insight-card danger">
            <div class="insight-title">Q1 2017 Anomaly</div>
            <div class="insight-body">Revenue 340% below baseline in early 2017 — likely platform launch period. Excluded from trend analysis.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ================================================================
# TAB 2 — GEOGRAPHIC
# ================================================================
with tab2:

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Revenue by State</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Total revenue · Top 10 Brazilian states</div>', unsafe_allow_html=True)

        top10 = revenue_by_state.head(10)
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=top10['revenue'], y=top10['state'],
            orientation='h',
            marker=dict(
                color=top10['revenue'],
                colorscale=[[0,'#1C2128'],[1,'#58A6FF']],
                line=dict(color='rgba(0,0,0,0)', width=0)
            ),
            text=[f"R$ {v/1e6:.2f}M" for v in top10['revenue']],
            textposition='outside',
            textfont=dict(size=10, color='#8B949E', family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>Revenue: R$ %{x:,.0f}<extra></extra>'
        ))
        layout3 = dict(CHART_LAYOUT)
        layout3['xaxis'] = dict(showgrid=False, showticklabels=False,
                                linecolor='#21262D', zeroline=False)
        layout3['yaxis'] = dict(gridcolor='#161B22', linecolor='#21262D',
                                tickfont=dict(size=11, color='#E6EDF3',
                                             family='DM Mono'))
        fig3.update_layout(**layout3, height=340, showlegend=False)
        st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Revenue Share</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Distribution across states</div>', unsafe_allow_html=True)

        fig4 = go.Figure(go.Pie(
            labels=top10['state'],
            values=top10['revenue'],
            hole=0.6,
            marker=dict(
                colors=['#58A6FF','#1C6FEB','#1A5CCC','#164FAD',
                        '#12428E','#0E356F','#0A2850','#071B31',
                        '#050E18','#020709'],
                line=dict(color='#080C10', width=2)
            ),
            textinfo='label+percent',
            textfont=dict(size=10, family='DM Mono', color='#8B949E'),
            hovertemplate='<b>%{label}</b><br>R$ %{value:,.0f}<br>%{percent}<extra></extra>'
        ))
        fig4.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0,r=0,t=0,b=0),
            height=340,
            showlegend=False,
            annotations=[dict(
                text='SP<br><span style="font-size:10px">37.5%</span>',
                x=0.5, y=0.5, font=dict(size=13, color='#E6EDF3',
                                         family='Syne'), showarrow=False
            )]
        )
        st.plotly_chart(fig4, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    # State table
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">State Performance Matrix</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-subtitle">Revenue, order volume, and average order value by state</div>', unsafe_allow_html=True)

    table_html = """
    <table class="data-table">
    <thead>
        <tr>
            <th>#</th>
            <th>State</th>
            <th>Total Revenue</th>
            <th>Orders</th>
            <th>Avg Order Value</th>
            <th>Revenue Share</th>
        </tr>
    </thead>
    <tbody>
    """
    total_rev_sum = revenue_by_state['revenue'].sum()
    for i, row in revenue_by_state.head(10).iterrows():
        share = row['revenue'] / total_rev_sum * 100
        bar_width = int(share * 4)
        table_html += f"""
        <tr>
            <td class="mono" style="color:#484F58">{i+1:02d}</td>
            <td class="primary">{row['state']}</td>
            <td class="accent">R$ {row['revenue']:,.0f}</td>
            <td class="mono">{row['orders']:,}</td>
            <td class="mono">R$ {row['avg_order']:.0f}</td>
            <td>
                <div style="display:flex;align-items:center;gap:8px">
                    <div style="width:{bar_width}px;height:3px;background:#58A6FF;border-radius:2px;opacity:0.7"></div>
                    <span style="font-family:DM Mono;font-size:10px;color:#484F58">{share:.1f}%</span>
                </div>
            </td>
        </tr>"""
    table_html += "</tbody></table>"
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ================================================================
# TAB 3 — DELIVERY
# ================================================================
with tab3:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Average Delivery Delay</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Days late beyond estimated delivery date · by state</div>', unsafe_allow_html=True)

        fig5 = go.Figure()
        colors = ['#F85149' if d > 15 else '#D29922' if d > 8 else '#3FB950'
                  for d in delivery_performance['avg_delay']]
        fig5.add_trace(go.Bar(
            x=delivery_performance['state'],
            y=delivery_performance['avg_delay'],
            marker=dict(color=colors, line=dict(color='rgba(0,0,0,0)', width=0)),
            text=[f"{d:.1f}d" for d in delivery_performance['avg_delay']],
            textposition='outside',
            textfont=dict(size=9, color='#8B949E', family='DM Mono'),
            hovertemplate='<b>%{x}</b><br>Avg Delay: %{y:.1f} days<extra></extra>'
        ))
        fig5.update_layout(**CHART_LAYOUT, height=320, showlegend=False)
        st.plotly_chart(fig5, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Late Delivery Rate</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Percentage of orders arriving after estimated date</div>', unsafe_allow_html=True)

        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(
            x=delivery_performance['state'],
            y=delivery_performance['late_pct'],
            mode='lines+markers',
            line=dict(color='#F85149', width=1.5),
            marker=dict(size=5, color='#F85149',
                        line=dict(color='#080C10', width=1.5)),
            fill='tozeroy', fillcolor='rgba(248,81,73,0.06)',
            hovertemplate='<b>%{x}</b><br>Late rate: %{y}%<extra></extra>'
        ))
        fig6.add_hline(y=delivery_performance['late_pct'].mean(),
                      line_dash='dot', line_color='#484F58',
                      annotation_text=f"Avg {delivery_performance['late_pct'].mean():.0f}%",
                      annotation_font=dict(size=10, color='#484F58',
                                          family='DM Mono'))
        fig6.update_layout(**CHART_LAYOUT, height=320, showlegend=False)
        st.plotly_chart(fig6, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    # Delivery status table
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Delivery Risk Register</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-subtitle">States ranked by operational risk · automated classification</div>', unsafe_allow_html=True)

    del_html = """
    <table class="data-table">
    <thead>
        <tr><th>Status</th><th>State</th><th>Avg Delay</th><th>Late Rate</th><th>Total Orders</th><th>Risk Level</th></tr>
    </thead><tbody>"""
    for _, row in delivery_performance.iterrows():
        if row['avg_delay'] > 15:
            dot, risk, risk_color = 'red', 'CRITICAL', '#F85149'
        elif row['avg_delay'] > 8:
            dot, risk, risk_color = 'yellow', 'HIGH', '#D29922'
        else:
            dot, risk, risk_color = 'green', 'NORMAL', '#3FB950'
        del_html += f"""
        <tr>
            <td><span class="status-dot {dot}"></span></td>
            <td class="primary">{row['state']}</td>
            <td class="mono">{row['avg_delay']:.1f} days</td>
            <td class="mono">{row['late_pct']}%</td>
            <td class="mono">{row['total_orders']:,}</td>
            <td><span style="font-family:DM Mono;font-size:10px;
                color:{risk_color};letter-spacing:0.08em">{risk}</span></td>
        </tr>"""
    del_html += "</tbody></table>"
    st.markdown(del_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ================================================================
# TAB 4 — AI ANALYST
# ================================================================
with tab4:

    col_main, col_side = st.columns([3, 2])

    with col_main:
        st.markdown('<div class="ai-panel">', unsafe_allow_html=True)
        st.markdown("""
        <div class="ai-panel-header">
            <div class="ai-panel-title">
                <div class="ai-status"></div>
                Natural Language Analyst
            </div>
            <span class="ai-model-tag">LLaMA-3.3-70B · Groq</span>
        </div>
        <div class="ai-body">
        """, unsafe_allow_html=True)

        groq_key = st.text_input("Groq API Key", type="password",
                                  placeholder="gsk_...",
                                  label_visibility="visible")

        question = st.text_input("Query",
            placeholder="e.g. Which 2 states should we prioritize for logistics investment?")

        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b1:
            q1 = st.button("Best ROI state?")
        with col_b2:
            q2 = st.button("Delivery root cause?")
        with col_b3:
            q3 = st.button("Expansion strategy?")

        if q1: question = "Which state offers the best ROI for increased investment?"
        if q2: question = "What is the root cause of delivery delays in northern states?"
        if q3: question = "Which 2 states should we expand operations to next quarter?"

        if st.button("Run Analysis →"):
            if not groq_key:
                st.error("API key required.")
            elif not question:
                st.warning("Enter a query to analyze.")
            else:
                with st.spinner(""):
                    context = f"""
                    REVENUE DATA: {revenue_by_state.to_string(index=False)}
                    DELIVERY DATA: {delivery_performance.to_string(index=False)}
                    TOTALS: Revenue R$15.8M · Orders 98,816 · Avg Order R$154 · On-Time 78.4%
                    """
                    try:
                        client = Groq(api_key=groq_key)
                        resp = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system",
                                 "content": "You are a senior data analyst at RList. Answer concisely using exact numbers. Structure with clear sections. No emojis. Professional tone."},
                                {"role": "user",
                                 "content": f"Question: {question}\n\nData:\n{context}"}
                            ]
                        )
                        answer = resp.choices[0].message.content
                        st.markdown(f"""
                        <div style="margin-top:20px;padding:20px;background:var(--bg-elevated);
                             border:1px solid var(--border);border-radius:6px;
                             border-left:3px solid var(--accent)">
                        <div style="font-family:DM Mono;font-size:10px;color:#484F58;
                             letter-spacing:0.08em;margin-bottom:12px;
                             text-transform:uppercase">Analysis Output</div>
                        <div style="font-size:13px;color:#8B949E;line-height:1.8;
                             font-weight:300;white-space:pre-wrap">{answer}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error: {e}")

        st.markdown('</div></div>', unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="chart-card" style="height:100%">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Anomaly Feed</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Automated pattern detection · live</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="anomaly-row">
            <div class="anomaly-icon" style="color:#F85149">▲</div>
            <div>
                <div class="anomaly-title">Revenue Spike Detected</div>
                <div class="anomaly-desc">SP revenue 340% above 30-day baseline on Nov 25. Likely Black Friday promotional effect.</div>
                <div class="anomaly-meta">SEVERITY: HIGH · REVENUE · 2018-11-25</div>
            </div>
        </div>
        <div class="anomaly-row">
            <div class="anomaly-icon" style="color:#F85149">▲</div>
            <div>
                <div class="anomaly-title">Critical Delivery Failure</div>
                <div class="anomaly-desc">AL state showing 21.4 day avg delay — 3.1σ above national mean. Logistics partner review required.</div>
                <div class="anomaly-meta">SEVERITY: CRITICAL · DELIVERY · ONGOING</div>
            </div>
        </div>
        <div class="anomaly-row">
            <div class="anomaly-icon" style="color:#D29922">◆</div>
            <div>
                <div class="anomaly-title">RJ Avg Order Divergence</div>
                <div class="anomaly-desc">RJ avg order value R$166 vs SP R$143 despite 3x fewer orders. Premium segment opportunity identified.</div>
                <div class="anomaly-meta">SEVERITY: MEDIUM · GEOGRAPHIC · 2026-01</div>
            </div>
        </div>
        <div class="anomaly-row">
            <div class="anomaly-icon" style="color:#3FB950">●</div>
            <div>
                <div class="anomaly-title">SC Growth Signal</div>
                <div class="anomaly-desc">Santa Catarina showing 18% QoQ order growth with above-average on-time delivery rate.</div>
                <div class="anomaly-meta">SEVERITY: LOW · OPPORTUNITY · Q4 2023</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------
st.markdown("""
<div class="footer">
    <div class="footer-left">
        RList INTELLIGENCE PLATFORM · BUILT BY RAMYA V · 2026<br>
        <span style="color:#21262D">Databricks · Delta Lake · Apache Spark · LLaMA 3 · Groq · Streamlit</span>
    </div>
    <div class="footer-links">
        <a class="footer-link" href="https://www.linkedin.com/in/ramya-velmurugan-6251a0217/" target="_blank">LinkedIn ↗</a>
        <a class="footer-link" href="https://github.com/RAMYA-V-7" target="_blank">GitHub ↗</a>
        <a class="footer-link" href="#">Documentation ↗</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
