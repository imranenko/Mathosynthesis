import random

class Multiplication():
    
    def generate_task(num1=(1, 10), num2=(10, 20)):
        num1 = random.randint(*num1)
        num2 = random.randint(*num2)
        return f"$${num1} \cdot {num2} = $$\n"

    def generate_with_missing_element(start=1, end=10):
        num1 = random.randint(start, end)
        num2 = random.randint(start, end)
        product = num1 * num2
        if random.random() < 0.5:
            task = f"$${num1} \cdot \_\_\_ = {product}$$\n"
        else:
            task = f"$$\_\_\_ \cdot {num2} = {product}$$\n"
        return task