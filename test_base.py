from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
#from utils.logger import CustomLogger

#log=CustomLogger().get_logger(__file__)

BINANCE_FUTURES_TESTNET_URL="https://testnet.binancefuture.com"
BINANCE_FUTURES_LIVE_URL="https://fapi.binance.com"

class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        print("Initializing BasicBot...")
        self.testnet = testnet
        self.client = Client(api_key, api_secret)

        # Configure Futures endpoint
        if self.testnet:
            self.client.FUTURES_URL = BINANCE_FUTURES_TESTNET_URL
        else:
            self.client.FUTURES_URL = BINANCE_FUTURES_LIVE_URL
        #log.info(f"Initialized BasicBot in {'Testnet' if self.testnet else 'Live'} mode")

if __name__ == "__main__":
    api_key ="FLbodqUqykilaiWiWZ2NdStAY4Mh1w4cwmrATB6kH5TnOVAzoYYMxJICvEZI0cj0"
    api_secret ="P33gkx1OUBDcv3cb97zDyODVtxJJ8NIaiKiXqnYmf5KSEDyWkKtUJgdE36W0mpGa"

    #log.info("BasicBot module loaded")
    guest=BasicBot(api_key, api_secret, testnet=True)
    #log.info("BasicBot instance created for testing")