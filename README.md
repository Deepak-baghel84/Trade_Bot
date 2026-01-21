🏗️ ## Project Architecture

trading_bot
│
├── main.py                 # CLI entry point
├── config.py               # API keys & environment config
├── test_connection.py      # Testnet connectivity check
│
├── bot/
│   ├── base_bot.py         # Core bot logic
│   ├── order_manager.py    # Order execution layer
│   ├── validator.py       # Input validation
│
├── utils/
│   ├── logger.py           # Logging setup
│   ├── helper.py           # Utility placeholder
│
├── requirements.txt
└── README.md

===========================================================================

⚙️ # Features Implemented

Binance Futures Testnet integration (USDT-M)

CLI-based order placement

Input validation (symbol, side, type, quantity, price)

Support for:

MARKET orders

LIMIT orders

Structured logging

Error handling with descriptive messages

Modular, extensible design

===========================================================================

# 🚀 How to Run

1️⃣ Install dependencies
'''bash
pip install -r requirements.txt
'''
2️⃣ Set API keys
'''bash
export BINANCE_API_KEY="your_testnet_key"
export BINANCE_API_SECRET="your_testnet_secret"
'''

(or configure in config.py for local testing)

3️⃣ Test connection
'''bash
python test_connection.py
'''
4️⃣ Place a test order
'''bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --testnet
'''
==============================================================================

# ⚠️ Known Issue (Documented)

While placing a MARKET order, an exception is raised during error handling due to the Binance exception object containing non-string data (tuple/dict).


This does not affect:

API authentication
Input validation
System architecture
Order routing logic

=============================================================================

#🧩 Future Improvements

Stop-Limit / OCO orders

WebSocket-based order monitoring

Precision handling via exchange info

Retry logic for transient API errors

Unit tests & mocks

-------------------------------------------------------------------------------

# 📎 Notes

This project prioritizes engineering correctness and safety

No real funds are used

Built strictly for Binance Futures Testnet
