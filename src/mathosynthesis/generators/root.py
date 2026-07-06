from typing import Any
from .generator import Generator

class Root(Generator):
    @staticmethod
    def generate_task(settings: dict[str, Any]) -> list[str]:
        """
        Generate root extraction tasks as strings.

        Args:
            settings: Configuration dictionary containing:
                - amount: Number of tasks.
                - root: Range or choices for the radicand.
                - index: Range or choices for the root index.

        Returns:
            List of root extraction tasks, e.g., "\\sqrt{16} =", "\\sqrt[3]{27} =".
        """
        tasks = []
        
        amount = settings.get("amount", 1)
        root_cfg = settings.get("root")
        index_cfg = settings.get("index")
        
        root_list = Root.generate_numbers(root_cfg, amount)
        index_list = Root.generate_numbers(index_cfg, amount)
        
        for root, index in zip(root_list, index_list):
            radicant = root**index

            if index == 2:
                task = fr"\sqrt{{\num{{{radicant}}}}} ="
            else:
                task = fr"\sqrt[{index}]{{\num{{{radicant}}}}} ="
                
            tasks.append(task)
                
        return tasks