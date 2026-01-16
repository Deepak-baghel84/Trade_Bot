from utils.logger import CustomLogger
from bot.base_bot import BasicBot
from bot.validator import validate_order_input
from config import API_KEY, API_SECRET
import argparse

log=CustomLogger().get_logger(__file__)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Simplified Binance Futures Trading Bot (Testnet)"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    parser.add_argument("--testnet", action="store_true", help="Use Binance Futures Testnet")

    return parser.parse_args()



def main():
    args = parse_arguments()
    log.info("Received CLI arguments")

        # Validate inputs
    try:
        validate_order_input(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
    except ValueError as e:
        log.error(f"Input validation failed: {e}")
        print(f"❌ Input Error: {e}")
        return
    
        # Initialize bot
    bot = BasicBot(
        api_key=API_KEY,
        api_secret=API_SECRET,
        testnet=args.testnet,
    )
         # Place order
    try:
        order_response = bot.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("✅ Order placed successfully")
        print(order_response)

    except Exception as e:
        log.exception("Order placement failed")
        print(f"❌ Order Failed: {str(e)}")


if __name__ == "__main__":
    main()
    log.info("Initialized trading bot")



