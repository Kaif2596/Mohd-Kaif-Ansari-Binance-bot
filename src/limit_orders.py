# src/limit_orders.py
"""
CLI to place a limit order.
Usage:
  python src/limit_orders.py BTCUSDT BUY 0.01 48000
"""

import argparse
import logging
import sys

from binance_client import get_client, place_limit_order
from validators import validate_symbol, validate_quantity, validate_price

logging.basicConfig(filename="bot.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    parser = argparse.ArgumentParser(description="Place a Binance Futures LIMIT order")
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("quantity", type=str)
    parser.add_argument("price", type=str, help="Limit price")
    args = parser.parse_args()

    if not validate_symbol(args.symbol):
        logging.error("Invalid symbol: %s", args.symbol)
        print("Invalid symbol. Must be like BTCUSDT")
        sys.exit(1)
    if not validate_quantity(args.quantity):
        logging.error("Invalid quantity: %s", args.quantity)
        print("Invalid quantity. Must be a positive number.")
        sys.exit(1)
    if not validate_price(args.price):
        logging.error("Invalid price: %s", args.price)
        print("Invalid price. Must be a positive number.")
        sys.exit(1)

    client = get_client()
    try:
        qty = float(args.quantity)
        price = float(args.price)
        resp = place_limit_order(client, args.symbol.upper(), args.side.upper(), qty, price)
        logging.info("Limit order placed: %s", resp)
        print("Order response:")
        print(resp)
    except Exception as e:
        logging.exception("Failed to place limit order: %s", e)
        print("Error placing order:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
