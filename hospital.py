from flask import Flask

app = Flask(__name__)
#criar a primeira rota
#função -> o que você quer exibir na página

@app.route("/")
def homepage():
    return "Esse é o site do hospital"

@app.route("/pacientes")
def pacientes():
    return "<p>Essa é a página de pacientes</p> Lowrucrada"


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)