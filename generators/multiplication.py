from .generator import Generator
import random

class Multiplication(Generator):
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        
        for _ in range(amount):
            factor1 = random.randint(*range1)
            factor2 = random.randint(*range2)
            
            tasks.append( f"${factor1} \\cdot {factor2} = $\n")
        
        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))

        
        for _ in range(amount):
            factor1 = random.randint(*range1)
            factor2 = random.randint(*range2)
            product = factor1 * factor2
            
            if random.random() < 0.5:
                task = f"${factor1} \\cdot \\_\\_\\_ = {product}$\n"
            else:
                task = f"$\\_\\_\\_ \\cdot {factor2} = {product}$\n"
            
            tasks.append(task)
            
        return tasks
    
if __name__ == "__init__":
    print("Hello World!!!")
    print(Multiplication.generate_with_missing_element())