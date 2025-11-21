# src/advanced/grid_strategy.py
"""
Basic grid: place limit orders equally spaced between lower and upper price.
Usage:
  python src/advanced/grid_strategy.py BTCUSDT BUY 0.01 45000 55000 5
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
    parser = argparse.ArgumentParser(description="Create grid of limit orders")
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("quantity", type=str)
    parser.add_argument("lower", type=str, help="Lower price bound")
    parser.add_argument("upper", type=str, help="Upper price bound")
    parser.add_argument("grids", type=int, help="Number of grid levels (integer)")
    args = parser.parse_args()

    if not (validate_symbol(args.symbol) and validate_quantity(args.quantity)
            and validate_price(args.lower) and validate_price(args.upper) and args.grids > 0):
        logging.error("Invalid inputs for grid: %s", args)
        print("Invalid inputs.")
        sys.exit(1)

    low = float(args.lower)
    high = float(args.upper)
    if low >= high:
        print("Lower must be < upper")
        sys.exit(1)

    qty = float(args.quantity)
    client = get_client()
    step = (high - low) / (args.grids - 1)
    orders = []
    for i in range(args.grids):
        price = low + step * i
        order_side = "BUY" if args.side == "BUY" else "SELL"
        try:
            resp = place_limit_order(client, args.symbol.upper(), order_side, qty, price)
            logging.info("Grid order placed: %s", resp)
            orders.append(resp)
            print("Placed grid order at", price)
        except Exception as e:
            logging.exception("Failed placing grid order at %s: %s", price, e)
            print("Failed placing order at", price, e)
    print("Grid placement complete. Orders:", orders)


if __name__ == "__main__":
    main()
