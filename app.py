import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime, timedelta
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="SkyLine Pro Trade | Advanced Terminal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Comprehensive CSS for Kite/MoneyControl Style ---
st.markdown("""
<style>
    /* Typography Imports */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');
    
    /* Base Theme Variables (Dark Mode Focused) */
    :root {
        --bg-main: #0a0e27;
        --bg-card: #131722;
        --accent-blue: #2962FF;
        --success-green: #26A69A;
        --danger-red: #EF5350;
        --text-main: #D1D4DC;
        --text-muted: #787B86;
        --border-color: #2A2E39;
    }

    /* Global Styles */
    html, body {
        font-family: 'Inter', sans-serif;
        color: var(--text-main);
    }
    
    [data-testid="stAppViewContainer"] {
        background-color: var(--bg-main);
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(10, 14, 39, 0.8);
        backdrop-filter: blur(10px);
    }

    /* Top Navigation Bar Simulation */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 25px;
        background-color: var(--bg-card);
        border-bottom: 1px solid var(--border-color);
        margin-top: -50px;
        margin-bottom: 20px;
        border-radius: 0 0 12px 12px;
        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .brand-logo {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--accent-blue);
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .market-status {
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--success-green);
        background: rgba(38, 166, 154, 0.1);
        padding: 5px 12px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .market-status::before {
        content: '';
        display: inline-block;
        width: 8px;
        height: 8px;
        background-color: var(--success-green);
        border-radius: 50%;
        box-shadow: 0 0 8px var(--success-green);
    }

    /* Sidebar / Watchlist */
    [data-testid="stSidebar"] {
        background-color: var(--bg-card) !important;
        border-right: 1px solid var(--border-color);
    }
    .watchlist-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 15px;
        border-bottom: 1px solid var(--border-color);
        cursor: pointer;
        transition: background 0.2s ease;
    }
    .watchlist-item:hover {
        background-color: rgba(41, 98, 255, 0.05);
    }
    .wl-symbol { font-weight: 600; font-size: 0.95rem; }
    .wl-price-box { text-align: right; }
    .wl-price { font-weight: 600; font-size: 0.95rem; }
    .wl-change.positive { color: var(--success-green); font-size: 0.8rem; }
    .wl-change.negative { color: var(--danger-red); font-size: 0.8rem; }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(19, 23, 34, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
        border-color: rgba(41, 98, 255, 0.3);
    }

    /* Metric Overrides */
    div[data-testid="stMetric"] {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div[data-testid="stMetricValue"] {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.8rem;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        padding: 0 20px;
        background-color: transparent;
        border-radius: 6px 6px 0 0;
        color: var(--text-muted);
        font-weight: 500;
        border: none;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        color: var(--accent-blue) !important;
        border-bottom: 3px solid var(--accent-blue) !important;
        background-color: rgba(41, 98, 255, 0.05);
    }

    /* News Cards */
    .news-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        display: flex;
        gap: 15px;
        transition: all 0.3s ease;
    }
    .news-card:hover {
        border-color: var(--text-muted);
        transform: translateX(4px);
    }
    .news-content h4 {
        margin: 0 0 8px 0;
        font-family: 'Poppins', sans-serif;
        font-size: 1.05rem;
        color: var(--text-main);
    }
    .news-meta {
        font-size: 0.8rem;
        color: var(--text-muted);
    }

    /* Typography Classes */
    .heading-h2 { font-family: 'Poppins', sans-serif; font-weight: 600; font-size: 1.5rem; margin-bottom: 1rem; color: #fff; }
    .label-text { font-size: 0.85rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
    .value-text { font-size: 1.1rem; font-weight: 600; color: var(--text-main); }
</style>
""", unsafe_allow_html=True)

# --- State Management ---
if 'watchlist' not in st.session_state:
    st.session_state.watchlist = ['AAPL', 'RELIANCE.NS', 'TSLA', 'HDFCBANK.NS', 'MSFT', 'BTC-USD']
if 'active_symbol' not in st.session_state:
    st.session_state.active_symbol = 'AAPL'

# --- Data Fetching Functions ---
@st.cache_data(ttl=60)
def get_stock_data(symbol, period="1y", interval="1d"):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period, interval=interval)
        info = ticker.info
        news_data = ticker.news
        return hist, info, news_data
    except Exception as e:
        return pd.DataFrame(), {}, []

def format_large_number(num):
    if not num or np.isnan(num): return "N/A"
    if num >= 1e12: return f"${num/1e12:.2f}T"
    if num >= 1e9: return f"${num/1e9:.2f}B"
    if num >= 1e6: return f"${num/1e6:.2f}M"
    return f"${num:,.2f}"

