import os

# ⚠️ Never hardcode real keys in production
API_KEY = os.getenv("BINANCE_API_KEY", "YOUR_TESTNET_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET", "YOUR_TESTNET_API_SECRET")

# Binance Futures URLs
BINANCE_FUTURES_TESTNET_URL = "https://testnet.binancefuture.com"
BINANCE_FUTURES_LIVE_URL = "https://fapi.binance.com"

# Default settings
DEFAULT_TESTNET = True
DEFAULT_RECV_WINDOW = 5000