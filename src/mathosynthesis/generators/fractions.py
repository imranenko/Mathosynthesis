import random
import logging
import math
from typing import Any
from .generator import Generator

logger = logging.getLogger(__name__)

class Fractions(Generator):
    @staticmethod
    def generate_task_with_addition(settings: dict[str, Any]) -> list[str]:
        tasks = []

        amount = settings.get("amount", 1)   
        multiplier_cfg = settings.get("multiplier")
        denominator_cfg = settings.get("denominator")
        same_denominator = settings.get("same_denominator")
        simplified_fractions = settings.get("simplified_fractions")
        
        denominator1_list = Generator.generate_numbers(denominator_cfg, amount)
        multiplier_list = Generator.generate_numbers(multiplier_cfg, amount)
        
        if same_denominator:
            denominator2_list = [denominator1 * multiplier for denominator1, multiplier in zip(denominator1_list, multiplier_list)]
        else:
            denominator2_list = Generator.generate_numbers(denominator_cfg, amount)
        
        for denominator1, denominator2 in zip(denominator1_list, denominator2_list):
            if random.random() < 0.5:
                denominator1, denominator2 = denominator2, denominator1

            if simplified_fractions:
                possible_numerators1 = list(filter(lambda x: math.gcd(x, denominator1) == 1, range(1, denominator1)))
                possible_numerators2 = list(filter(lambda x: math.gcd(x, denominator2) == 1, range(1, denominator2)))
                numerator1 = random.choice(possible_numerators1)
                numerator2 = random.choice(possible_numerators2)
            else:
                numerator1 = random.randint(1, denominator1 - 1)
                numerator2 = random.randint(1, denominator2 - 1)

            tasks.append(fr"\frac{{\num{{{numerator1}}}}}{{\num{{{denominator1}}}}} + \frac{{\num{{{numerator2}}}}}{{\num{{{denominator2}}}}} =")
        return tasks
    
    @staticmethod
    def generate_tasks_with_simplification(settings: dict[str, Any]) -> list[str]:
        tasks = []

        amount = settings.get("amount", 1)
        denominator_cfg = settings.get("denominator")
        coefficient_cfg = settings.get("coefficient")
        
        denominator_list = Generator.generate_numbers(denominator_cfg, amount)
        numerator_list = [random.randint(1, denominator - 1) for denominator in denominator_list]
        coefficient_list = Generator.generate_numbers(coefficient_cfg, amount)
        
        for coefficient, denominator, numerator in zip(coefficient_list, denominator_list, numerator_list):
            denominator *= coefficient
            numerator *= coefficient
            
            tasks.append(fr"\frac{{\num{{{numerator}}}}}{{\num{{{denominator}}}}} =")
        
        return tasks
    
    @staticmethod
    def generate_tasks_improper_to_mixed(settings: dict[str, Any]) -> list[str]:
        tasks = []

        amount = settings.get("amount", 1)
        numerator_cfg = settings.get("numerator")
        simplified_fractions = settings.get("simplified_fractions", False)
        
        numerator_list = Generator.generate_numbers(numerator_cfg, amount)
        
        for numerator in numerator_list:
            if simplified_fractions:
                possible_denominators = list(filter(lambda x: math.gcd(x, numerator) == 1, range(1, numerator)))
                denominator = random.choice(possible_denominators)
            else:
                denominator = random.randint(1, numerator - 1)
            
            tasks.append(fr"\frac{{\num{{{numerator}}}}}{{\num{{{denominator}}}}} =")
        
        return tasks
    
    @staticmethod
    def generate_task_mixed_to_improper(settings: dict[str, Any]) -> list[str]:
        tasks = []
        
        amount = settings.get("amount", 1)
        whole_number_cfg = settings.get("whole")
        denominator_cfg = settings.get("denominator")
        simplified_fractions = settings.get("simplified_fractions", False)
        
        whole_number_list = Generator.generate_numbers(whole_number_cfg, amount)
        denominator_list = Generator.generate_numbers(denominator_cfg, amount)
        
        for whole_number, denominator in zip(whole_number_list, denominator_list):
            if simplified_fractions:
                possible_numerators = list(filter(lambda x: math.gcd(x, denominator) == 1, range(1, denominator)))
                numerator = random.choice(possible_numerators)
            else:
                numerator = random.randint(1, denominator - 1)

            tasks.append(fr"\num{{{whole_number}}} \frac{{\num{{{numerator}}}}}{{\num{{{denominator}}}}} =")
        
        return tasks