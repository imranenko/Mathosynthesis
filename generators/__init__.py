from generators.addition import Addition
from generators.subtraction import Subtraction
from generators.multiplication import Multiplication
from generators.division import Division

register = {
    "addition": lambda settings: Addition.generate_block(task_function=Addition.generate_task, settings=settings),
    "subtraction": lambda settings: Subtraction.generate_block(Subtraction.generate_task, settings=settings),
    "multiplication": lambda settings: Multiplication.generate_block(Multiplication.generate_task, settings=settings),
    "division": lambda settings: Division.generate_block(Division.generate_task, settings=settings),
    # "addition_missing": Addition.generate_with_missing_element,
    # "subtraction_missing": Subtraction.generate_with_missing_element,
    # "multiplication_missing": Multiplication.generate_with_missing_element,
    # "division_missing": Division.generate_with_missing_element
}