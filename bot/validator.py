from utils.logger import CustomLogger
log=CustomLogger().get_logger(__file__)

def validate_order_input(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
):
    """
    Validates user input before sending it to Binance.
    Raises ValueError if validation fails.
    """

    # 1️⃣ Symbol validation
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-margined pairs are supported (e.g. BTCUSDT)")

    # 2️⃣ Side validation
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be either BUY or SELL")

    # 3️⃣ Order type validation
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("Order type must be MARKET or LIMIT")

    # 4️⃣ Quantity validation
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # 5️⃣ Price validation (only for LIMIT orders)
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

    # 6️⃣ Price should not be provided for MARKET orders
    if order_type == "MARKET" and price is not None:
        raise ValueError("Price should not be provided for MARKET orders")
    
    log.info("Order input validation passed")
    return True

