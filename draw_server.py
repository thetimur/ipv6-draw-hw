import cv2
import socket
import numpy as np
import time

THICKNESS = 5
HOST = '127.0.0.1'
PORT = 23432
DRAW_COLOR = (5, 71, 131)
END_KEY = 27

matrix = np.zeros(shape=[1024, 1024, 3], dtype=np.uint8)


def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def line(a, b, c, d):
    seg_start = (a, b)
    seg_end = (c, d)

    cv2.line(matrix, seg_start, seg_end, DRAW_COLOR, thickness=THICKNESS)


def setup_socket(s):
    s.settimeout(100)
    s.bind((HOST, PORT))
    s.listen()


def server():
    log("Startup...")
    cv2.namedWindow(winname="window")
    log("OK, ready!\nSetting up socket...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    setup_socket(s)
    log("Socket setup complete.")

    c, _ = s.accept()

    while True:
        cv2.imshow("window", matrix)

        if cv2.waitKey(20) == END_KEY:
            break

        for resp in c.recv(1024).decode().split("#"):
            log(f'Got coord: {resp}')

            if len(resp.split()) < 4:
                continue

            log(resp.split())
            
            line(*map(int, resp.split()))

    c.close()
    cv2.destroyWindow("window")


if __name__ == "__main__":
    server()
