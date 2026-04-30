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
        multiplier_cfg = settings.get("multiplier", {"choices": [1]})
        simplified_fractions = settings.get("simplified_fractions", False)
        same_denominator = settings.get("same_denominator", False)
        
        denominator_cfg = settings.get("denominator", {"range": (2, 10)})
        denominator1_list = Generator.generate_numbers(denominator_cfg, amount)
        multiplier_list = Generator.generate_numbers(multiplier_cfg, amount)
        if same_denominator:
            denominator2_list = [denominator1 * multiplier for denominator1, multiplier in zip(denominator1_list, multiplier_list)]
        else:
            denominator2_list = Generator.generate_numbers(denominator_cfg, amount)
            denominator2_list = [denominator2 * multiplier for denominator2, multiplier in zip(denominator2_list, multiplier_list)]
        
        for i in range(amount):
            denominator1 = denominator1_list[i]
            denominator2 = denominator2_list[i]
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