import random
from typing import Any
from textwrap import dedent
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
        tasks = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1")
        summand2_cfg = settings.get("summand2")
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for summand1, summand2 in zip(summand1_list, summand2_list):
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
            
            tasks.append(fr"\num{{{summand1}}} + \num{{{summand2}}} =")
            
        return tasks


    @staticmethod
    def generate_with_missing_element(settings: dict[str, Any]) -> list[str]:
        """
        Generate addition tasks with one missing element represented by blanks.

        Args:
            settings: Same as generate_task.

        Returns:
            List of addition tasks with a missing summand, e.g., "3 + ___ = 8".
        """
        tasks = []
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1")
        summand2_cfg = settings.get("summand2")
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for summand1, summand2 in zip(summand1_list, summand2_list):
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
                
            sum = summand1 + summand2
        
            if random.random() < 0.5:
                task = fr"\num{{{summand1}}} + \_\_\_ = \num{{{sum}}}"
            else:
                task = fr"\_\_\_ + \num{{{summand2}}} = \num{{{sum}}}"

            tasks.append(task)

        return tasks
    
    def generate_column_task(settings: dict[str, Any]) -> list[str]:
        tasks = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1")
        summand2_cfg = settings.get("summand2")
        commutative = settings.get("commutative", False)
        
        summand1_list = Addition.generate_numbers(summand1_cfg, amount)
        summand2_list = Addition.generate_numbers(summand2_cfg, amount)

        for summand1, summand2 in zip(summand1_list, summand2_list):       
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
                
            sum = summand1 + summand2
        
            task = dedent(fr"""
                \begin{{array}}{{r}}
                \num{{{summand1}}} \\
                +\num{{{summand2}}} \\
                \hline
                \phantom{{{sum}}}
                \end{{array}}
            """)
            tasks.append(task)
            
        return tasks
    
    @staticmethod
    def generate_with_decimal_numbers(settings: dict[str, Any]) -> list[str]:
        tasks = []
        
        amount = settings.get("amount", 1)
        summand1_cfg = settings.get("summand1")
        summand2_cfg = settings.get("summand2")
        commutative = settings.get("commutative", True)
        
        summand1_list = Generator.generate_scientific_notation_number(summand1_cfg, amount)
        summand2_list = Generator.generate_scientific_notation_number(summand2_cfg, amount)
        
        for summand1, summand2 in zip(summand1_list, summand2_list):
            if commutative and random.random() < 0.5:
                summand1, summand2 = summand2, summand1
                
            tasks.append(fr"\num{{{summand1}}}+\num{{{summand2}}}=")
        
        return tasks