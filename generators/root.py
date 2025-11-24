import random

class Root():
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        root_range = settings.get("root", (2, 9))
        index_range = settings.get("index", (2, 2))
        
        for _ in range(amount):
            root = random.randint(*root_range)
            index = random.randint(*index_range)
            radicant = root**index

            if index == 2:
                task = f"\sqrt{{{radicant}}} = "
            else:
                task = f"\sqrt[{index}]{{{radicant}}} = "
            tasks.append(task)
                
        return tasks