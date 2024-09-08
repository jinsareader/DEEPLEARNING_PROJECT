import tkinter
import tcp_connector

mysocket = tcp_connector.Mysocket();
mysocket.connect("127.0.0.1", 8080);

class mainwindow :
    def __init__(self) :
        self.window = tkinter.Tk();
        
        self.entry = tkinter.Entry(master = self.window, width = 100);
        self.entry.grid(column = 0, row = 0);

        self.button = tkinter.Button(master = self.window, text = "작동");
        self.button.grid(column = 0, row = 1);
        self.button.config(command=self.send_file);

        self.text = tkinter.Text(width = 100, height = 50);
        self.text.grid(column = 0, row = 2);

        self.window.mainloop();

    def send_file(self) :
        loc = self.entry.get();
        with open(loc, mode = "rb") as f :
            self.text.delete("1.0", "end")
            bytes = f.read();
            self.text.insert(tkinter.CURRENT,bytes,"");
            mysocket.mysend(bytes);


mainwindow();