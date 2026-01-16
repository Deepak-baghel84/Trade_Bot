from binance.client import Client
from config import API_KEY, API_SECRET, BINANCE_FUTURES_TESTNET_URL

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BINANCE_FUTURES_TESTNET_URL

try:
    account_info = client.futures_account()
    print("✅ Connection successful")
    print("Available balance:", account_info["availableBalance"])
except Exception as e:
    print("❌ Connection failed:", e)
