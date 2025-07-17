import random

class Addition():
    
    def generate_task(range1=(1, 10), range2=(1, 10)):
        summand1 = random.randint(*range1)
        summand2 = random.randint(*range2)
        
        return f"$${summand1} + {summand2} = $$\n"

    def generate_with_missing_element(range1=(1, 10), range2=(1, 10)):
        summand1 = random.randint(*range1)
        summand2 = random.randint(*range2)
        sum = summand1 + summand2
        
        if random.random() < 0.5:
            task = f"$${summand1} + \_\_\_ = {str(sum)*2}$$\n"
        else:
            task = f"$$\_\_\_ + {summand2} = {sum}$$\n"
        return task