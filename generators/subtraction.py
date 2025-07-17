import random

class Subtraction():

    def generate_task(range1=(100, 999), range2=(100, 999), only_pos=False):
        minuend = random.randint(*range1)
        subtrahend = random.randint(*range2)
        
        if only_pos and minuend < subtrahend:
            minuend, subtrahend = subtrahend, minuend
            
        return f"$${minuend} - {subtrahend} = $$\n"

    def generate_with_missing_element(range1=(100, 999), range2=(100, 999), only_pos=False):
        minuend = random.randint(*range1)
        subtrahend = random.randint(*range2)
        
        if only_pos and minuend - subtrahend:
            minuend, subtrahend = subtrahend, minuend
        difference = minuend - subtrahend
        
        if random.random() < 0.5:
            task = f"$${minuend} - \\_\\_\\_ = {str(difference)*2}$$\n"
        else:
            task = f"$$\\_\\_\\_ - {subtrahend} = {difference}$$\n"
        return task
