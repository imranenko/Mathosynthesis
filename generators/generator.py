import random
import logging

logger = logging.getLogger(__name__)

class Generator():
    @staticmethod
    def generate_numbers(number_cfg, amount=1):
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