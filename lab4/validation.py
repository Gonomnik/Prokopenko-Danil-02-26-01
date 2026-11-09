"""
Валидация пользовательского ввода: масса смеси 
-Проверка границ через if-elif-else.
-Циклический ввод до корректного значения.
"""

from __future__ import annotations

from constants import M_MIN, M_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """Проверка попадания value в [low, high] через if-elif-else.

    Returns:
        (True, "") — если значение в диапазоне, иначе (False, сообщение).
        """
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """Циклически запрашивать число, пока не будет корректного.

    Проверяет тип (float) через try/except ValueError и границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_mass() -> float:
    """Циклический ввод общей массы смеси M (кг), допустимо 1..10000."""
    return input_number(
        "Введите общую массу смеси M, кг (1..10000): ",
        M_MIN, M_MAX,
)