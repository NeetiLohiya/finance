# 📈 StockVista - Professional Stock Market Dashboard

<div align="center">

![StockVista Logo](https://img.shields.io/badge/StockVista-Professional%20Trading%20Platform-2962FF?style=for-the-badge&logo=yahoo&logoColor=white)

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**A premium stock market analysis platform with real-time data, technical indicators, and multi-user authentication**

[Live Demo](#) • [Features](#-features) • [Installation](#-installation) • [Documentation](#-documentation)

</div>

---

## 🌟 Features

### 📊 **Real-Time Market Data**
- Live stock prices, volume, and market statistics
- Support for stocks, indices, forex, and cryptocurrencies
- Historical data analysis with customizable date ranges
- Major market indices tracking (S&P 500, NASDAQ, DOW)

### 📈 **Advanced Charting**
- Interactive candlestick charts with OHLC data
- Multiple chart types: Candlestick, Line, Area, Heikin Ashi
- Volume analysis with color-coded bars
- Timeframe options: 1D, 5D, 1M, 3M, 6M, 1Y, 5Y, Max
- Zoom, pan, and full-screen capabilities

### 🔧 **Technical Analysis**
- **Moving Averages**: 50-day and 200-day MA
- **RSI**: Relative Strength Index with overbought/oversold zones
- **MACD**: Moving Average Convergence Divergence
- **Bollinger Bands**: Volatility indicators
- Custom indicator combinations

### 💼 **Portfolio Management**
- Personal portfolio tracker
- Real-time P&L calculations
- Holdings distribution visualization
- Performance analytics
- Export portfolio data to CSV

### 🔍 **Stock Screening & Comparison**
- Multi-stock comparison charts
- Advanced filters (price, volume, market cap, sector)
- Correlation heatmaps
- Normalized performance tracking
- Sector performance analysis

### 📰 **Market News & Insights**
- Latest stock-specific news
- Market sentiment analysis
- News integration from multiple sources
- Trending stocks section

### 🔐 **Multi-User Authentication**
- **Google OAuth 2.0** integration
- Traditional email/password signup/login
- Secure session management with JWT
- Password encryption using bcrypt
- Email verification
- Password reset functionality
- Personalized user profiles

### 🎨 **Premium UI/UX**
- **Dark/Light theme** toggle
- Professional trading platform design inspired by Zerodha Kite
- Glassmorphism effects
- Responsive design (mobile, tablet, desktop)
- Smooth animations and transitions
- Custom styled components
- Interactive tooltips and notifications

### 🎮 **Easter Eggs**
- Anti-gravity mode (type "antigravity" in search)
- Barrel roll effect (type "do a barrel roll")
- Fun surprises for users!

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Cloud account (for OAuth - optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/stockvista.git
cd stockvista
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```env
# Google OAuth (Optional - for Google Sign-In)
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here

# JWT Secret Key
JWT_SECRET_KEY=your_random_secret_key_here

# Database
DATABASE_URL=sqlite:///database/users.db

# News API (Optional)
NEWS_API_KEY=your_news_api_key_here

# Email Configuration (Optional - for verification)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

5. **Initialize the database**
```bash
python database.py
```

6. **Run the application**
```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📦 Project Structure

```
stockvista/
│
├── main.py                 # Main Streamlit application
├── auth.py                 # Authentication logic
├── database.py             # Database operations
├── models.py               # Data models
├── utils.py                # Helper functions
├── config.py               # Configuration settings
│
├── components/
│   ├── charts.py          # Chart components
│   ├── indicators.py      # Technical indicators
│   ├── portfolio.py       # Portfolio management
│   ├── news.py            # News integration
│   └── ui_elements.py     # Reusable UI components
│
├── assets/
│   ├── styles.css         # Custom CSS
│   ├── logo.png           # App logo
│   └── images/            # UI images
│
├── database/
│   └── users.db           # SQLite database
│
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License

```

---

## 🔑 Google OAuth Setup (Optional)

To enable Google Sign-In:

1. **Go to [Google Cloud Console](https://console.cloud.google.com/)**

2. **Create a new project** or select existing

3. **Enable Google+ API**
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google+ API"
   - Click "Enable"

4. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Application type: "Web application"
   - Add authorized redirect URIs:
     - `http://localhost:8501`
     - `https://yourdomain.com` (for production)

5. **Copy Client ID and Secret** to `.env` file

---

## 📚 Dependencies

```
streamlit>=1.28.0
yfinance>=0.2.28
plotly>=5.17.0
pandas>=2.0.0
numpy>=1.24.0
bcrypt>=4.0.1
PyJWT>=2.8.0
python-dotenv>=1.0.0
streamlit-google-auth>=0.2.0
streamlit-cookies-manager>=0.2.0
requests>=2.31.0
Pillow>=10.0.0
ta>=0.11.0
newsapi-python>=0.2.7
```

---

## 🎯 Usage

### 1. **Authentication**
- Click "Sign In with Google" or use email/password
- New users can register via the Sign Up tab
- Email verification link sent upon registration

### 2. **Dashboard**
- Search stocks using the search bar (e.g., AAPL, GOOGL, TSLA)
- View real-time prices and statistics
- Analyze charts with multiple timeframes

### 3. **Technical Analysis**
- Navigate to "Technicals" tab
- Add indicators from the dropdown
- Customize indicator parameters

### 4. **Portfolio**
- Add stocks to your portfolio
- Input purchase price and quantity
- Track real-time P&L

### 5. **Watchlist**
- Click ⭐ to add stocks to watchlist
- View all watchlist items in sidebar
- Quick access to favorite stocks

### 6. **Stock Comparison**
- Select multiple stocks from comparison tool
- View normalized performance
- Analyze correlations

---

## 🛠️ Configuration

### Theme Customization

Edit `assets/styles.css` to customize colors:

```css
:root {
  --primary-color: #2962FF;
  --success-color: #26A69A;
  --danger-color: #EF5350;
  --background-dark: #0a0e27;
  --card-dark: #131722;
}
```

### Default Settings

Edit `config.py`:

```python
DEFAULT_STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
SESSION_TIMEOUT = 1800  # 30 minutes
MAX_WATCHLIST_ITEMS = 20
CHART_HEIGHT = 600
```

---

## 🔒 Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT token-based authentication
- ✅ SQL injection prevention with parameterized queries
- ✅ CSRF protection
- ✅ Rate limiting on login attempts
- ✅ Session timeout
- ✅ Secure cookie handling
- ✅ Input validation and sanitization

---

## 🌐 Deployment

### Streamlit Community Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add secrets in Streamlit Cloud dashboard
5. Deploy!

### Heroku

```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
heroku config:set GOOGLE_CLIENT_ID=your_id
heroku open
```

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

```bash
docker build -t stockvista .
docker run -p 8501:8501 stockvista
```

---

## 📊 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Technical Analysis
![Technical Analysis](screenshots/technical.png)

### Portfolio
![Portfolio](screenshots/portfolio.png)

### Authentication
![Login](screenshots/login.png)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Write meaningful commit messages
- Add tests for new features

---

## 🐛 Known Issues

- [ ] Email verification requires SMTP setup
- [ ] Google OAuth requires Cloud project setup
- [ ] Some stocks may have limited historical data
- [ ] News API has rate limits on free tier

---

## 🗺️ Roadmap

- [ ] Add cryptocurrency support
- [ ] Implement paper trading
- [ ] Add price alerts with notifications
- [ ] Mobile app version
- [ ] Real-time WebSocket data
- [ ] Machine learning price predictions
- [ ] Social trading features
- [ ] Advanced screening tools
- [ ] Options and derivatives analysis
- [ ] Multi-language support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👏 Acknowledgments

- **yfinance** - For free stock data API
- **Plotly** - For interactive charts
- **Streamlit** - For the amazing framework
- **Zerodha Kite** - UI/UX inspiration
- **MoneyControl** - Design inspiration

---

## 📞 Support

- **Email**: support@stockvista.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/stockvista/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/stockvista/discussions)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/stockvista&type=Date)](https://star-history.com/#yourusername/stockvista&Date)

---

<div align="center">

**Made with ❤️ by [Your Name](https://github.com/yourusername)**

If you found this project helpful, please give it a ⭐!

[⬆ Back to Top](#-stockvista---professional-stock-market-dashboard)

</div>
