import tkinter
import tcp_connector

mysocket = tcp_connector.Mysocket();

class mainwindow :
    def __init__(self) :
        self.window = tkinter.Tk();

        r = 0;
        self.iplabel = tkinter.Label(master = self.window, width = 20, text = "IP");
        self.iplabel.grid(column = 0, row = r);
        self.ipentry = tkinter.Entry(master = self.window, width = 80);
        self.ipentry.insert(0,"127.0.0.1");
        self.ipentry.grid(column = 1, row = r);
        self.ipbutton = tkinter.Button(master = self.window, width = 20, text = "연결");
        self.ipbutton.grid(column = 2, row = r);
        self.ipbutton.config(command=self.connect_tcp)

        r = r+1;
        self.label = tkinter.Label(master = self.window, width = 20,text = "url");
        self.label.grid(column = 0, row = r);
        self.entry = tkinter.Entry(master = self.window, width = 80);
        self.entry.grid(column = 1, row = r);
        self.button = tkinter.Button(master = self.window, width =20, text = "작동", state = "disable");
        self.button.grid(column = 2, row = r);
        self.button.config(command=self.send_file);

        r = r + 1;
        self.text = tkinter.Text(width = 100, height = 50);
        self.text.grid(column = 0, row = r, columnspan= 3);

        self.window.mainloop();

    def send_file(self) :
        loc = self.entry.get();
        with open(loc, mode = "rb") as f :
            self.text.delete("1.0", "end")
            bytes = f.read();
            self.text.insert(tkinter.CURRENT,bytes,"");
            mysocket.mysend(bytes);

    def connect_tcp(self) :
        try : 
            mysocket.connect(self.ipentry.get(),8080);
            self.button.config(state = "normal");
            self.ipbutton.config(state = "disabled");
        except Exception as e :
            self.text.delete("1.0", "end");
            self.text.insert(tkinter.CURRENT,e);



mainwindow();
