import random
from typing import Any
from .generator import Generator

class Division(Generator):  
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate division tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks to generate.
                - dividend: Range or choices for the dividend.
                - divisor: Range or choices for the divisor.
                - quotient: Range or choices for the quotient.

        Returns:
            List of division task strings, e.g., "20 \\div 5 =".
        """
        tasks = []
        amount = settings.get("amount", 1)
        dividend_cfg = settings.get("dividend")
        divisor_cfg = settings.get("divisor")
        quotient_cfg = settings.get("quotient")
        
        if dividend_cfg and divisor_cfg:
            dividend_list = Division.generate_numbers(dividend_cfg, amount)
            divisor_list = Division.generate_numbers(divisor_cfg, amount)
        elif divisor_cfg and quotient_cfg:
            divisor_list = Division.generate_numbers(divisor_cfg, amount)
            quotient_list = Division.generate_numbers(quotient_cfg, amount)
            dividend_list = [quotient * divisor for quotient, divisor in zip(quotient_list, divisor_list)]
        else:
            raise ValueError("Invalid JSON format")
                
        for i in range(amount):
            divisor = divisor_list[i]
            dividend = dividend_list[i]
            
            task = fr"\num{{{dividend}}} \div \num{{{divisor}}} ="
            tasks.append(task)
                
        return tasks

    @staticmethod
    def generate_with_missing_element(settings: dict[str, Any]) -> list[str]:
        """
        Generate division tasks with one missing element represented by blanks.

        Args:
            settings: Same as generate_task.

        Returns:
            List of division tasks with a missing divisor or dividend, e.g., "20 \\div ___ = 4".
        """
        tasks = []
        amount = settings.get("amount", 1)
        divisor_cfg = settings.get("divisor", {"range": (1, 10)})
        quotient_cfg = settings.get("quotient", {"range": (1, 10)})
        
        divisor_list = Division.generate_numbers(divisor_cfg, amount)
        quotient_list = Division.generate_numbers(quotient_cfg, amount)
        
        for i in range(amount):
            divisor = divisor_list[i]
            quotient = quotient_list[i]
            divident = quotient * divisor

            if random.random() < 0.5:
                task = fr"\num{{{divident}}} \div \_\_\_ = \num{{{quotient}}}"
            else:
                task = fr"\_\_\_ \div \num{{{divisor}}} = \num{{{quotient}}}"
                
            tasks.append(task)
        
        return tasks
