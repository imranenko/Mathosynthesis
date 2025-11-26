from .generator import Generator

class Root(Generator):
    @staticmethod
    def generate_task(settings: dict) -> list[str]:
        tasks = []
        amount = settings.get("amount", 1)
        root_cfg = settings.get("root", (2, 9))
        index_cfg = settings.get("index", (2, 2))
        
        root_list = Root.generate_numbers(root_cfg, amount)
        index_cfg = Root.generate_numbers(index_cfg, amount)
        
        for i in range(amount):
            root = root_list[i]
            index = root_list[i]
            radicant = root**index

            if index == 2:
                task = f"\sqrt{{{radicant}}} ="
            else:
                task = f"\sqrt[{index}]{{{radicant}}} ="
                
            tasks.append(task)
                
        return tasks