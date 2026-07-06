import random
from typing import Any
from textwrap import dedent
from .generator import Generator

class Subtraction(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate subtraction tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - minuend: Range or choices for the minuend.
                - subtrahend: Range or choices for the subtrahend.
                - only_pos: If True, ensures result is not negative.

        Returns:
            List of subtraction tasks, e.g., "8 - 3 =".
        """
        tasks = []
        
        amount = settings.get("amount", 1)
        minuend_cfg = settings.get("minuend")
        subtrahend_cfg = settings.get("subtrahend")
        only_pos = settings.get("only_pos", False)

        minuend_list = Subtraction.generate_numbers(minuend_cfg, amount)
        subtrahend_list = Subtraction.generate_numbers(subtrahend_cfg, amount)
        
        for minuend, subtrahend in zip(minuend_list, subtrahend_list):
            if only_pos and minuend < subtrahend:
                minuend, subtrahend = subtrahend, minuend
            
            tasks.append(fr"\num{{{minuend}}} - \num{{{subtrahend}}} =")

        return tasks

    @staticmethod
    def generate_with_missing_element(settings: dict[str, Any]) -> list[str]:
        """
        Generate subtraction tasks with one missing element represented by blanks.

        Args:
            settings: Same as generate_task.

        Returns:
            List of subtraction tasks with a missing element, e.g., "8 - ___ = 5".
        """
        tasks = []
        
        amount = settings.get("amount", 1)
        minuend_cfg = settings.get("minuend")
        subtrahend_cfg = settings.get("subtrahend")
        only_pos = settings.get("only_pos", False)

        minuend_list = Subtraction.generate_numbers(minuend_cfg, amount)
        subtrahend_list = Subtraction.generate_numbers(subtrahend_cfg, amount)
        
        for minuend, subtrahend in zip(minuend_list, subtrahend_list):            
            if only_pos and minuend < subtrahend:
                minuend, subtrahend = subtrahend, minuend
                
            difference = minuend - subtrahend
            
            if random.random() < 0.5:
                task = fr"\num{{{minuend}}} - \_\_\_ = \num{{{difference}}}"
            else:
                task = fr"\_\_\_ - \num{{{subtrahend}}} = \num{{{difference}}}"
                
            tasks.append(task)

        return tasks

    @staticmethod
    def generate_column_task(settings: dict[str, Any]) -> list[str]:
            tasks = []
            
            amount = settings.get("amount", 1)
            minuend_cfg = settings.get("minuend")
            subtrahend_cfg = settings.get("subtrahend")
            only_pos = settings.get("only_pos", False)

            minuend_list = Subtraction.generate_numbers(minuend_cfg, amount)
            subtrahend_list = Subtraction.generate_numbers(subtrahend_cfg, amount)
            
            for minuend, subtrahend in zip(minuend_list, subtrahend_list):
                if only_pos and minuend < subtrahend:
                    minuend, subtrahend = subtrahend, minuend
                
                difference = minuend - subtrahend
                
                task = dedent(fr"""
                    \begin{{array}}{{r}}
                    \num{{{minuend}}} \\
                    -\num{{{subtrahend}}} \\
                    \hline
                    \phantom{{{difference}}}
                    \end{{array}}
                """)
                tasks.append(task)

            return tasks
    
    @staticmethod
    def generate_with_decimal_numbers(settings: dict[str, Any]) -> list[str]:
        tasks = []
        
        amount = settings.get("amount", 1)
        minuend_cfg = settings.get("minuend")
        subtrahend_cfg = settings.get("subtrahend")
        commutative = settings.get("commutative", True)
        
        minuend_list = Subtraction.generate_scientific_notation_number(minuend_cfg, amount)
        subtrahend_list = Subtraction.generate_scientific_notation_number(subtrahend_cfg, amount)
        
        for minuend, subtrahend in zip(minuend_list, subtrahend_list):
            if commutative and random.random() < 0.5:
                minuend, subtrahend = subtrahend, minuend
                
            tasks.append(fr"\num{{{minuend}}}-\num{{{subtrahend}}}=")