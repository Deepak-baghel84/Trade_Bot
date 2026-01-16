from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from utils.logger import CustomLogger

log=CustomLogger().get_logger(__file__)

from config import (
    BINANCE_FUTURES_TESTNET_URL,
    BINANCE_FUTURES_LIVE_URL,
)

class BasicBot:
    def _init_(self, api_key: str, api_secret: str, testnet: bool = True):
        self.testnet = testnet
        self.client = Client(api_key, api_secret)

        # Configure Futures endpoint
        if self.testnet:
            self.client.FUTURES_URL = BINANCE_FUTURES_TESTNET_URL
        else:
            self.client.FUTURES_URL = BINANCE_FUTURES_LIVE_URL
        
        log.info(f"Initialized BasicBot in {'Testnet' if self.testnet else 'Live'} mode")

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None,
    ):
        """
        Places a Futures order on Binance (Market or Limit).
        Returns order response.
        """

        try:
            if order_type == "MARKET":
                return self._place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                return self._place_limit_order(symbol, side, quantity, price)

            else:
                raise ValueError("Unsupported order type")

        except (BinanceAPIException, BinanceOrderException) as e:
            raise RuntimeError(f"Binance error: {e.message}")

    def _place_market_order(self, symbol: str, side: str, quantity: float):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

    def _place_limit_order(
        self, symbol: str, side: str, quantity: float, price: float
    ):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )