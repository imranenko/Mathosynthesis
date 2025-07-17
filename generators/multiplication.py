import random

class Multiplication():
    
    def generate_task(range1=(1, 10), range2=(10, 20)):
        factor1 = random.randint(*range1)
        factor2 = random.randint(*range2)
        
        return f"$${factor1} \\cdot {factor2} = $$\n"

    def generate_with_missing_element(range1=(1, 10), range2=(1, 10)):
        factor1 = random.randint(*range1)
        factor2 = random.randint(*range2)
        product = factor1 * factor2
        
        if random.random() < 0.5:
            task = f"$${factor1} \\cdot \\_\\_\\_ = {product}$$\n"
        else:
            task = f"$$\\_\\_\\_ \\cdot {factor2} = {product}$$\n"
        return task
    
if __name__ == "__init__":
    print("Hello World!!!")
    print(Multiplication.generate_with_missing_element())