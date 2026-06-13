from flask import Flask, render_template, jsonify
import socket
import threading
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
state = ""
def detector():
    global state
    socket_desktop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_desktop.bind(('0.0.0.0', 8080))
    socket_desktop.listen(5)
    inf, addr = socket_desktop.accept()
    try:
        while True:
            data = inf.recv(1024).decode().strip()
            if data == "on":
                print("1")
                state = "on"
            else:
                print("0")
                state = "off"
    finally:
        socket_desktop.close()
def updator():
    while True:
       # print(state)
        socketio.emit('update', state)
        socketio.sleep(1)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    threading.Thread(target=detector, daemon=True).start()
    socketio.start_background_task(updator)
    socketio.run(app, host='0.0.0.0', port=5000)