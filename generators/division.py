import random
from .generator import Generator

class Division(Generator):  
    @staticmethod
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        divisor_cfg = settings.get("divisor", (1, 10))
        quotient_cfg = settings.get("quotient", (1, 10))
        
        divisor_list = Division.generate_numbers(divisor_cfg, amount)
        quotient_list = Division.generate_numbers(quotient_cfg, amount)
        
        for i in range(amount):
            divisor = divisor_list[i]
            quotient = quotient_list[i]
            divident = quotient * divisor
            
            task = f"{divident} \\div {divisor} ="
            tasks.append(task)
                
        return tasks

    @staticmethod
    def generate_with_missing_element(settings):
        tasks = []
        amount = settings.get("amount", 1)
        divisor_cfg = settings.get("divisor", (1, 10))
        quotient_cfg = settings.get("quotient", (1, 10))
        
        divisor_list = Division.generate_numbers(divisor_cfg, amount)
        quotient_list = Division.generate_numbers(quotient_cfg, amount)
        
        for i in range(amount):
            divisor = divisor_list[i]
            quotient = quotient_list[i]
            divident = quotient * divisor

            if random.random() < 0.5:
                task = f"{divident} \\div \\_\\_\\_ = {quotient}"
            else:
                task = f"\\_\\_\\_ \\div {divisor} = {quotient}"
                
            tasks.append(task)
        
        return tasks
