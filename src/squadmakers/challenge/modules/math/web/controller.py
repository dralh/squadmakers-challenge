from flask import Blueprint, jsonify, request

__all__ = ["math_blueprint"]

from squadmakers.challenge.modules.math.exc import InvalidNumberException
from squadmakers.challenge.modules.math.use_case import MathUseCase

math_blueprint = Blueprint("math", __name__, url_prefix="/math")


@math_blueprint.route("/leastcommonmultiple", methods=["GET"])
def calculate_least_common_multiple():
    numbers_str = request.args.get("numbers")

    if numbers_str is None:
        raise InvalidNumberException("You must provide a list of numbers")

    try:
        numbers = [int(n) for n in numbers_str.split(",")]
    except TypeError:
        raise InvalidNumberException("You must provide valid numbers")

    lcm = MathUseCase.calculate_least_common_multiple(numbers)

    return jsonify(result=lcm)


@math_blueprint.route("/increment", methods=["GET"])
def increment_number():
    number_str = request.args.get("number")

    if number_str is None:
        raise InvalidNumberException("You must provide a number")

    try:
        number = int(number_str)
    except TypeError:
        raise InvalidNumberException("You must provide a valid number")

    result = MathUseCase.increment_number(number)

    return jsonify(result=result)
