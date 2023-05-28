import socket
import cv2
import numpy as np
import time

HOST = '127.0.0.1'
PORT = 23432
THICKNESS = 5
DRAW_COLOR = (5, 71, 131)
END_KEY = 27

class Drawer:
    def __init__(self):
        self.isDrawing = False
        cv2.namedWindow(winname="window")
        cv2.setMouseCallback("window", self.mouse_callback)

    def line(self, a, b, c, d):
        seg_start = (a, b)
        seg_end = (c, d)

        cv2.line(matrix, seg_start, seg_end, DRAW_COLOR, thickness=THICKNESS)

    def mouse_callback(self, event, x, y, _, __):
        if self.isDrawing:
            coords = f"{self.last_x} {self.last_y} {x} {y}#"

            log(f'Sent:' + coords)
            s.send(coords.encode())

            self.line(self.last_x, self.last_y, x, y)
            
            log(f'Draw coord: {self.last_x} {self.last_y} to {x} {y}.')

        self.last_x, self.last_y = x, y

        if event == cv2.EVENT_LBUTTONDOWN:
            self.isDrawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.isDrawing = False

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def client():
    log('Startup...')
    Drawer()
    log('OK, ready!\n')

    while True:
        cv2.imshow("window", matrix)
        
        if cv2.waitKey(20) == END_KEY:
            break

    cv2.destroyWindow("window")

if __name__ == "__main__":
    matrix = np.zeros(shape=[1024, 1024, 3], dtype=np.uint8)
    
    log('Setting up socket...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    log('Socket ready!')

    client()
