import socket
import time

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def client():
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    log("Client started.")
    log("Setting up socket...")
    setup_socket(s)
    
    log("Socket setup complete.")

    log("Sending \"Hello from client!\" to server.")
    s.send("Hello from client!".encode())

    log("Server response: " + s.recv(1024).decode())

def setup_socket(s):
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(("::1", 23432))

if __name__ == "__main__":
    client()
