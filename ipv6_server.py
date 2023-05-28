import socket
import time

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def startup():
    log("Application started.")
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    log("Setting up socket...")
    setup_socket(s)
    
    log("Socket setup complete.")

    while True:
        s.listen()
        connection, address = s.accept()

        log(f"Got connection: [{address}]")

        response = connection.recv(1024).decode().upper()
        connection.sendto(response.encode(), address)

        log(f"Sent {response} to {address}\n")

def setup_socket(s):
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("::1", 23432))

if __name__ == "__main__":
    startup()
