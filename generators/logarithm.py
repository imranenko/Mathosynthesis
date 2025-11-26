from .generator import Generator
class Logarithm(Generator):
    @staticmethod
    def generate_task(settings: dict) -> list[str]:
        tasks = []
        amount = settings.get("amount", 1)
        base_cfg = settings.get("base", (1, 10))
        log_cfg = settings.get("log", (2, 4))
        
        base_list = Logarithm.generate_numbers(base_cfg, amount)
        log_list = Logarithm.generate_numbers(log_cfg, amount)
        
        for i in range(amount):
            base = base_list[i]
            log = log_list[i]
            anti_log = base**log
            
            task = f"\log_{{{base}}}\\num{{{anti_log}}} ="
            tasks.append(task)
        
        return tasks