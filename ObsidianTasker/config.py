import configparser
import os

def get_config_path():
    return os.path.expanduser('~/.obsidiantasker/config.ini')

def validate_path(file_path):
    # Check if the provided path is valid
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    else:
        return False

def prompt_for_task_file_path():
    while True:
        task_file_path = input("Please enter the path to your task file: ").strip()
        if validate_path(task_file_path):
            return task_file_path
        else:
            print("The path provided is incorrect. Please try again.")

def load_config():
    # Define the path to the configuration file
    config_path = get_config_path()

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Check if the config file exists
    if not os.path.exists(config_path):
        # If not, prompt the user for the task file path
        print("Welcome to ObsidianTasker!")
        task_file_path = prompt_for_task_file_path()

        # Ensure the containing directory exists
        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        # Set the provided task file path in the config
        config['Settings'] = {'TaskFilePath': task_file_path}

        # Write the new configuration to the file
        with open(config_path, 'w') as config_file:
            config.write(config_file)
    else:
        # If the config file exists, read it
        config.read(config_path)

    return config

def save_config(config):
    config_path = get_config_path()
    with open(config_path, 'w') as config_file:
        config.write(config_file)

def set_task_file_path():
    config = load_config()
    task_file_path = prompt_for_task_file_path()
    config['Settings']['TaskFilePath'] = task_file_path
    save_config(config)

def get_task_file_path():
    config = load_config()
    # Check if the 'TaskFilePath' is in config, otherwise prompt the user
    if 'TaskFilePath' not in config['Settings']:
        set_task_file_path()
    return config['Settings']['TaskFilePath']
