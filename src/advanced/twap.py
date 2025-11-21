# src/advanced/twap.py
"""
Simple TWAP: split total quantity into N chunks and send market orders.
Usage:
  python src/advanced/twap.py BTCUSDT BUY 0.1 --chunks 5 --interval 2
"""

import argparse
import logging
import sys
import time

from binance_client import get_client, place_market_order
from validators import validate_symbol, validate_quantity

logging.basicConfig(filename="bot.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    parser = argparse.ArgumentParser(description="TWAP executor (simple)")
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("quantity", type=str)
    parser.add_argument("--chunks", type=int, default=5, help="Number of slices")
    parser.add_argument("--interval", type=int, default=2, help="Seconds between slices")
    args = parser.parse_args()

    if not validate_symbol(args.symbol) or not validate_quantity(args.quantity) or args.chunks <= 0 or args.interval < 0:
        logging.error("Invalid inputs for TWAP: %s", args)
        print("Invalid inputs.")
        sys.exit(1)

    client = get_client()
    total_qty = float(args.quantity)
    qty_per = total_qty / args.chunks
    print(f"Executing TWAP: {args.chunks} slices, {qty_per} per slice, interval {args.interval}s")
    for i in range(args.chunks):
        try:
            resp = place_market_order(client, args.symbol.upper(), args.side.upper(), qty_per)
            logging.info("TWAP slice %s executed: %s", i + 1, resp)
            print("Slice", i + 1, "resp:", resp)
        except Exception as e:
            logging.exception("TWAP slice failed: %s", e)
            print("Error in slice", i + 1, e)
        if i < args.chunks - 1:
            time.sleep(args.interval)


if __name__ == "__main__":
    main()
