from .generator import Generator

class Exponantiation(Generator):
    @staticmethod
    def generate_task(settings):
        tasks = []
        amount = settings.get("amount", 1)
        base_cfg = settings.get("base", (1, 10))
        exponent_cfg = settings.get("exponent", (2, 4))

        base_list = Exponantiation.generate_numbers(base_cfg, amount)
        exponent_list = Exponantiation.generate_numbers(exponent_cfg, amount)
        
        for i in range(amount):
            base = base_list[i]
            exponent = exponent_list[i]
            
            task = f"{base}^{{{exponent}}} ="
            tasks.append(task)
        
        return tasks