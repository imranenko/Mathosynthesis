from generator import Generator
from typing import Any
import random

class Algebra(Generator):
    @staticmethod
    def generate_linear_equation(settings: dict[str, Any]) -> list[str]:
        """
        Generate a list of linear equations according to the given configuration.

        Args:
            settings: Configuration dictionary containing:
                - "amount": Number of equations to generate. Defaults to 1.
                - "k": Configuration for generating the coefficient of x.
                - "c": Configuration for generating the constant term.
                - "possible_base_symbols": Optional list of symbols to use as the
                variable. Defaults to ["x"].

        Returns:
            A list of linear equations formatted as LaTeX strings.
        """
        tasks = []

        amount = settings.get("amount", 1)
        k_cfg = settings.get("k")
        c_cfg = settings.get("c")
        base_symbol_cfg = settings.get("possible_base_symbols", ["x"])

        k_list = Algebra.generate_numbers(k_cfg, amount)
        c_list = Algebra.generate_numbers(c_cfg, amount)
        base_symbol_list = random.choices(base_symbol_cfg, k=amount)

        for k, c, base_symbol in zip(k_list, c_list, base_symbol_list):
            tasks.append(fr"{k}{base_symbol} + {c} = 0")

        return tasks
        
    @staticmethod
    def generate_quadratic_equation(settings: dict[str, Any]) -> list[str]:
        task = []
        
        amount = settings.get("amount", 1)
        a_cfg = settings.get("a", {"choices": [1]})
        b_cfg = settings.get("b")
        c_cfg = settings.get("c")
        base_symbol_cfg = settings.get("possible_base_symbols", ["x"])
        
        a_list = Algebra.generate_numbers(a_cfg, amount)
        b_list = Algebra.generate_numbers(b_cfg, amount)
        c_list = Algebra.generate_numbers(c_cfg, amount)
        base_symbol_list = random.choices(base_symbol_cfg, amount)
        
        for a, b, c, base_symbol in zip(a_list, b_list, c_list, base_symbol_list):
            task.append(fr"{a}{base_symbol}^2{"+" + b if b >= 0 else b}{"+" + c if c >= 0 else c} = 0")
        
        
        