from typing import Any
from .generator import Generator

class Exponantiation(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate exponentiation tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - base: Range or choices for the base.
                - exponent: Range or choices for the exponent.

        Returns:
            List of exponentiation tasks, e.g., "3^{4} =".
        """
        tasks = []
        
        amount = settings.get("amount", 1)
        base_cfg = settings.get("base")
        exponent_cfg = settings.get("exponent")

        base_list = Exponantiation.generate_numbers(base_cfg, amount)
        exponent_list = Exponantiation.generate_numbers(exponent_cfg, amount)
        
        for base, exponent in zip(base_list, exponent_list):
            tasks.append(fr"\num{{{base}}}^{{{exponent}}} =")
        
        return tasks