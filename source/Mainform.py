#erase 'from source' for unit test
import tkinter;
import cv2;
import threading;
import PIL;
import PIL.ImageTk;
import PIL.Image;
import os;
from source import AI_classifier;
from source import Correctform;
#import AI_classifier;
#import Correctform;


result_img = 0;
img_width = 400;
img_height = 400;

class Mainform() :
    def __init__(self) :
        t1 = threading.Thread(target = camera);
        t1.daemon = True;
        t1.start();

        self.script_dir = os.path.dirname(os.path.abspath(__file__)) + '\\';
        with open(self.script_dir + 'classifier.txt', mode = "r") as f :
            file_dir = f.readline();
        self.classifier = AI_classifier.Classifier(self.script_dir+file_dir);

        self.window = tkinter.Tk();

        self.pic_label = tkinter.Label(master = self.window);
        self.pic_label.grid(row = 0, column = 1, columnspan= 3)

        self.button = tkinter.Button(master = self.window, width = 10, text = "이상해요");
        self.button.config(command=self.capture);
        self.button.grid(row = 1, column = 0, columnspan=1);

        self.result_label = tkinter.Label(master = self.window, width = 50, bg = "gray");
        self.result_label.grid(row=1, column = 1, columnspan= 2);

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
            result_text = self.classifier.classify(result_img);
            self.result_label.config(text = result_text);
        except :
            self.result_label.config(text = "ERR");
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