from flask import Flask

app = Flask(__name__)

@app.get("/")
def inicio():
    return {
        "mensagem": "Api de Chamados em Funcionamento"
    }