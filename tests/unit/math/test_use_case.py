import pytest

from squadmakers.challenge.modules.math.exc import InvalidNumberException
from squadmakers.challenge.modules.math.use_case import MathUseCase


def test_calculate_least_common_multiple_with_invalid_numbers():
    with pytest.raises(InvalidNumberException):
        MathUseCase.calculate_least_common_multiple(["aa", 2])


@pytest.mark.parametrize(
    "numbers,expected_result",
    [
        ([1, 2, 3], 6),
        ([5, 2, 3], 30),
        ([4, 2], 4),
        ([1, 1, 1], 1),
    ],
)
def test_calculate_least_common_multiple_with_valid_numbers(
    numbers, expected_result
):
    result = MathUseCase.calculate_least_common_multiple(numbers)
    assert result == expected_result


def test_increment_number_with_invalid_number():
    with pytest.raises(InvalidNumberException):
        MathUseCase.increment_number("hola")


@pytest.mark.parametrize(
    "number,expected_result",
    [
        (5, 6),
        (50000, 50001),
        (359, 360),
        (23892, 23893),
    ],
)
def test_increment_number_with_valid_number(number, expected_result):
    result = MathUseCase.increment_number(number)
    assert result == expected_result
