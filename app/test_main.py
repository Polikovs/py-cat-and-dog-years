import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    (-15, -5, [0, 0]),  # Тест на від'ємні числа
    (0, 0, [0, 0]),  # Менше 15
    (15.9, 15.9, [1, 1]),  # Плаваюча кома
    (14, 14, [0, 0]),   # Граничне значення < 15
    (15, 15, [1, 1]),   # Перший поріг
    (23, 23, [1, 1]),   # Граничне значення < 24
    (24, 24, [2, 2]),   # Другий поріг
    (27, 27, [2, 2]),   # Не вистачає до наступного кроку кота
    (27, 28, [2, 2]),   # Не вистачає до наступного кроку кота та собаки
    (28, 28, [3, 2]),   # Наступний крок для кота
    (28, 29, [3, 3]),   # Рівно наступний крок (24+4 для кота, 24+5 для собаки)
    (100, 100, [21, 17]),  # Великі значення
    (10**6, 10**6, [249996, 199997]),  # Тест на дуже великі числа
])
def test_get_human_age(cat_years: int, dog_years: int, expected: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected


def test_result_type() -> None:
    result = get_human_age(24, 24)

    assert isinstance(result, list), "Результат має бути списком"
    assert isinstance(result[0], int), "Елементи мають бути цілими числами"
