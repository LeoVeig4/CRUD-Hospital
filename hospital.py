from flask import Flask, render_template

app = Flask(__name__)
#criar a primeira rota
#função -> o que você quer exibir na página
#template
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/pacientes")
def pacientes():
    return render_template("pacientes.html")

@app.route("/pacientes/<nome>")
def pacientesNome(nome):
    return render_template("pacientes.html", nome=nome)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)