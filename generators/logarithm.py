import random
from math import sqrt

class Logarithm():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        base_range = settings.get("base", (1, 10))
        log_range = settings.get("log", (2, 4))
        
        for _ in range(amount):
            base = random.randint(*base_range)
            log = random.randint(*log_range)
            anti_log = base**log
            
            task = f"\log_{{{base}}}\\num{{{anti_log}}} =\n"
            tasks.append(task)
        
        return tasks