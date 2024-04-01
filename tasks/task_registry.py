class TaskRegistry:
    _tasks = {}

    @classmethod
    def register_task(cls, name, task_function):
        if not callable(task_function):
            raise ValueError("Task function must be callable")
        cls._tasks[name] = task_function

    @classmethod
    def get_task(cls, name):
        return cls._tasks.get(name)