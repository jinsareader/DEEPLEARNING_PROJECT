import socket
import tkinter
import threading
import os

file_dir = ["\\can\\", "\\glass\\", "\\ST\\"];
file_dir_index = 0;


class Serverform :
    def __init__(self) :
        for dir in file_dir :
            try :
                os.makedirs(os.path.dirname(os.path.abspath(__file__))+dir);
            except Exception as e :
                print(e);

        self.window = tkinter.Tk();
        self.IPentry = tkinter.Entry(master = self.window);
        self.IPentry.insert(0,"127.0.0.1;8080");
        self.IPentry.pack(anchor='n');
        
        self.button = tkinter.Button(master = self.window, text = "연결");
        self.button.config(command=self.connect);
        self.button.pack(anchor="s");
    
        self.window.mainloop();

    def connect(self) :
        IPnPort = self.IPentry.get().replace(" ","").split(";");
        server_thread = threading.Thread(target = server, args=(IPnPort[0],IPnPort[1]));
        server_thread.daemon = True;
        server_thread.start();
        self.button.config(text = "연결 됨", state = "disabled");


def handle_client(clientsocket):
    global file_dir_index;

    """Handle communication with a client."""
    while True:
        try:
            data = clientsocket.recv(1024*1024*10)
            if not data:
                break
            # Process the data (e.g., echo it back to the client)
            if len(data) == 1:
                print(int.from_bytes(data));
                file_dir_index = int.from_bytes(data);
            else :
                file_len = len(os.listdir(os.path.dirname(os.path.abspath(__file__)) + file_dir[file_dir_index]));
                with open(os.path.dirname(os.path.abspath(__file__)) + file_dir[file_dir_index] + str(file_len) + ".jpg", "wb") as f :
                    f.write(data);
            clientsocket.sendall(data)
        except ConnectionResetError:
            break
    clientsocket.close()

def server(IP : str, Port : str):
    """Main server function."""
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((IP, int(Port)))  # Using port 8080 to avoid permission issues
    soc.listen(5)
    print("Server is listening on port %s.." %Port)

    while True:
        try:
            clientsocket, address = soc.accept()
            print(f"Connection from {address}")
            # Start a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client, args=(clientsocket,))
            client_thread.start()
        except Exception as e:
            print(f"Error: {e}");


if __name__ == "__main__":
    Serverform();
