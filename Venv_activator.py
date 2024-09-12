import subprocess;
import sys;
import os;

def run_in_venv(script_path):
    venv_path = os.path.dirname(os.path.abspath(__file__)) + "\\.recycler"
    # Define the activation command based on the OS
    activate_cmd = f'{venv_path}/bin/activate' if sys.platform != 'win32' else f'{venv_path}/Scripts/activate'

    # Construct the command to run the script
    command = f'source {activate_cmd} && python {script_path}' if sys.platform != 'win32' else f'{venv_path}/Scripts/activate && python {script_path}'
    
    # Execute the command
    subprocess.run(command, shell=True, check=True)


run_in_venv(os.path.dirname(os.path.abspath(__file__)) + "\\executor.py");