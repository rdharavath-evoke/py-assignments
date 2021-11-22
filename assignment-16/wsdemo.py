from logging import debug
from flask import Flask
from flask_socketio import SocketIO, send
import time
import threading

app=Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app)


@app.route('/message')
def handle_message():
    strn = "message"
    for i in range(0, len(strn)):
        print(strn[i], end="")
        time.sleep(2)

if __name__ == '__main__':
    socketio.run(app,debug=True)




# from flask import Flask, render_template
# from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)

# if __name__ == '__main__':
#     socketio.run(app)





# from flask import Flask

# app=Flask(__name__)

# @app.route("/msg")
# def msg():
#     return {"msg":"message"}

# if __name__=="__main__":
#     app.run(debug=True)








