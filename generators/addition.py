import random

class Addition():
    def generate_task(settings):
        lines = []
        
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        
        for _ in range(amount):
            summand1 = random.randint(*range1)
            summand2 = random.randint(*range2)
            
            task = f"{summand1} + {summand2} ="
            lines.append(task)
            
        return lines


    def generate_with_missing_element(settings):
        lines = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))

        for _ in range(amount):
            summand1 = random.randint(*range1)
            summand2 = random.randint(*range2)
            sum = summand1 + summand2

            if random.random() < 0.5:
                task = f"{summand1} + \\_\\_\\_ = {sum}"
            else:
                task = f"\\_\\_\\_ + {summand2} = {sum}"

            lines.append(task)

        return lines
    