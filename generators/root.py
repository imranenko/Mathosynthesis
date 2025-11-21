import random

class Root():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("base", (1, 10))
        range2 = settings.get("exponent", (2, 4))
        
        for _ in range(amount):
            root = random.randint(*range1)
            degree = random.randint(*range2)
            radicant = root**degree

            task = f"\sqrt[{degree}]{{{radicant}}} = "
            tasks.append(task)
                
        return tasks