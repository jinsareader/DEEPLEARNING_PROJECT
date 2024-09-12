from source import Venv_activator;
import subprocess


subprocess.run("cd ./source && python -m venv .recycler", shell=True, check=True)

Venv_activator.run_in_venv("-m pip install opencv-python");
Venv_activator.run_in_venv("-m pip install pillow");
Venv_activator.run_in_venv("-m pip install tensorflow");



