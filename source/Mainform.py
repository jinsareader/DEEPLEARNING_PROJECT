#erase 'from source' for unit test
import tkinter;
import cv2;
import threading;
import PIL;
import PIL.ImageTk;
import PIL.Image;
import os
import numpy;
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import AI_classifier;
import Correctform;
import AI_classifier;
import scratch_classifier;
import Correctform;


result_img = 0;
img_width = 400;
img_height = 400;

class Mainform() :
    def __init__(self) :
        self.flg = 0;

        t1 = threading.Thread(target = camera);
        t1.daemon = True;
        t1.start();

        self.script_dir = os.path.dirname(os.path.abspath(__file__)) + '\\';
        with open(self.script_dir + 'define.txt', mode = "r") as f :
            lines = f.readlines()
            if lines[1].split("=")[1].strip() == "h5" :
                file_dir = lines[2].split("=")[1].strip();
                self.AI_classifier = AI_classifier.Classifier(self.script_dir+file_dir)
                self.flg = 0;
            elif lines[1].split("=")[1].strip() == "pt" :
                file_dir = lines[2].split("=")[1].strip();
                self.scratch_classifier = scratch_classifier.Classifier(self.script_dir+file_dir);
                self.flg = 1;

        self.window = tkinter.Tk();

        self.left_panel = tkinter.PanedWindow(master= self.window, width = 70);
        self.left_panel.grid(row = 0, column= 0);

        self.pic_label = tkinter.Label(master = self.left_panel);
        self.pic_label.grid(row = 0, column = 0, columnspan= 3);

        self.button = tkinter.Button(master = self.left_panel, width = 10, text = "이상해요");
        self.button.config(command=self.capture);
        self.button.grid(row = 1, column = 0, columnspan=1);

        self.result_label = tkinter.Label(master = self.left_panel, width = 50, bg = "gray");
        self.result_label.grid(row=1, column = 1, columnspan= 2);

        self.right_panel = tkinter.PanedWindow(master= self.window, width = 80);
        self.right_panel.grid(row = 0, column= 1);

        #self.text = tkinter.Text(master = self.right_panel, width = 60, height = 30);
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot();
        self.ax.set(ylim = (0,1))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_panel)
        self.canvas.get_tk_widget().pack();

        self.update();
        self.classifying();
        self.window.mainloop();

    def update(self) :
        try :
            vid = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB);
            self.photo = PIL.Image.fromarray(vid);
            self.photo = PIL.ImageTk.PhotoImage(image = self.photo);
            self.pic_label.config(image=self.photo);
        except :
            pass;
        self.window.after(15, self.update);
    def classifying(self) :
        try :
            if self.flg == 0 :
                result_text = self.AI_classifier.classify(result_img);
                self.result_label.config(text = result_text);  
            elif self.flg == 1 :
                type, percent = self.scratch_classifier.classify(result_img);
                self.x = type;
                self.y = percent;
                self.ax.bar(self.x,self.y,width=1,color = "blue",edgecolor="white")
                self.canvas.draw();


                result_text = str(type[numpy.argmax(percent)]) + " : " + str(percent[numpy.argmax(percent)]);
                self.result_label.config(text = result_text);
        except Exception as e :
            self.result_label.config(text = e);
        self.window.after(15, self.classifying);

    def capture(self) :
        cv2.imwrite(self.script_dir +'result_img.jpg', result_img);
        Correctform.Correctform();

        

def camera() :
    global result_img;
    vid = cv2.VideoCapture(0);

    while True :
        ret, img = vid.read();
        result_img = cv2.resize(img,(img_width,img_height));
        ##vid.release();


if __name__ == "__main__" :
    Mainform();