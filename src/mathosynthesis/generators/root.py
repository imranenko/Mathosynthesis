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
        root_cfg = settings.get("root", {"range": (2, 9)})
        index_cfg = settings.get("index", {"range": (2, 2)})
        
        root_list = Root.generate_numbers(root_cfg, amount)
        index_list = Root.generate_numbers(index_cfg, amount)
        
        for i in range(amount):
            root = root_list[i]
            index = index_list[i]
            radicant = root**index

            if index == 2:
                task = fr"\sqrt{{{radicant}}} ="
            else:
                task = fr"\sqrt[{index}]{{{radicant}}} ="
                
            tasks.append(task)
                
        return tasks