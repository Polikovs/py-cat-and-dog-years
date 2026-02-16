import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    (0, 0, [0, 0]),     # Менше 15
    (14, 14, [0, 0]),   # Граничне значення < 15
    (15, 15, [1, 1]),   # Перший поріг
    (23, 23, [1, 1]),   # Граничне значення < 24
    (24, 24, [2, 2]),   # Другий поріг
    (27, 28, [2, 2]),   # Не вистачає до наступного кроку
    (28, 29, [3, 3]),   # Рівно наступний крок (24+4 для кота, 24+5 для собаки)
    (100, 100, [21, 17])  # Великі значення
])
def test_get_human_age(cat_years: int, dog_years: int, expected: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected
