# src/advanced/stop_limit.py
"""
Simple stop-limit wrapper.
Usage:
  python src/advanced/stop_limit.py BTCUSDT BUY 0.01 98000 97900
  (symbol side qty stopPrice limitPrice)
"""

import argparse
import logging
import sys

from binance_client import get_client, place_stop_limit_order
from validators import validate_symbol, validate_quantity, validate_price

logging.basicConfig(filename="bot.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    parser = argparse.ArgumentParser(description="Place STOP-LIMIT order")
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("quantity", type=str)
    parser.add_argument("stopPrice", type=str, help="Trigger price")
    parser.add_argument("price", type=str, help="Limit price to place when triggered")
    args = parser.parse_args()

    if not (validate_symbol(args.symbol) and validate_quantity(args.quantity)
            and validate_price(args.stopPrice) and validate_price(args.price)):
        print("Invalid inputs")
        logging.error("Invalid inputs for stop-limit: %s", args)
        sys.exit(1)

    client = get_client()
    try:
        resp = place_stop_limit_order(client, args.symbol.upper(), args.side.upper(),
                                      float(args.quantity), float(args.price), float(args.stopPrice))
        logging.info("Stop-limit order placed: %s", resp)
        print("Order response:")
        print(resp)
    except Exception as e:
        logging.exception("Failed to place stop-limit order: %s", e)
        print("Error placing stop-limit order:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
