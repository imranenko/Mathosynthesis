import random

class Exponantiation():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("base", (1, 10))
        range2 = settings.get("exponent", (2, 4))
        
        for _ in range(amount):
            base = random.randint(*range1)
            exponent = random.randint(*range2)
            
            task = f"{base}^{{{exponent}}} = \n"
            tasks.append(task)
        
        return tasks