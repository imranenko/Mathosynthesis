import random
from .generator import Generator

class Subtraction(Generator):
    @staticmethod
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        minuend_cfg = settings.get("minuend", (1, 10))
        subtrahend_cfg = settings.get("subrahend", (1, 10))
        only_pos = settings.get("only_pos", False)

        minuend_list = Subtraction.generate_numbers(minuend_cfg, amount)
        subtrahend_list = Subtraction.generate_numbers(subtrahend_cfg, amount)
        
        for i in range(amount):
            minuend = minuend_list[i]
            subtrahend = subtrahend_list[i]
            
            if only_pos and minuend < subtrahend:
                minuend, subtrahend = subtrahend, minuend
            
            tasks.append(f"{minuend} - {subtrahend} =")

        return tasks

    @staticmethod
    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        minuend_cfg = settings.get("minuend", (1, 10))
        subtrahend_cfg = settings.get("subrahend", (1, 10))
        only_pos = settings.get("only_pos", False)

        minuend_list = Subtraction.generate_numbers(minuend_cfg, amount)
        subtrahend_list = Subtraction.generate_numbers(subtrahend_cfg, amount)
        
        for i in range(amount):
            minuend = minuend_list[i]
            subtrahend = subtrahend_list[i]                
            
            if only_pos and minuend < subtrahend:
                minuend, subtrahend = subtrahend, minuend
                
            difference = minuend - subtrahend
            
            if random.random() < 0.5:
                task = f"{minuend} - \\_\\_\\_ = {str(difference)*2}"
            else:
                task = f"\\_\\_\\_ - {subtrahend} = {difference}"
                
            tasks.append(task)

        return tasks
