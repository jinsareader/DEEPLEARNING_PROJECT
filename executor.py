from source import Venv_activator;
import os;


try :
    Venv_activator.run_in_venv(os.path.dirname(os.path.abspath(__file__)) + "\\source\\Mainform.py");
except Exception as e :
    print("\n\n\n--------------------------------오류 발생------------------------------------")
    print(e);
    input();
