<<<<<<< HEAD
"""Меню выбора типа технологической смеси через match-case"""

from __future__ import annotations


def show_menu() -> None:
    """Вывести меню типов смесей."""
    print("\n Выберите тип технологической смеси:")
    print("  1 — бетон     (цемент 0.15, песок 0.35, щебень 0.50)")
    print("  2 — керамика  (глина 0.60, песок 0.25, добавка 0.15)")
    print("  3 — сплав     (Cu 0.70, Zn 0.25, Pb 0.05)")
    print("  0 — выход")


def select_mode() -> str | None:
    """Циклически запрашивать режим и возвращать ключ смеси через match-case.

    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер режима (от 0 до 3): ").strip()
        match choice:
            case "1":
                return "1"
            case "2":
                return "2"
            case "3":
                return "3"
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")


def mode_name(key: str) -> str:
    """Вернуть название смеси по ключу через match-case."""
    match key:
        case "1":
            return "бетон"
        case "2":
            return "керамика"
        case "3":
            return "сплав"
        case _:
=======
"""Меню выбора типа технологической смеси через match-case"""

from __future__ import annotations


def show_menu() -> None:
    """Вывести меню типов смесей."""
    print("\n Выберите тип технологической смеси:")
    print("  1 — бетон     (цемент 0.15, песок 0.35, щебень 0.50)")
    print("  2 — керамика  (глина 0.60, песок 0.25, добавка 0.15)")
    print("  3 — сплав     (Cu 0.70, Zn 0.25, Pb 0.05)")
    print("  0 — выход")


def select_mode() -> str | None:
    """Циклически запрашивать режим и возвращать ключ смеси через match-case.

    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер режима (от 0 до 3): ").strip()
        match choice:
            case "1":
                return "1"
            case "2":
                return "2"
            case "3":
                return "3"
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")


def mode_name(key: str) -> str:
    """Вернуть название смеси по ключу через match-case."""
    match key:
        case "1":
            return "бетон"
        case "2":
            return "керамика"
        case "3":
            return "сплав"
        case _:
>>>>>>> c95305767346365f32b91a9307371588d386ea2e
            return "неизвестно"