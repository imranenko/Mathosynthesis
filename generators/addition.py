import random

class Addition():
    
    def generate_task(range1=(1, 10), range2=(1, 10)):
        num1 = random.randint(*range1)
        num2 = random.randint(*range2)
        
        return f"$${num1} + {num2} = $$\n"

    def generate_with_missing_element(range1=(1, 10), range2=(1, 10)):
        num1 = random.randint(*range1)
        num2 = random.randint(*range2)
        sum = num1 + num2
        
        if random.random() < 0.5:
            task = f"$${num1} + \_\_\_ = {str(sum)*2}$$\n"
        else:
            task = f"$$\_\_\_ + {num2} = {sum}$$\n"
        return task