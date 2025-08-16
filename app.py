from flask import Flask

app = Flask(__name__)

# definindo rotas
@app.route("/")
def entrada():
    return("hello world!")

@app.route("/sobre")
def sobre():
    return("pagina sobre!")

# definindo quem tem permissao de acessar
if __name__ == "__main__":
    app.run(debug=True)
