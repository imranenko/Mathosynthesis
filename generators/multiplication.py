import random

def generate_multiplication_task(num1=(1, 10), num2=(10, 20)):
    num1 = random.randint(*num1)
    num2 = random.randint(*num2)
    return f"$${num1} \cdot {num2} = $$\n"

def generate_multiplication_task_with_missing_element(start=1, end=10):
    num1 = random.randint(start, end)
    num2 = random.randint(start, end)
    answer = num1 * num2
    if random.random() < 0.5:
        task = f"$${num1} \cdot \_\_\_ = {answer}$$\n"
    else:
        task = f"$$\_\_\_ \cdot {num2} = {answer}$$\n"
    return task


def generate_multiplication_task_as_table(start=1, end=20):
    num1 = random.randint(start, end)
    num2 = random.randint(start, end)
    task = f"""$$
\\begin{{array}}{{r}}
{num1} \\\\
\\underline{{\\times \\ {num2}}} \\\\
\\end{{array}}
$$\n"""
    return task
