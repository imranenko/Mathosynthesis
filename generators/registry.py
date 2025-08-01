from generators import Addition, Subtraction, Multiplication, Division

register = {
    "addition": Addition.generate_task,
    "addition_missing": Addition.generate_with_missing_element,
    "subtraction": Subtraction.generate_task,
    "subtraction_missing": Subtraction.generate_with_missing_element,
    "multiplication": Multiplication.generate_task,
    "multiplication_missing": Multiplication.generate_with_missing_element,
    "division": Division.generate_task,
    "division_missing": Division.generate_with_missing_element
}