import random

class Division():  
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        divisor_range = settings.get("divisor", (1, 10))
        quotient_range = settings.get("quotient", (1, 10))
        
        for _ in range(amount):
            divisor = random.randint(*divisor_range)
            quotient = random.randint(*quotient_range)
            divident = quotient * divisor
            
            task = f"{divident} \\div {divisor} =\n"
                
            tasks.append(task)
                
        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        divisor_range = settings.get("divisor", (1, 10))
        quotient_range = settings.get("quotient", (1, 10))
        
        for _ in range(amount):
            divisor = random.randint(*divisor_range)
            quotient = random.randint(*quotient_range)
            divident = quotient * divisor

            if random.random() < 0.5:
                task = f"{divident} \\div \\_\\_\\_ = {quotient}\n"
            else:
                task = f"\\_\\_\\_ \\div {divisor} = {quotient}\n"
                
            tasks.append(task)
        
        return tasks
