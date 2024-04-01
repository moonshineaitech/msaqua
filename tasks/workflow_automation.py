from .task_registry import TaskRegistry

def create_workflow(self, task_sequence, arguments):
    # ... (existing code with error handling and task registry lookup)
    workflow = []
    for task_name, task_args in zip(task_sequence, arguments):
        task = TaskRegistry.get_task(task_name)
        if task is None:
            raise ValueError(f"Task '{task_name}' not registered")
        workflow.append((task, task_args))
    return workflow

def execute_workflow(self, workflow, mode="sequential"):
    # ... (existing code with execution based on mode)
    pass