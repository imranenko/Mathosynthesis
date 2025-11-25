import random

class Multiplication():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        factor1_range = settings.get("factor1", (1, 10))
        factor2_range = settings.get("factor2", (1, 10))
        commutative = settings.get("commutative", False)
        
        
        for _ in range(amount):
            if commutative and random.random() < 0.5:
                factor1_range, factor2_range = factor2_range, factor1_range
            
            factor1 = random.randint(*factor1_range)
            factor2 = random.randint(*factor2_range)
            
            tasks.append( f"{factor1} \\cdot {factor2} = \n")
        
        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        factor1_range = settings.get("factor1", (1, 10))
        factor2_range = settings.get("factor2", (1, 10))
        commutative = settings.get("commutative", False)
        
        if commutative and random.random() < 0.5:
            summand1_range, summand2_range = summand2_range, summand1_range
        
        for _ in range(amount):
            factor1 = random.randint(*factor1_range)
            factor2 = random.randint(*factor2_range)
            product = factor1 * factor2
            
            if random.random() < 0.5:
                task = f"{factor1} \\cdot \\_\\_\\_ = {product}\n"
            else:
                task = f"\\_\\_\\_ \\cdot {factor2} = {product}\n"
            
            tasks.append(task)
            
        return tasks