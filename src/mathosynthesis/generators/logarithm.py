from typing import Any
from .generator import Generator
class Logarithm(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate logarithm tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - base: Range or choices for the logarithm base.
                - log: Range or choices for the logarithm exponent.

        Returns:
            List of logarithm tasks, e.g., "\\log_{2}\\num{16} =".
        """
        tasks = []
        amount = settings.get("amount", 1)
        base_cfg = settings.get("base", {"range": (1, 10)})
        log_cfg = settings.get("log", {"range": (2, 4)})
        
        base_list = Logarithm.generate_numbers(base_cfg, amount)
        log_list = Logarithm.generate_numbers(log_cfg, amount)
        
        for i in range(amount):
            base = base_list[i]
            log = log_list[i]
            anti_log = base**log
            
            task = fr"\log_{{{base}}}\num{{{anti_log}}} ="
            tasks.append(task)
        
        return tasks