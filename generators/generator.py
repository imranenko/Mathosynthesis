import random
import logging
from typing import Any

logger = logging.getLogger(__name__)

class Generator():
    @staticmethod
    def generate_numbers(number_cfg: dict[str, Any], amount: int = 1) -> list[int]:
        """
        Generate a list of random numbers according to the configuration.

        Args:
            number_cfg: Configuration dictionary containing either:
                - 'range': tuple of (start, end) integers, and optional 'step'.
                - 'choices': list of possible values, with optional 'weights'.
            amount: Number of numbers to generate.

        Returns:
            List of generated integers.

        Raises:
            ValueError: If configuration format is invalid.
        """
        results = []
        
        if "range" in number_cfg:
            start, end = number_cfg["range"]
            step = number_cfg.get("step", 1)
            possible_values = list(range(start, end + 1, step))
            
            for _ in range(amount):
                results.append(random.choice(possible_values))

        elif "choices" in number_cfg:
            choices = number_cfg["choices"]
            weights_cfg = number_cfg.get("weights", {})
            weights = []
            
            for choice in choices:
                weights.append(weights_cfg.get(str(choice), 1))
            for _ in range(amount):
                results.append(random.choices(choices, weights=weights, k=1)[0])
        else:
            logger.error("Invalid JSON format")
            raise ValueError("Invalid JSON format")
    
        return results