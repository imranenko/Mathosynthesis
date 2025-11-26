import random
from .generator import Generator

class Addition(Generator):
    @staticmethod
    def generate_task(settings):
        lines = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1", (1, 10))
        summand2_cfg = settings.get("summand2", (1, 10))
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for i in range(amount):
            summand1 = summand1_list[i]
            summand2 = summand2_list[i]
        
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
            
            task = f"{summand1} + {summand2} ="
            lines.append(task)
            
        return lines


    @staticmethod
    def generate_with_missing_element(settings):
        lines = []
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1", (1, 10))
        summand2_cfg = settings.get("summand2", (1, 10))
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for i in range(amount):
            summand1 = summand1_list[i]
            summand2 = summand2_list[i]
            sum = summand1 + summand2
        
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
            
            if random.random() < 0.5:
                task = f"{summand1} + \\_\\_\\_ = {sum}"
            else:
                task = f"\\_\\_\\_ + {summand2} = {sum}"

            lines.append(task)

        return lines
    