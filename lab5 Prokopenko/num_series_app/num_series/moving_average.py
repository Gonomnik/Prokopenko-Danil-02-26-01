"""Модуль скользящих средних."""
from typing import List, Sequence

def _check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or window < 1:
        raise ValueError(f"window должно быть целым >= 1 (получено: {window})")
    if window > n:
        raise ValueError(f"window ({window}) больше длины ряда ({n})")

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму (O(n))."""
    _check_window(window, len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA (окно должно быть нечётным)."""
    if window % 2 == 0:
        raise ValueError("Для центрированного MA окно должно быть нечётным")
    _check_window(window, len(data))
    half = window // 2
    return [
        sum(data[i - half : i + half + 1]) / window
        for i in range(half, len(data) - half)
    ]

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: alpha в (0, 1]."""
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должно быть в (0, 1] (получено: {alpha})")
    if not data:
        raise ValueError("Ряд пуст")
    result = [float(data[0])]
    for x in data[1:]:
        result.append(alpha * x + (1 - alpha) * result[-1])
    return result