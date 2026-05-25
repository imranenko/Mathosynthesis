import random
from typing import Any
from .generator import Generator

class Multiplication(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate multiplication tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - factor1: Range or choices for first factor.
                - factor2: Range or choices for second factor.
                - commutative: Whether to randomly swap factors.

        Returns:
            List of multiplication tasks, e.g., "3 \\cdot 5 =".
        """
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", {"range": (1, 10)})
        factor2_cfg = settings.get("factor2", {"range": (1, 10)})
        commutative = settings.get("commutative", False)
        
        factor1_list = Multiplication.generate_numbers(factor1_cfg, amount)
        factor2_list = Multiplication.generate_numbers(factor2_cfg, amount)
        
        for i in range(amount):
            factor1 = factor1_list[i]
            factor2 = factor2_list[i]
            
            if commutative and random.random() < 0.5:
                factor1, factor2 = factor2, factor1
            
            task = fr"\num{{{factor1}}} \cdot \num{{{factor2}}} ="
            tasks.append(task)
        
        return tasks


    @staticmethod
    def generate_task_with_round_numbers(settings: dict[str, Any]) -> list[str]:
        """
        Generate multiplication tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - factor1: Range or choices for first factor.
                - factor2: Range or choices for second factor.
                - ten_power1: Range or choices for first power of 10.
                - ten_power2: Range or choices for second power of 10.
                - commutative: Whether to randomly swap factors.

        Returns:
            List of multiplication tasks, e.g., "30 \\cdot 500 =".
        """
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", {"range": (1, 10)})
        factor2_cfg = settings.get("factor2", {"range": (1, 10)})
        ten_power1_cfg = settings.get("ten_power1", {"range": (1, 3)})
        ten_power2_cfg = settings.get("ten_power2", {"range": (1, 3)})
        commutative = settings.get("commutative", False)
        
        factor1_list = Multiplication.generate_numbers(factor1_cfg, amount)
        factor2_list = Multiplication.generate_numbers(factor2_cfg, amount)
        ten_power1_list = Multiplication.generate_numbers(ten_power1_cfg, amount)
        ten_power2_list = Multiplication.generate_numbers(ten_power2_cfg, amount)
        
        for i in range(amount):
            factor1 = factor1_list[i]
            factor2 = factor2_list[i]
            ten_power1 = ten_power1_list[i]
            ten_power2 = ten_power2_list[i]
            
            if commutative and random.random() < 0.5:
                factor1, factor2 = factor2, factor1
                ten_power1, ten_power2 = ten_power2, ten_power1
            
            task = fr"\num{{{factor1 * 10**ten_power1}}} \cdot \num{{{factor2 * 10**ten_power2}}} ="
            tasks.append(task)
        
        return tasks

    @staticmethod
    def generate_with_missing_element(settings: dict[str, Any]) -> list[str]:
        """
        Generate multiplication tasks with one missing element represented by blanks.

        Args:
            settings: Same as generate_task.

        Returns:
            List of multiplication tasks with a missing factor, e.g., "3 \\cdot ___ = 15".
        """
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", {"range": (1, 10)})
        factor2_cfg = settings.get("factor2", {"range": (1, 10)})
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
                task = fr"\num{factor1} \cdot \_\_\_ = \num{{{product}}}"
            else:
                task = fr"\_\_\_ \cdot \num{{{factor2}}} = \num{{{product}}}"
            
            tasks.append(task)
            
        return tasks
    
    def generate_column_task(settings: dict[str, Any]) -> list[str]:
        tasks = []
        amount = settings.get("amount", 1)
        factor1_cfg = settings.get("factor1", {"range": (1, 10)})
        factor2_cfg = settings.get("factor2", {"range": (1, 10)})
        commutative = settings.get("commutative", False)
        
        factor1_list = Multiplication.generate_numbers(factor1_cfg, amount)
        factor2_list = Multiplication.generate_numbers(factor2_cfg, amount)
        
        for i in range(amount):
            factor1 = factor1_list[i]
            factor2 = factor2_list[i]
            
            if commutative and random.random() < 0.5:
                factor1, factor2 = factor2, factor1
                
            product = factor1 * factor2
            
            task = task = fr"""\begin{{array}}{{r}}
\num{{{factor1}}} \\
\times\num{{{factor2}}} \\
\hline
\phantom{{{product}}}
\end{{array}}"""
            tasks.append(task)
        
        return tasks