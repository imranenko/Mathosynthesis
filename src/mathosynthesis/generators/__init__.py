from .addition import Addition
from .subtraction import Subtraction
from .multiplication import Multiplication
from .division import Division

from .exponentiation import Exponantiation
from .root import Root
from .logarithm import Logarithm

from .fractions import Fractions

register = {
    "addition": Addition.generate_task,
    # "addition_missing": Addition.generate_with_missing_element,
    "column_addition": Addition.generate_column_task,
    "decimal_addition": Addition.generate_with_decimal_numbers,

    "subtraction": Subtraction.generate_task,
    # "subtraction_missing": Subtraction.generate_with_missing_element,
    "column_subtraction": Subtraction.generate_column_task,
    
    "multiplication": Multiplication.generate_task,
    # "multiplication_missing": Multiplication.generate_with_missing_element,
    "multiplication_with_round_numbers": Multiplication.generate_task_with_round_numbers,
    "column_multiplication": Multiplication.generate_column_task,
    
    "division": Division.generate_task,
    # "division_missing": Division.generate_with_missing_element
    # Note: Column division missing
    
    "exponantiation": Exponantiation.generate_task,
    "root": Root.generate_task,
    "logarithm": Logarithm.generate_task,

    "fraction_addition": Fractions.generate_task_with_addition,
    "fraction_simplification": Fractions.generate_tasks_with_simplification,
    "fraction_improper_to_mixed": Fractions.generate_tasks_improper_to_mixed,
    "fraction_mixed_to_improper": Fractions.generate_task_mixed_to_improper,
}