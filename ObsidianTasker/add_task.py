from .config import load_config

def add_task(task: str):
    print("Adding task")
    config = load_config()
    task_file_path = config['Settings']['TaskFilePath']
    task = f"- [ ] {task}"
    with open(task_file_path, 'a') as task_file:
        task_file.write(task + '\n')
    return None
