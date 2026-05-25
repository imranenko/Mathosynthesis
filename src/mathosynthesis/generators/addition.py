import random
from typing import Any
from .generator import Generator

class Addition(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate addition tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks to generate.
                - summand1: Range or choices for the first summand.
                - summand2: Range or choices for the second summand.
                - commutative: Whether to randomly swap summands.

        Returns:
            List of addition task strings, e.g., "3 + 5 =".
        """
        lines = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1", {"range": (1, 10)})
        summand2_cfg = settings.get("summand2", {"range": (1, 10)})
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for i in range(amount):
            summand1 = summand1_list[i]
            summand2 = summand2_list[i]
        
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
            
            task = fr"\num{{{summand1}}} + \num{{{summand2}}} ="
            lines.append(task)
            
        return lines


    @staticmethod
    def generate_with_missing_element(settings: dict[str, Any]) -> list[str]:
        """
        Generate addition tasks with one missing element represented by blanks.

        Args:
            settings: Same as generate_task.

        Returns:
            List of addition tasks with a missing summand, e.g., "3 + ___ = 8".
        """
        lines = []
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1", {"range": (1, 10)})
        summand2_cfg = settings.get("summand2", {"range": (1, 10)})
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
                task = fr"\num{{{summand1}}} + \_\_\_ = \num{{{sum}}}"
            else:
                task = fr"\_\_\_ + \num{{{summand2}}} = \num{{{sum}}}"

            lines.append(task)

        return lines
    
    def generate_column_task(settings: dict[str, Any]) -> list[str]:
        lines = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1", {"range": (1, 10)})
        summand2_cfg = settings.get("summand2", {"range": (1, 10)})
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for i in range(amount):
            summand1 = summand1_list[i]
            summand2 = summand2_list[i]
        
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
                
            sum = summand1 + summand2
            
            task = fr"""\begin{{array}}{{r}}
\num{{{summand1}}} \\
+\num{{{summand2}}} \\
\hline
\phantom{{{sum}}}
\end{{array}}"""
            lines.append(task)
            
        return lines