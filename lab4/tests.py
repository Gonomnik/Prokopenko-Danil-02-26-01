"""
Юнит-тесты для validation и operations
Запуск:
    python -m unittest tests -v
"""

import unittest
from unittest.mock import patch

import logger
import operations
import validation


class BaseTestCase(unittest.TestCase):
    """Базовый класс тестов: очищает журнал перед каждым тестом."""

    def setUp(self) -> None:
        """Очистить журнал ошибок."""
        logger.clear()


class TestValidateRange(BaseTestCase):
    """Тесты функции validate_range."""

    def test_inside(self) -> None:
        """Значение внутри диапазона."""
        ok, msg = validation.validate_range(500.0, 1.0, 10000.0)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_on_low_boundary(self) -> None:
        """Значение на нижней границе."""
        ok, msg = validation.validate_range(1.0, 1.0, 10000.0)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_on_high_boundary(self) -> None:
        """Значение на верхней границе."""
        ok, msg = validation.validate_range(10000.0, 1.0, 10000.0)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_below(self) -> None:
        """Значение меньше диапазона."""
        ok, msg = validation.validate_range(0.5, 1.0, 10000.0)
        self.assertFalse(ok)
        self.assertIn("меньше", msg)

    def test_above(self) -> None:
        """Значение больше диапазона."""
        ok, msg = validation.validate_range(20000.0, 1.0, 10000.0)
        self.assertFalse(ok)
        self.assertIn("больше", msg)


class TestInputMass(BaseTestCase):
    """Тесты циклического ввода массы смеси (3 теста)."""

    def test_cycle_abc_big_small(self) -> None:
        """Сначала не число, затем больше максимума, затем корректно."""
        with patch("validation.input", side_effect=["abc", "20000", "500"]):
            result = validation.input_mass()

        self.assertEqual(result, 500.0)
        self.assertEqual(len(logger.get_entries()), 2)

    def test_lower_boundary(self) -> None:
        """Нижняя граница массы M = 1."""
        with patch("validation.input", side_effect=["1"]):
            result = validation.input_mass()

        self.assertEqual(result, 1.0)

    def test_upper_boundary(self) -> None:
        """Верхняя граница массы M = 10000."""
        with patch("validation.input", side_effect=["10000"]):
            result = validation.input_mass()

        self.assertEqual(result, 10000.0)


class TestOperations(BaseTestCase):
    """Тесты расчётов и классификации."""

    def test_component_masses_concrete(self) -> None:
        """Массы компонентов бетона при M = 1000 кг."""
        masses = operations.component_masses(1000.0, "1")
        self.assertAlmostEqual(masses["цемент"], 150.0)
        self.assertAlmostEqual(masses["песок"], 350.0)
        self.assertAlmostEqual(masses["щебень"], 500.0)

    def test_component_masses_ceramic(self) -> None:
        """Массы компонентов керамики при M = 1000 кг."""
        masses = operations.component_masses(1000.0, "2")
        self.assertAlmostEqual(masses["глина"], 600.0)
        self.assertAlmostEqual(masses["песок"], 250.0)
        self.assertAlmostEqual(masses["добавка"], 150.0)

    def test_component_masses_alloy(self) -> None:
        """Массы компонентов сплава при M = 1000 кг."""
        masses = operations.component_masses(1000.0, "3")
        self.assertAlmostEqual(masses["Cu"], 700.0)
        self.assertAlmostEqual(masses["Zn"], 250.0)
        self.assertAlmostEqual(masses["Pb"], 50.0)

    def test_batch_class_small(self) -> None:
        """Малая партия: M < 100."""
        self.assertEqual(operations.batch_class(5.0), "малая партия")

    def test_batch_class_lower_boundary(self) -> None:
        """Граница 100 кг относится к средней партии."""
        self.assertEqual(operations.batch_class(100.0), "средняя партия")

    def test_batch_class_medium(self) -> None:
        """Средняя партия: 100 <= M <= 1000."""
        self.assertEqual(operations.batch_class(500.0), "средняя партия")

    def test_batch_class_upper_boundary(self) -> None:
        """Граница 1000 кг относится к средней партии."""
        self.assertEqual(operations.batch_class(1000.0), "средняя партия")

    def test_batch_class_large(self) -> None:
        """Крупная партия: M > 1000."""
        self.assertEqual(operations.batch_class(1001.0), "крупная партия")

    def test_fractions_sum_concrete(self) -> None:
        """Сумма долей бетона равна 1."""
        self.assertAlmostEqual(operations.fractions_sum("1"), 1.0)

    def test_fractions_sum_ceramic(self) -> None:
        """Сумма долей керамики равна 1."""
        self.assertAlmostEqual(operations.fractions_sum("2"), 1.0)

    def test_fractions_sum_alloy(self) -> None:
        """Сумма долей сплава равна 1."""
        self.assertAlmostEqual(operations.fractions_sum("3"), 1.0)

    def test_fractions_are_valid_all(self) -> None:
        """Проверка fractions_are_valid для всех трёх смесей."""
        for key in ("1", "2", "3"):
            self.assertTrue(operations.fractions_are_valid(key))