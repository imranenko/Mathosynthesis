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
            
            task = fr"{factor1} \cdot {factor2} =" + "\n"
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
                task = fr"{factor1} \cdot \_\_\_ = {product}"
            else:
                task = fr"\_\_\_ \cdot {factor2} = {product}"
            
            tasks.append(task)
            
        return tasks