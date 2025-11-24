import random

class Exponantiation():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        base_range = settings.get("base", (1, 10))
        exponent_range = settings.get("exponent", (2, 4))
        
        for _ in range(amount):
            base = random.randint(*base_range)
            exponent = random.randint(*exponent_range)
            
            task = f"{base}^{{{exponent}}} = \n"
            tasks.append(task)
        
        return tasks