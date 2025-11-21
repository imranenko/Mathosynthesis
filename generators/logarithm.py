import random
from math import sqrt

class Logarithm():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("base", (1, 10))
        range2 = settings.get("exponent", (2, 4))
        
        for _ in range(amount):
            base = random.randint(*range1)
            log = random.randint(*range2)
            anti_log = base**log
            
            task = f"\log_{{{base}}}{{{anti_log}}}\n"
            tasks.append(task)
        
        return tasks