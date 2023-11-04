from faker import Faker
import random
import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='flask2k'
)

cursor = conn.cursor()

fake = Faker()

for _ in range(2000):
    nome = fake.name()
    idade = random.randint(1, 100)
    genero = random.choice(['Masculino', 'Feminino', 'Outro'])
    endereco = fake.address()
    cidade = fake.city()
    estado = fake.state_abbr()
    telefone = fake.phone_number()
    email = fake.email()
    data_admissao = fake.date_this_year()
    data_alta = fake.date_this_year()
    diagnostico = fake.sentence()
    tratamento = fake.text()
    observacoes = fake.text()
    try:

        cursor.execute('''INSERT INTO pacientes 
                        (nome, idade, genero, endereco, cidade, estado, telefone, email, 
                        data_admissao, data_alta, diagnostico, tratamento, observacoes) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    (nome, idade, genero, endereco, cidade, estado, telefone, email,
                        data_admissao, data_alta, diagnostico, tratamento, observacoes))

    except Exception as e:
        print("Não foi possível inserir os dados!\n{}".format(e))

conn.commit()
cursor.close()
conn.close()

print("Dados inseridos com sucesso!")
