from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details} is added to the section"

    def complete_task(self, task_name):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):

        result = [f"Section {self.name}"]
        for t in self.tasks:
            result.append(t.details)
        return '\n'.join(result)

