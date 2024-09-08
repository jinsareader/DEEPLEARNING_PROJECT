import socket
import threading
import keyboard

def handle_client(clientsocket):
    """Handle communication with a client."""
    while True:
        try:
            data = clientsocket.recv(1024*1024*10)
            if not data:
                break
            # Process the data (e.g., echo it back to the client)
            with open("./test.jpg", "wb") as f :
                f.write(data);
            clientsocket.sendall(data)
        except ConnectionResetError:
            break
    clientsocket.close()

def server():
    """Main server function."""
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(('127.0.0.1', 8080))  # Using port 8080 to avoid permission issues
    soc.listen(5)
    print("Server is listening on port 8080...")

    while True:
        try:
            clientsocket, address = soc.accept()
            print(f"Connection from {address}")
            # Start a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client, args=(clientsocket,))
            client_thread.start()
        except Exception as e:
            print(f"Error: {e}")
        
        # Check if the 'q' key is pressed to stop the server
        if keyboard.is_pressed('q'):
            print("Stopping server...")
            break

    soc.close()

if __name__ == "__main__":
    server()