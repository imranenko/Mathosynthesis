from .addition import Addition
from .subtraction import Subtraction
from .multiplication import Multiplication
from .division import Division

from .exponentiation import Exponantiation
from .root import Root
from .logarithm import Logarithm

register = {
    "addition": Addition.generate_task,
    "subtraction": Subtraction.generate_task,
    "multiplication": Multiplication.generate_task,
    "division": Division.generate_task,
    
    "multiplication_with_round_numbers": Multiplication.generate_task_with_round_numbers,
    
    "exponantiation": Exponantiation.generate_task,
    "root": Root.generate_task,
    "logarithm": Logarithm.generate_task,
    
    
    # "addition_missing": Addition.generate_with_missing_element,
    # "subtraction_missing": Subtraction.generate_with_missing_element,
    # "multiplication_missing": Multiplication.generate_with_missing_element,
    # "division_missing": Division.generate_with_missing_element
}