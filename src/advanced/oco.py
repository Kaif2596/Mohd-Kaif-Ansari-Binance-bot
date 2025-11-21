# src/advanced/oco.py
"""
Create a take-profit (limit) + stop-loss (stop-limit) pair.
Usage:
  python src/advanced/oco.py BTCUSDT BUY 0.01 96000 94000 93900
  (symbol side qty take_profit stop_trigger stop_limit_price)
"""

import argparse
import logging
import sys

from binance_client import get_client, place_limit_order, place_stop_limit_order
from validators import validate_symbol, validate_quantity, validate_price

logging.basicConfig(filename="bot.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    parser = argparse.ArgumentParser(description="Create OCO pair (TP + SL)")
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("quantity", type=str)
    parser.add_argument("take_profit", type=str)
    parser.add_argument("stop_trigger", type=str)
    parser.add_argument("stop_limit_price", type=str)
    args = parser.parse_args()

    if not (validate_symbol(args.symbol) and validate_quantity(args.quantity)
            and validate_price(args.take_profit) and validate_price(args.stop_trigger)
            and validate_price(args.stop_limit_price)):
        logging.error("Invalid inputs for OCO: %s", args)
        print("Invalid inputs.")
        sys.exit(1)

    client = get_client()
    try:
        qty = float(args.quantity)
        # If side is BUY, TP and SL are SELL orders (to close)
        close_side = "SELL" if args.side == "BUY" else "BUY"

        tp_resp = place_limit_order(client, args.symbol.upper(), close_side, qty, float(args.take_profit))
        logging.info("Placed take-profit order: %s", tp_resp)

        sl_resp = place_stop_limit_order(client, args.symbol.upper(), close_side, qty,
                                         float(args.stop_limit_price), float(args.stop_trigger))
        logging.info("Placed stop-loss order: %s", sl_resp)

        print("TP response:", tp_resp)
        print("SL response:", sl_resp)
        print("(Note: this is a pair placement; true OCO requires monitoring/cancelling.)")
    except Exception as e:
        logging.exception("Failed to place OCO orders: %s", e)
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
