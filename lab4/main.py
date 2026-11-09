<<<<<<< HEAD
"""Точка входа: расчёт компонентов технологической смеси"""

from validation import input_mass
from menu import show_menu, select_mode, mode_name
from operations import component_masses, batch_class, fractions_are_valid


def main() -> None:
    """Главный сценарий программы."""
    print("=== Расчёт компонентов технологической смеси ===")

    while True:
        show_menu()
        key = select_mode()
        if key is None:
            print("Работа завершена.")
            break

        if not fractions_are_valid(key):
            print("Ошибка: сумма долей компонентов не равна 1. Расчёт отменён.")
            continue

        mass = input_mass()

        masses = component_masses(mass, key)
        cls = batch_class(mass)

        print("\n Результаты ")
        print(f"Тип смеси:   {mode_name(key)}")
        for component, component_mass in masses.items():
            print(f"  {component}: {component_mass:.2f} кг")
        print(f"Класс партии: {cls}")
        print("\n")


if __name__ == "__main__":
=======
"""Точка входа: расчёт компонентов технологической смеси"""

from validation import input_mass
from menu import show_menu, select_mode, mode_name
from operations import component_masses, batch_class, fractions_are_valid


def main() -> None:
    """Главный сценарий программы."""
    print("=== Расчёт компонентов технологической смеси ===")

    while True:
        show_menu()
        key = select_mode()
        if key is None:
            print("Работа завершена.")
            break

        if not fractions_are_valid(key):
            print("Ошибка: сумма долей компонентов не равна 1. Расчёт отменён.")
            continue

        mass = input_mass()

        masses = component_masses(mass, key)
        cls = batch_class(mass)

        print("\n Результаты ")
        print(f"Тип смеси:   {mode_name(key)}")
        for component, component_mass in masses.items():
            print(f"  {component}: {component_mass:.2f} кг")
        print(f"Класс партии: {cls}")
        print("\n")


if __name__ == "__main__":
>>>>>>> c95305767346365f32b91a9307371588d386ea2e
    main()