import random
from .generator import Generator

class Multiplication(Generator):
    @staticmethod
    def generate_task(settings: dict) -> list[str]:
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", (1, 10))
        factor2_cfg = settings.get("factor2", (1, 10))
        commutative = settings.get("commutative", False)
        
        factor1_list = Multiplication.generate_numbers(factor1_cfg, amount)
        factor2_list = Multiplication.generate_numbers(factor2_cfg, amount)
        
        for i in range(amount):
            factor1 = factor1_list[i]
            factor2 = factor2_list[i]
            
            if commutative and random.random() < 0.5:
                factor1, factor2 = factor2, factor1
            
            task = f"{factor1} \\cdot {factor2} =\n"
            tasks.append(task)
        
        return tasks

    @staticmethod
    def generate_with_missing_element(settings: dict) -> list[str]:
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", (1, 10))
        factor2_cfg = settings.get("factor2", (1, 10))
        commutative = settings.get("commutative", False)
        
        factor1_list = Multiplication.generate_numbers(factor1_cfg, amount)
        factor2_list = Multiplication.generate_numbers(factor2_cfg, amount)
        
        for i in range(amount):
            factor1 = factor1_list[i]
            factor2 = factor2_list[i]
            product = factor1 * factor2
            
            if commutative and random.random() < 0.5:
                factor1, factor2 = factor2, factor1
            
            if random.random() < 0.5:
                task = f"{factor1} \\cdot \\_\\_\\_ = {product}"
            else:
                task = f"\\_\\_\\_ \\cdot {factor2} = {product}"
            
            tasks.append(task)
            
        return tasks