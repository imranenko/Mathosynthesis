import random

class Subtraction():

    def generate_task(range1=(100, 999), range2=(100, 999), only_pos=False):
        num1 = random.randint(*range1)
        num2 = random.randint(*range2)
        
        if only_pos and num1 < num2:
            num1, num2 = num2, num1
            
        return f"$${num1} - {num2} = $$\n"

    def generate_with_missing_element(range1=(100, 999), range2=(100, 999), only_pos=False):
        num1 = random.randint(*range1)
        num2 = random.randint(*range2)
        
        if only_pos and num1 - num2:
            num1, num2 = num2, num1
        difference = num1 - num2
        
        if random.random() < 0.5:
            task = f"$${num1} - \_\_\_ = {str(difference)*2}$$\n"
        else:
            task = f"$$\_\_\_ - {num2} = {difference}$$\n"
        return task
