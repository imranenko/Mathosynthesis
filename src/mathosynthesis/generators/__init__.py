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

    "subtraction": Subtraction.generate_task,
    "multiplication": Multiplication.generate_task,
    "division": Division.generate_task,
    
    "multiplication_with_round_numbers": Multiplication.generate_task_with_round_numbers,
    
    "exponantiation": Exponantiation.generate_task,
    "root": Root.generate_task,
    "logarithm": Logarithm.generate_task,

    "fraction_addition": Fractions.generate_task_with_addition,
    "fraction_simplification": Fractions.generate_tasks_with_simplification,
    "fraction_improper_to_mixed": Fractions.generate_tasks_improper_to_mixed,
    "fraction_mixed_to_improper": Fractions.generate_task_mixed_to_improper,
    
    # "addition_missing": Addition.generate_with_missing_element,
    # "subtraction_missing": Subtraction.generate_with_missing_element,
    # "multiplication_missing": Multiplication.generate_with_missing_element,
    # "division_missing": Division.generate_with_missing_element
    
    "column_addition": Addition.generate_column_task,
    "column_subtraction": Subtraction.generate_column_task,
    "column_multiplication": Multiplication.generate_column_task,
}