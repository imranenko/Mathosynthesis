import random

class Addition():
    def generate_task(settings):
        lines = []
        
        amount = settings.get("amount", 1)
        summand1_range = settings.get("summand1", (1, 10))
        summand2_range = settings.get("summand2", (1, 10))
        commutative = settings.get("commutative", False)
        

        for _ in range(amount):
            if commutative and random.random() < 0.5:
                summand1_range, summand2_range = summand2_range, summand1_range
            
            summand1 = random.randint(*summand1_range)
            summand2 = random.randint(*summand2_range)
            
            task = f"{summand1} + {summand2} ="
            lines.append(task)
            
        return lines


    def generate_with_missing_element(settings):
        lines = []
        amount = settings.get("amount", 1)
        summand1_range = settings.get("summand1", (1, 10))
        summand2_range = settings.get("summand2", (1, 10))
        commutative = settings.get("commutative", False)
        
        if commutative and random.random() < 0.5:
            summand1_range, summand2_range = summand2_range, summand1_range

        for _ in range(amount):
            summand1 = random.randint(*summand1_range)
            summand2 = random.randint(*summand2_range)
            sum = summand1 + summand2

            if random.random() < 0.5:
                task = f"{summand1} + \\_\\_\\_ = {sum}"
            else:
                task = f"\\_\\_\\_ + {summand2} = {sum}"

            lines.append(task)

        return lines
    