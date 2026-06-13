#ONLY FOR TESTING NO REAL USE IN THE ACTUAL SYSTEM!
import socket
socket_desktop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_desktop.bind(('192.168.1.2', 8080))
socket_desktop.listen(5)
inf, addr = socket_desktop.accept()
try:
    while True:
        data = inf.recv(1024).decode().strip()
        if data == "on":
            print("1")
except KeyboardInterrupt:
    socket_desktop.close()
