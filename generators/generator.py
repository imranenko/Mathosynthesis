class Generator:
    @staticmethod
    def generate_block(task_function, settings):
        lines = []
        lines.append("\\begin{multicols}{2}")
        lines.append("\\begin{enumerate}")
        
        tasks = task_function(settings)
        for task in tasks:
            lines.append(f"\\item {task}")
        
        lines.append("\\end{enumerate}")
        lines.append("\\end{multicols}")
        
        return lines