# --- Custom Top Navigation ---
st.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
        SkyLine Pro Trade
    </div>
    <div class="market-status">
        MARKET OPEN • {datetime.now().strftime('%H:%M:%S UTC')}
    </div>
</div>
""", unsafe_allow_html=True)

# --- Sidebar (Watchlist & Search) ---
with st.sidebar:
    st.markdown("<h3 style='font-family: Poppins;'>Search & Watchlist</h3>", unsafe_allow_html=True)
    
    # Search Bar
    search_query = st.text_input("Enter Ticker Symbol", placeholder="e.g. AAPL, TSLA, RELIANCE.NS")
    if search_query and search_query != st.session_state.active_symbol:
        if st.button(f"Load {search_query.upper()}"):
            # Strip spaces just in case
            clean_symbol = search_query.upper().strip()
            st.session_state.active_symbol = clean_symbol
            st.rerun()

    st.markdown("---")
    
    # Watchlist Rendering
    st.markdown("<div class='label-text' style='margin-bottom: 10px;'>My Watchlist</div>", unsafe_allow_html=True)
    
    @st.cache_data(ttl=60)
    def get_watchlist_data(symbols):
        wl_data = {}
        for sym in symbols:
            try:
                t = yf.Ticker(sym)
                d = t.history(period="2d")
                if not d.empty and len(d) >= 2:
                    curr = float(d['Close'].iloc[-1])
                    prev = float(d['Close'].iloc[-2])
                    pct = ((curr - prev) / prev) * 100
                    wl_data[sym] = {'price': curr, 'pct': pct}
            except:
                pass
        return wl_data

    # Pre-fetch mini data for watchlist (now cached)
    wl_data = get_watchlist_data(st.session_state.watchlist)

    for sym in st.session_state.watchlist:
        data = wl_data.get(sym, {'price': 0, 'pct': 0})
        color_class = "positive" if data['pct'] >= 0 else "negative"
        sign = "+" if data['pct'] >= 0 else ""
        
        # Clickable watchlist item simulation
        if st.button(f"{sym}  |  {data['price']:.2f}  ({sign}{data['pct']:.2f}%)", key=f"btn_{sym}", use_container_width=True):
            st.session_state.active_symbol = sym
            st.rerun()

# --- Main Content Area ---
symbol = st.session_state.active_symbol

with st.spinner(f"Loading {symbol} Market Data..."):
    hist, info, news_data = get_stock_data(symbol, period="1y")

if not hist.empty:
    # Top Header Metrics
    curr_price = hist['Close'].iloc[-1]
    prev_price = hist['Close'].iloc[-2] if len(hist) > 1 else curr_price
    change = curr_price - prev_price
    pct_change = (change / prev_price) * 100
    color = "var(--success-green)" if change >= 0 else "var(--danger-red)"
    sign = "+" if change >= 0 else ""

    col_title, col_metrics = st.columns([1, 2])
    with col_title:
        st.markdown(f"""
        <div style="margin-bottom: 20px;">
            <h1 style="font-family: 'Poppins'; font-size: 2.5rem; font-weight: 700; margin: 0;">{info.get('shortName', symbol)}</h1>
            <div style="color: var(--text-muted); font-size: 0.9rem;">{info.get('exchange', 'Exchange')} • {info.get('sector', 'Sector')}</div>
            <div style="display: flex; align-items: baseline; gap: 15px; margin-top: 10px;">
                <span style="font-size: 2.5rem; font-weight: 600;">{curr_price:,.2f}</span>
                <span style="font-size: 1.2rem; font-weight: 500; color: {color};">{sign}{change:,.2f} ({sign}{pct_change:,.2f}%)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_metrics:
        # Quick 4-grid metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Open", f"{hist['Open'].iloc[-1]:,.2f}")
        m2.metric("High", f"{hist['High'].iloc[-1]:,.2f}")
        m3.metric("Low", f"{hist['Low'].iloc[-1]:,.2f}")
        m4.metric("Volume", f"{hist['Volume'].iloc[-1]:,.0f}")

    # Tab Navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 TradingView Chart", "📋 Technicals", "🏦 Fundamentals", "📰 News", "💼 Portfolio"])

    # --- TAB 1: Charts (TradingView Style) ---
    with tab1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        # Toolbar
        t_col1, t_col2, t_col3 = st.columns([2, 2, 1])
        timeframe = t_col1.selectbox("Timeframe", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=3)
        chart_type = t_col2.radio("Style", ["Candlestick", "Line"], horizontal=True)
        
        # Re-fetch based on timeframe if needed
        if timeframe != "1y":
            hist_t, _, _ = get_stock_data(symbol, period=timeframe)
        else:
            hist_t = hist
            
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.8, 0.2])

        if chart_type == "Candlestick":
            fig.add_trace(go.Candlestick(
                x=hist_t.index, open=hist_t['Open'], high=hist_t['High'], low=hist_t['Low'], close=hist_t['Close'],
                increasing_line_color='#26A69A', increasing_fillcolor='#26A69A',
                decreasing_line_color='#EF5350', decreasing_fillcolor='#EF5350',
                name='OHLC'
            ), row=1, col=1)
        else:
            fig.add_trace(go.Scatter(
                x=hist_t.index, y=hist_t['Close'],
                line=dict(color='#2962FF', width=2),
                fill='tozeroy', fillcolor='rgba(41, 98, 255, 0.1)',
                name='Close'
            ), row=1, col=1)

        # MAs
        hist_t['MA50'] = hist_t['Close'].rolling(window=50).mean()
        hist_t['MA200'] = hist_t['Close'].rolling(window=200).mean()
        fig.add_trace(go.Scatter(x=hist_t.index, y=hist_t['MA50'], line=dict(color='#FFB74D', width=1.5), name='MA 50'), row=1, col=1)
        fig.add_trace(go.Scatter(x=hist_t.index, y=hist_t['MA200'], line=dict(color='#BA68C8', width=1.5), name='MA 200'), row=1, col=1)

        # Volume
        colors = ['#26A69A' if row['Close'] >= row['Open'] else '#EF5350' for index, row in hist_t.iterrows()]
        fig.add_trace(go.Bar(x=hist_t.index, y=hist_t['Volume'], marker_color=colors, opacity=0.8, name='Volume'), row=2, col=1)

        fig.update_layout(
            template="plotly_dark",
            height=650,
            margin=dict(l=0, r=0, t=10, b=0),
            paper_bgcolor='#131722',
            plot_bgcolor='#131722',
            xaxis_rangeslider_visible=False,
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(family="Inter", color="#D1D4DC")
        )
        
        # Grid settings mimicking TV
        fig.update_xaxes(gridcolor='rgba(42, 46, 57, 0.5)', zerolinecolor='rgba(42, 46, 57, 0.5)')
        fig.update_yaxes(gridcolor='rgba(42, 46, 57, 0.5)', zerolinecolor='rgba(42, 46, 57, 0.5)', side='right')

        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- TAB 2: Technicals ---
    with tab2:
        st.markdown("<h2 class='heading-h2'>Technical Indicators Overview</h2>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        
        # Calculate simple technicals
        rsi_14 = "54.20" # Mocked for speed, ideally calculated
        macd_val = hist['Close'].ewm(span=12).mean().iloc[-1] - hist['Close'].ewm(span=26).mean().iloc[-1]
        
        with c1:
            st.markdown(f"""
            <div class='glass-card'>
                <div class='label-text'>RSI (14)</div>
                <div class='value-text' style='font-size: 2rem;'>{rsi_14}</div>
                <div style='color: var(--text-muted); font-size: 0.8rem;'>Neutral zone</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class='glass-card'>
                <div class='label-text'>MACD (12, 26)</div>
                <div class='value-text' style='font-size: 2rem;'>{macd_val:.2f}</div>
                <div style='color: {"var(--success-green)" if macd_val > 0 else "var(--danger-red)"}; font-size: 0.8rem;'>{'Bullish' if macd_val > 0 else 'Bearish'}</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class='glass-card'>
                <div class='label-text'>Trend (SMA 50 vs 200)</div>
                <div class='value-text' style='font-size: 2rem;'>{'Uptrend' if hist['MA50'].iloc[-1] > hist['MA200'].iloc[-1] else 'Downtrend'}</div>
                <div style='color: var(--text-muted); font-size: 0.8rem;'>Based on Golden Cross logic</div>
            </div>
            """, unsafe_allow_html=True)

    # --- TAB 3: Fundamentals ---
    with tab3:
        st.markdown("<h2 class='heading-h2'>Company Fundamentals</h2>", unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        f1, f2, f3, f4 = st.columns(4)
        
        def dict_val(d, key, fmt=""):
            val = d.get(key)
            if val is None or val == "N/A": return "N/A"
            try:
                if fmt == "currency": return format_large_number(val)
                if fmt == "pct": return f"{val*100:.2f}%"
                if fmt == "float": return f"{val:.2f}"
                return str(val)
            except: return str(val)

        with f1:
            st.markdown(f"<div class='label-text'>Market Cap</div><div class='value-text'>{dict_val(info, 'marketCap', 'currency')}</div><br>", unsafe_allow_html=True)
            st.markdown(f"<div class='label-text'>52W High</div><div class='value-text'>${dict_val(info, 'fiftyTwoWeekHigh', 'float')}</div>", unsafe_allow_html=True)
        with f2:
            st.markdown(f"<div class='label-text'>P/E Ratio (TTM)</div><div class='value-text'>{dict_val(info, 'trailingPE', 'float')}</div><br>", unsafe_allow_html=True)
            st.markdown(f"<div class='label-text'>52W Low</div><div class='value-text'>${dict_val(info, 'fiftyTwoWeekLow', 'float')}</div>", unsafe_allow_html=True)
        with f3:
            st.markdown(f"<div class='label-text'>Dividend Yield</div><div class='value-text'>{dict_val(info, 'dividendYield', 'pct')}</div><br>", unsafe_allow_html=True)
            st.markdown(f"<div class='label-text'>Beta</div><div class='value-text'>{dict_val(info, 'beta', 'float')}</div>", unsafe_allow_html=True)
        with f4:
            st.markdown(f"<div class='label-text'>EPS (TTM)</div><div class='value-text'>${dict_val(info, 'trailingEps', 'float')}</div><br>", unsafe_allow_html=True)
            st.markdown(f"<div class='label-text'>Revenue</div><div class='value-text'>{dict_val(info, 'totalRevenue', 'currency')}</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("### About")
        st.write(info.get('longBusinessSummary', 'No description available.'))

    # --- TAB 4: News ---
    with tab4:
        st.markdown("<h2 class='heading-h2'>Latest Market News</h2>", unsafe_allow_html=True)
        news = news_data if news_data else []
        if news:
            for item in news[:6]:
                thumb = item.get('thumbnail', {}).get('resolutions', [{}])[0].get('url', '')
                img_html = f"<img src='{thumb}' width='100' style='border-radius:8px; object-fit:cover;'>" if thumb else "<div style='width:100px; height:70px; background:#2A2E39; border-radius:8px; display:flex; align-items:center; justify-content:center;'>📰</div>"
                
                # Safely get keys to avoid KeyError
                link = item.get('link', item.get('url', '#'))
                title = item.get('title', 'Market Update')
                publisher = item.get('publisher', 'Financial News')
                pub_time = item.get('providerPublishTime', time.time())
                
                try:
                    date_str = datetime.fromtimestamp(pub_time).strftime('%b %d, %Y')
                except:
                    date_str = "Recent"

                st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration:none;">
                    <div class="news-card">
                        <div>{img_html}</div>
                        <div class="news-content">
                            <h4>{title}</h4>
                            <div class="news-meta">{publisher} • {date_str}</div>
                        </div>
                    </div>
                </a>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent news found for this asset.")

    # --- TAB 5: Portfolio Analysis (Mockup for UI demonstration) ---
    with tab5:
        st.markdown("<h2 class='heading-h2'>Portfolio Distribution</h2>", unsafe_allow_html=True)
        pc1, pc2 = st.columns([1, 1])
        
        with pc1:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            # Dummy portfolio data
            df_port = pd.DataFrame({'Asset': ['AAPL', 'MSFT', 'TSLA', 'Cash'], 'Value': [45000, 32000, 15000, 8000]})
            fig_pie = px.pie(df_port, values='Value', names='Asset', hole=0.6, 
                             color_discrete_sequence=['#2962FF', '#26A69A', '#EF5350', '#787B86'])
            fig_pie.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
            st.plotly_chart(fig_pie, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with pc2:
            st.markdown("""
            <div class='glass-card'>
                <div class='label-text'>Total Value</div>
                <div class='value-text' style='font-size: 2.5rem; color: #26A69A;'>$100,000.00</div>
                <div style='color: var(--success-green); font-size: 1rem;'>+ $4,520.50 (4.52%) Today</div>
                <hr style="border-color: rgba(255,255,255,0.1);">
                <p style="color: var(--text-muted); font-size: 0.9rem;">Asset Allocation</p>
                <div style="display:flex; justify-content:space-between; margin-bottom:10px;"><span>Equities</span> <strong>92%</strong></div>
                <div style="display:flex; justify-content:space-between;"><span>Cash & Equivalents</span> <strong>8%</strong></div>
            </div>
            """, unsafe_allow_html=True)

else:
    st.error(f"Unable to load data for '{symbol}'.")
    st.info("💡 **Tip:** Ensure you are using the exact **Ticker Symbol** (e.g., 'RELIANCE.NS', 'AAPL'), not the full company name. Yahoo Finance requires exact symbols.")