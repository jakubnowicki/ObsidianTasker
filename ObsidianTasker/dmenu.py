import subprocess

def open_dmenu():
    # Open dmenu with subprocess
    dmenu_process = subprocess.Popen(['dmenu'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Get user input from dmenu
    user_input, _ = dmenu_process.communicate(input=b'')

    # Return user input as a string
    return user_input.decode().strip()
