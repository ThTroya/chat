from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#criar primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")

#roda o aplicativo
#app.run(debug=True)
socketio.run(app, host="192.168.56.1")

#websocket