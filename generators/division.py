import random

class Division():
    
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        
        for _ in range(amount):
            num1 = random.randint(*range1)
            num2 = random.randint(*range2)
            product = num1 * num2
            
            if random.random() < 0.5:
                task = f"$${product} \\div {num1} = $$\n"
            else:
                task = f"$${product} \\div {num2} = $$\n"
                
            tasks.append(task)
                
        return tasks

    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        range1 = settings.get("range1", (1, 10))
        range2 = settings.get("range2", (1, 10))
        
        for _ in range(amount):
            num1 = random.randint(*range1)
            num2 = random.randint(*range2)
            product = num1 * num2

            if random.random() < 0.5:
                task = f"$${product} \\div \\_\\_\\_ = {num1}$$\n"
            else:
                task = f"$$\\_\\_\\_ \\div {num2} = {num1}$$\n"
                
        tasks.append(task)
        
        return tasks


if __name__ == "__main__":
    for i in range(10):
        print(Division.generate_with_missing_element())