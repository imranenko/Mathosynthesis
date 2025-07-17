import random

class Division():
    
    def generate_task(factor1=(2, 9), factor2=(2, 9)):
        num1 = random.randint(*factor1)
        num2 = random.randint(*factor2)
        product = num1 * num2
        
        if random.random() < 0.5:
            task = f"$${product} \div {num1} = $$\n"
        else:
            task = f"$${product} \div {num2} = $$\n"
        return task

    def generate_with_missing_element(factor1=(2, 9), factor2=(2,9)):
        num1 = random.randint(*factor1)
        num2 = random.randint(*factor2)
        product = num1 * num2

        if random.random() < 0.5:
            task = f"$${product} \div \_\_\_ = {num1}$$\n"
        else:
            task = f"$$\_\_\_ \div {num2} = {num1}$$\n"
        return task


if __name__ == "__main__":
    for i in range(10):
        print(Division.generate_with_missing_element())