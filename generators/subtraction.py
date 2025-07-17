import random

class Subtraction():

    def generate_task(range1=(100, 999), range2=(100, 999), only_pos=False):
        nummend = random.randint(*range1)
        subtrahend = random.randint(*range2)
        
        if only_pos and nummend < subtrahend:
            nummend, subtrahend = subtrahend, nummend
            
        return f"$${nummend} - {subtrahend} = $$\n"

    def generate_with_missing_element(range1=(100, 999), range2=(100, 999), only_pos=False):
        nummend = random.randint(*range1)
        subtrahend = random.randint(*range2)
        
        if only_pos and nummend - subtrahend:
            nummend, subtrahend = subtrahend, nummend
        difference = nummend - subtrahend
        
        if random.random() < 0.5:
            task = f"$${nummend} - \_\_\_ = {str(difference)*2}$$\n"
        else:
            task = f"$$\_\_\_ - {subtrahend} = {difference}$$\n"
        return task
