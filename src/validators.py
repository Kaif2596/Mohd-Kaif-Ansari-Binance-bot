# src/validators.py
"""
Simple validators for symbol, quantity and price.
"""

import re


def validate_symbol(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    return bool(re.match(r"^[A-Z0-9]+USDT$", symbol.upper()))


def validate_quantity(qty) -> bool:
    try:
        q = float(qty)
        return q > 0
    except Exception:
        return False


def validate_price(price) -> bool:
    try:
        p = float(price)
        return p > 0
    except Exception:
        return False
