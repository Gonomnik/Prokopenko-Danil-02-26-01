"""Модуль генерации данных"""
import math
import random
from typing import List, Optional

def _validate_n(n: int) -> None:
    """Проверка, что n — положительное целое."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"n должно быть положительным целым (получено: {n!r})")

def random_series(n: int, low: float = -100.0, high: float = 100.0, seed: Optional[int] = None) -> List[float]:
    """Ряд из n случайных чисел на [low, high]."""
    _validate_n(n)
    if low >= high:
        raise ValueError(f"low должно быть < high (получено: {low} >= {high})")
    rng = random.Random(seed)
    return [rng.uniform(low, high) for _ in range(n)]

def sine_series(n: int, amplitude: float = 1.0, frequency: float = 1.0, noise: float = 0.0, seed: Optional[int] = None) -> List[float]:
    """Синусоидальный ряд с шумом."""
    _validate_n(n)
    rng = random.Random(seed)
    return [
        amplitude * math.sin(2 * math.pi * frequency * i / n) 
        + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]

def trend_series(n: int, start: float = 0.0, step: float = 1.0, noise: float = 0.0, seed: Optional[int] = None) -> List[float]:
    """Линейный тренд."""
    _validate_n(n)
    rng = random.Random(seed)
    return [
        start + step * i + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]