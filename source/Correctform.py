#erase from source when unit test
import tkinter
import os;
from functools import partial
import tcp_connector 


class Correctform :
    def __init__(self) :
        self.ivar = 0;
        r = 0;
        self.window = tkinter.Tk();
        self.socket = tcp_connector.Mysocket();
        try :
            self.script_dir = os.path.dirname(os.path.abspath(__file__)) + '\\';
            with open(self.script_dir+"IPnPort.txt", mode = "r") as f :
                temp = f.readline();
                IPnPort = temp.replace(" ","").split(";");
                self.socket.connect(IPnPort[0],int(IPnPort[1]));
                self.label_text = "당신은 이걸 무어라 생각하시나요?"
        except Exception as e :
            self.label_text = "서버 연결에 실패했습니다. " + str(e)
        self.label = tkinter.Label(self.window, text = self.label_text);
        self.label.grid(row = r, column = 0);
        r = r + 1;

        self.var = tkinter.IntVar();
        self.rb1 = tkinter.Radiobutton(self.window, text = "캔", variable = self.var, value = 0, anchor = "w", width= 50);
        self.rb2 = tkinter.Radiobutton(self.window, text = "유리병", variable = self.var, value = 1, anchor = "w", width= 50);
        self.rb3 = tkinter.Radiobutton(self.window, text = "스티로폼", variable = self.var, value = 2, anchor = "w", width= 50);
        self.rb1.config(command = partial(self.rb_click, 0));
        self.rb2.config(command = partial(self.rb_click, 1));
        self.rb3.config(command = partial(self.rb_click, 2));
        self.rb1.grid(row = r, column = 0);
        r += 1;
        self.rb2.grid(row = r, column = 0);
        r += 1;
        self.rb3.grid(row = r, column = 0);
        r += 1;

        self.ok_button = tkinter.Button(self.window, text = "확 인");
        self.ok_button.config(command=self.ok_func);
        self.ok_button.grid(row = r, column= 0);


        self.window.mainloop();

    def ok_func(self) :
        #self.ok_button.config(text = str(self.var.get()));
        #self.socket.mysend(self.var.get().to_bytes());
        self.socket.mysend(self.ivar.to_bytes());
        with open(self.script_dir+"result_img.jpg", "rb") as f:
            byte = f.read();
            self.socket.mysend(byte);
    
    def rb_click(self, i : int) :
        self.ivar = i;
        

if __name__ == "__main__" :
    Correctform();
