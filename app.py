from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# #configurar o banco de dados
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'flask2k'

# Configure the database
# app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
# app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
# app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
# app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

app.config['MYSQL_HOST'] = 'crud-hospital-db-1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask5k'
mysql = MySQL(app)

# #Creating a connection cursor
# cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# mysql.connection.commit()
 
# #Closing the cursor
# cursor.close()

@app.route('/form')
def form():
    return render_template('forms.html')
 
@app.route('/cadastrar_paciente', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        genero = request.form.get('genero', None)
        endereco = request.form.get('endereco', None)
        cidade = request.form.get('cidade', None)
        estado = request.form.get('estado', None)
        telefone = request.form.get('telefone', None)
        email = request.form.get('email', None)
        data_admissao = request.form.get('data_admissao', None)
        data_alta = request.form.get('data_alta', None)
        diagnostico = request.form.get('diagnostico', None)
        tratamento = request.form.get('tratamento', None)
        observacoes = request.form.get('observacoes', None)
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO pacientes 
                            (nome, idade, genero, endereco, cidade, estado, telefone, email, 
                            data_admissao, data_alta, diagnostico, tratamento, observacoes) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                        (nome, idade, genero, endereco, cidade, estado, telefone, email,
                            data_admissao, data_alta, diagnostico, tratamento, observacoes))
            mysql.connection.commit()
        except Exception as e:
            return "Não foi possível inserir os dados!\n{}".format(e), 400
        
        cursor.close()
        return "Paciente cadastrado com sucesso!"


#criar a primeira rota
#função -> o que você quer exibir na página
#template
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/pacientes")
def pacientes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pacientes")
    result = cursor.fetchall()
    cursor.close()
    return render_template("pacientes.html", pacientes=result)

@app.route("/pacientes/<id>")
def pacientesInfo(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pacientes where id = %s", (id,))
    result = cursor.fetchall()
    cursor.close()
    if(len(result) == 0):
        return "Record not found", 400
    return render_template("paciente.html", paciente=result)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)