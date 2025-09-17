import random

class Subtraction():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        only_pos = settings.get("only_pos", True)

        for _ in range(amount):
        
            minuend = random.randint(*range1)
            subtrahend = random.randint(*range2)
        
            if only_pos and minuend < subtrahend:
                minuend, subtrahend = subtrahend, minuend
            
            tasks.append(f"${minuend} - {subtrahend} = $\n")

        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        only_pos = settings.get("only_pos", True)
        
        for _ in range(amount):
            
            minuend = random.randint(*range1)
            subtrahend = random.randint(*range2)
            
            if only_pos and minuend - subtrahend:
                minuend, subtrahend = subtrahend, minuend
                
            difference = minuend - subtrahend
            
            if random.random() < 0.5:
                task = f"{minuend} - \\_\\_\\_ = {str(difference)*2}\n"
            else:
                task = f"\\_\\_\\_ - {subtrahend} = {difference}\n"
                
            tasks.append(task)

        return tasks
