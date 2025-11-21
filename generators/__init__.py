from generators.addition import Addition
from generators.subtraction import Subtraction
from generators.multiplication import Multiplication
from generators.division import Division

from generators.exponentiation import Exponantiation
from generators.root import Root
from generators.logarithm import Logarithm

register = {
    "addition": Addition.generate_task,
    "subtraction": Subtraction.generate_task,
    "multiplication": Multiplication.generate_task,
    "division": Division.generate_task,
    
    "exponantiation": Exponantiation.generate_task,
    "root": Root.generate_task,
    "logarithm": Logarithm.generate_task,
    
    # "addition_missing": Addition.generate_with_missing_element,
    # "subtraction_missing": Subtraction.generate_with_missing_element,
    # "multiplication_missing": Multiplication.generate_with_missing_element,
    # "division_missing": Division.generate_with_missing_element
}