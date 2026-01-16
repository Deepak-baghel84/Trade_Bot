
from binance.exceptions import BinanceAPIException, BinanceOrderException

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol: str, side: str, quantity: float):
        try:
            return self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )
        except (BinanceAPIException, BinanceOrderException) as e:
            raise RuntimeError(f"Market order failed: {e.message}")
def place_limit_order(
        self, symbol: str, side: str, quantity: float, price: float
    ):
        try:
            return self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )
        except (BinanceAPIException, BinanceOrderException) as e:
            raise RuntimeError(f"Limit order failed: {e.message}")
        
def place_stop_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        stop_price: float,
        price: float,
    ):
        try:
            return self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                stopPrice=stop_price,
                price=price,
                timeInForce="GTC",
            )
        except (BinanceAPIException, BinanceOrderException) as e:
            raise RuntimeError(f"Stop-Limit order failed: {e.message}")
        

        