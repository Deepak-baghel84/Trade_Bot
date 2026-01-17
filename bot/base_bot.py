from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from utils.logger import CustomLogger

log=CustomLogger().get_logger(__file__)

#from config import (
BINANCE_FUTURES_TESTNET_URL="https://testnet.binancefuture.com",
BINANCE_FUTURES_LIVE_URL="https://fapi.binance.com",
#)

class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
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
        log.info(f"Placing {order_type} order: {side} {quantity} {symbol} at {price if price else 'Market Price'}")
        try:
            if order_type == "MARKET":
                print("Placing market order...")
                resp = self._place_market_order(symbol=symbol, side=side, quantity=quantity)
                print(resp)
                return resp

            elif order_type == "LIMIT":
                return self._place_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)

            else:
                raise ValueError("Unsupported order type")

        except (BinanceAPIException, BinanceOrderException) as e:
            log.error(f"Order placement failed: {str(e)}")
            raise RuntimeError(f"Binance error: {str(e)}")
     
    

    def _place_market_order(self, symbol: str, side: str, quantity: float):
    # Set leverage (required for futures)
        try:
            info = self.client.futures_exchange_info()
            symbols_info = info['symbols']
            symbol_info = next((item for item in symbols_info if item['symbol'] == symbol), None)
            if symbol_info is None:
                raise ValueError(f"Symbol {symbol} not found in exchange info")
            leverage_brackets = symbol_info.get('brackets', [])
            if not leverage_brackets:
                raise ValueError(f"No leverage brackets found for symbol {symbol}")
            max_leverage = int(leverage_brackets[-1]['initialLeverage'])
            self.client.futures_change_leverage(symbol=symbol, leverage=max_leverage)
        #self.client.futures_change_leverage(symbol=symbol,leverage=1)

        #order = self.client.futures_create_order(symbol=symbol,side=side,type="MARKET", quantity=quantity,)

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",  
                quantity=quantity,
            )
            log.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            log.error(f"Failed to place market order: {str(e)}")
            raise RuntimeError(f"Failed to place market order: {str(e)}")
        

    def _place_limit_order(self, symbol: str='BTCUSDT', side: str='SELL', quantity: float=0.001, price: float=1000000.00):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )
    

#if __name__ == "__main__":
 #   api_key ="your api key here"
  #  api_secret ="your api secret here"
#
    #log.info("BasicBot module loaded")
 #   guest=BasicBot(api_key, api_secret, testnet=True)
    #log.info("BasicBot instance created for testing")

