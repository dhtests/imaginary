"""
Imaginary service — utilities.
"""


def clamp(value: int, lo: int, hi: int) -> int:
    return max(lo, min(value, hi))


def chunk(lst: list, size: int) -> list:
    return [lst[i:i + size] for i in range(0, len(lst), size)]
