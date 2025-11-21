# src/binance_client.py
"""
Central Binance Futures client wrapper.
Reads API keys from env and returns a client or a MockClient.
Provides simple place_* wrappers used by CLI scripts.
"""

import os
import time
import logging

try:
    from binance.client import Client as BinanceClient
    from binance.exceptions import BinanceAPIException, BinanceOrderException
except Exception:
    BinanceClient = None
    BinanceAPIException = Exception
    BinanceOrderException = Exception

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
USE_TESTNET = os.getenv("BINANCE_USE_TESTNET", "true").lower() in ("1", "true", "yes")

logger = logging.getLogger(__name__)


class MockClient:
    """Very small mock that returns deterministic fake order responses."""
    def __init__(self):
        self._order_id = 1000

    def futures_create_order(self, **kwargs):
        self._order_id += 1
        now = int(time.time() * 1000)
        resp = {
            "orderId": self._order_id,
            "clientOrderId": f"mock-{self._order_id}",
            "status": "NEW",
            "symbol": kwargs.get("symbol"),
            "origQty": kwargs.get("quantity"),
            "executedQty": "0",
            "type": kwargs.get("type"),
            "side": kwargs.get("side"),
            "fills": [],
            "transactTime": now,
        }
        return resp


def get_client():
    """Return a configured Binance client, or MockClient if missing."""
    if API_KEY and API_SECRET and BinanceClient is not None:
        client = BinanceClient(API_KEY, API_SECRET)
        # Best-effort testnet config (may vary by python-binance version)
        if USE_TESTNET:
            try:
                client.API_URL = "https://testnet.binancefuture.com"
            except Exception:
                pass
        logger.info("Using real Binance client (keys provided)")
        return client
    else:
        logger.warning("Using MockClient (no API keys or python-binance missing)")
        return MockClient()


# Wrappers used by CLI modules (keep parameter names simple)
def place_market_order(client, symbol, side, quantity):
    kwargs = dict(symbol=symbol, side=side.upper(), type="MARKET", quantity=quantity)
    return client.futures_create_order(**kwargs)


def place_limit_order(client, symbol, side, quantity, price, timeInForce="GTC"):
    kwargs = dict(symbol=symbol, side=side.upper(), type="LIMIT", quantity=quantity,
                  price=price, timeInForce=timeInForce)
    return client.futures_create_order(**kwargs)


def place_stop_limit_order(client, symbol, side, quantity, price, stopPrice, timeInForce="GTC"):
    kwargs = dict(symbol=symbol, side=side.upper(), type="STOP_LOSS_LIMIT", quantity=quantity,
                  price=price, stopPrice=stopPrice, timeInForce=timeInForce)
    return client.futures_create_order(**kwargs)
