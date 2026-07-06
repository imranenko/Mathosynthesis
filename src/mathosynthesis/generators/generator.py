import random
import logging
from typing import Any

logger = logging.getLogger(__name__)

class Generator():
    @staticmethod
    def generate_possible_values(number_cfg: dict[str, Any]) -> tuple[list[int], list[int] | None]:
        if "range" in number_cfg:
            start, end = number_cfg["range"]
            step = number_cfg.get("step", 1)
            choices = list(range(start, end + 1, step))
            return choices, None
        
        elif "choices" in number_cfg:
            choices = number_cfg["choices"]
            weights = number_cfg.get("weights")
            return choices, weights
        
        else:
            logger.error("Invalid JSON format")
            raise ValueError("Invalid JSON format")


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
        possible_values, weights = Generator.generate_possible_values(number_cfg)
        numbers = random.choices(possible_values, weights=weights, k=amount)
        return numbers
    
    @staticmethod
    def generate_fractions(fraction_cfg: dict[str, Any], amount: int = 1):
        fractions = []
        
        numerator_cfg = fraction_cfg.get("numerator")
        denominator_cfg = fraction_cfg.get("denominator")
        denominator_coefficient_cfg = fraction_cfg.get("denominator_coefficient", {"choices": [1]})
        
        if numerator_cfg and denominator_cfg:
            denominator_list = Generator.generate_numbers(denominator_cfg, amount)
            denominator_coefficient_list = Generator.generate_numbers(denominator_coefficient_cfg, amount)
            
            numerator_list = Generator.generate_numbers(numerator_cfg, amount)
            denominator_list = [den * coeff for den, coeff in zip(denominator_list, denominator_coefficient_list)]

        elif numerator_cfg:
            denominator_coefficient_list = Generator.generate_numbers(denominator_coefficient_cfg, amount)
            
            numerator_list = Generator.generate_numbers(numerator_cfg, amount)
            denominator_list = [random.randint(1, numerator - 1) * coeff for numerator, coeff in zip(numerator_list, denominator_coefficient_list)]

        elif denominator_cfg:
            denominator_list = Generator.generate_numbers(denominator_cfg, amount)
            denominator_coefficient_list = Generator.generate_numbers(denominator_coefficient_cfg, amount)
            
            numerator_list = [random.randint(1, denominator - 1) for denominator in denominator_list]
            denominator_list = [den * coeff for den, coeff in zip(denominator_list, denominator_coefficient_list)]
        
        else:
            raise ValueError("Invalid JSON format")
        
        # if simplified_fractions:
        #         possible_numerators1 = list(filter(lambda x: math.gcd(x, denominator1) == 1, range(1, denominator1)))
        #         numerator1 = random.choice(possible_numerators1)
        # else:
        #     numerator1 = random.randint(1, denominator1 - 1)
        
        for numerator, denominator in zip(numerator_list, denominator_list):
            fractions.append(fr"\frac{{{numerator}}}{{\num{{{denominator}}}}}")
        
        return fractions
    

    @staticmethod
    def generate_scientific_notation_number(scientific_notation_number_cfg: dict[str, Any], amount: int):
        scientific_notation_numbers = []
        
        significand_cfg = scientific_notation_number_cfg.get("significand")
        exponent_cfg = scientific_notation_number_cfg.get("exponent")
        
        significand_list = Generator.generate_numbers(significand_cfg)
        exponent_list = Generator.generate_numbers(exponent_cfg)
        
        for significand, exponent in zip(significand_list, exponent_list):
            scientific_notation_numbers.append(fr"{significand * 10**exponent}")
            
        return scientific_notation_numbers
        
        
    @staticmethod
    def generate_monomials(monomial_cfg: dict[str, Any], amount: int = 1):
        monomials = []
        
        coefficient_cfg = monomial_cfg.get("coefficient")
        exponent_cfg = monomial_cfg.get("exponent")
        possible_base_symbols = monomial_cfg.get("possible_base_symbols", ["x"])
        
        coefficient_list = Generator.generate_numbers(coefficient_cfg, amount)
        exponent_list = Generator.generate_numbers(exponent_cfg, amount)
        base_symbol_list = random.choices(possible_base_symbols, amount)
        
        for coefficient, exponent, base_symbol in zip(coefficient_list, exponent_list, base_symbol_list):            
            monomials.append(fr"\num{{{coefficient}}}{base_symbol}^{{{exponent}}}")

        return monomials
