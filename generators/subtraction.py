import random

class Subtraction():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        minuend_range = settings.get("minuend", (1, 10))
        subtrahend_range = settings.get("subrahend", (1, 10))
        only_pos = settings.get("only_pos", False)

        for _ in range(amount):
            if only_pos: # Will it be trully random distribution?
                minuend = random.randint(*minuend_range)
                subtrahend = random.randint(subtrahend_range[0], minuend-1)
            else:
                minuend = random.randint(*minuend_range)
                subtrahend = random.randint(*subtrahend_range)
            
            tasks.append(f"{minuend} - {subtrahend} = \n")

        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        minuend_range = settings.get("minuend", (1, 10))
        subtrahend_range = settings.get("subrahend", (1, 10))
        only_pos = settings.get("only_pos", False)
        
        for _ in range(amount):
            if only_pos: # Will it be trully random distribution?
                minuend = random.randint(*minuend_range)
                subtrahend = random.randint(subtrahend_range[0], minuend-1)
            else:
                minuend = random.randint(*minuend_range)
                subtrahend = random.randint(*subtrahend_range)
                
            difference = minuend - subtrahend
            
            if random.random() < 0.5:
                task = f"{minuend} - \\_\\_\\_ = {str(difference)*2}\n"
            else:
                task = f"\\_\\_\\_ - {subtrahend} = {difference}\n"
                
            tasks.append(task)

        return tasks
