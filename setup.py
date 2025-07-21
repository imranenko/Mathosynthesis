from generators.addition import *
from generators.subtraction import *
from generators.multiplication import *
from generators.division import *


def operations_beginner():
    tasks = []
    
    tasks += [Addition.generate_task((100, 1000), (100, 1000)) for _ in  range (5)]
    tasks += "\n"

    tasks += [Subtraction.generate_task((100, 1000), (100, 1000), only_pos=True) for _ in range(5)]
    tasks += "\n"
    
    tasks += [Multiplication.generate_task((2, 9), (21, 29)) for _ in range(5)]
    tasks += "\n"
    
    tasks += [Division.generate_task((2, 9), (21, 29)) for _ in range(5)]
    
    return tasks


def multiplication_beginner():
    tasks = []
    
    tasks += [Multiplication.generate_task((2, 9), (2, 9)) for _ in range(10)]
    tasks += "\n"
    
    tasks += [Multiplication.generate_with_missing_element((2, 9), (2, 9)) for _ in range(10)]
    
    return tasks


def multiplication_intermidiate():
    tasks = []
    
    tasks += [Multiplication.generate_task((7, 9), (11, 19)) for _ in range(10)]
    tasks += "\n"
    
    tasks += [Multiplication.generate_with_missing_element((2,9), (11, 19)) for _ in range(10)]
    
    return tasks  

