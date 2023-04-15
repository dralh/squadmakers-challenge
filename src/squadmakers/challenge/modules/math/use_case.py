import math
from typing import List

__all__ = ["MathUseCase"]

from squadmakers.challenge.modules.math.exc import InvalidNumberException


class MathUseCase:
    @staticmethod
    def calculate_least_common_multiple(numbers: List[int]) -> int:
        if not numbers:
            raise InvalidNumberException("You must provide numbers")

        if not all(isinstance(n, int) for n in numbers):
            raise InvalidNumberException("You must provide valid numbers")

        return math.lcm(*numbers)

    @staticmethod
    def increment_number(number: int) -> int:
        if not isinstance(number, int):
            raise InvalidNumberException("You must provide a valid number")

        return number + 1
