"""Расчёты: массы компонентов, класс партии, проверка суммы долей"""

import math
from typing import Annotated

from constants import MIXTURES, SMALL_LIMIT, MEDIUM_LIMIT


def component_masses(
    total_mass: Annotated[float, "Общая масса смеси, кг"],
    mixture_key: Annotated[str, "Ключ смеси: '1', '2' или '3'"],
) -> dict[str, float]:
    """Рассчитать массы компонентов смеси по формуле m_i = M · fraction_i.

    Args:
        total_mass: общая масса смеси, кг.
        mixture_key: ключ смеси.

    Returns:
        Словарь {название компонента: масса, кг}.
    """
    fractions = MIXTURES[mixture_key]["fractions"]
    return {
        name: total_mass * fraction
        for name, fraction in fractions.items()
    }


def batch_class(
    mass: Annotated[float, "Общая масса смеси, кг"],
) -> str:
    """Классифицировать партию по массе через if-elif-else.

    M < 100 — малая партия;
    100 ≤ M ≤ 1000 — средняя партия;
    M > 1000 — крупная партия.

    Args:
        mass: общая масса смеси, кг.

    Returns:
        Название класса партии.
    """
    if mass < SMALL_LIMIT:
        return "малая партия"
    elif mass <= MEDIUM_LIMIT:
        return "средняя партия"
    else:
        return "крупная партия"


def fractions_sum(
    mixture_key: Annotated[str, "Ключ смеси"],
) -> float:
    """Вернуть сумму долей компонентов смеси."""
    return sum(MIXTURES[mixture_key]["fractions"].values())


def fractions_are_valid(
    mixture_key: Annotated[str, "Ключ смеси"],
) -> bool:
    """Проверить, что сумма долей компонентов равна 1 (через math.isclose)."""
    return math.isclose(fractions_sum(mixture_key), 1.0, abs_tol=1e-12)