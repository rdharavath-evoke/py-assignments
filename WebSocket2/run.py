from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, logger=True,  engineio_logger=True)

values = {
    'slider1': 25,
    'slider2': 0,
}

@app.route('/')
def index():
    return render_template('index.html', **values)

@socketio.on('connect')
def on_connect():
    print("client connected!")

@socketio.on('disconnect')
def test_disconnect():
    print("client disconnected!")

@socketio.on('value changed')
def value_changed(message):
    values[message['who']] = message['data']
    emit('update value', message, broadcast=True)

@socketio.on('client_ack')
def client_ack():
    print("received connection acknowledge from client!")

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
