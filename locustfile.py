from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task(1)
    def equal_reads_and_writes(self):
        if fake.random_int(min=1, max=100) <= 50:  # 50% chance for each
            self.cadastrar_paciente()
        else:
            self.pacientes_info()

    # @task(2)
    # def more_reads_than_writes(self):
    #     if fake.random_int(min=1, max=100) <= 25:  # 25% chance for post
    #         self.cadastrar_paciente()
    #     else:
    #         self.pacientes_info()

    # @task(3)
    # def more_reads_than_writes(self):
    #     if fake.random_int(min=1, max=100) <= 75:  # 75% chance for post
    #         self.cadastrar_paciente()
    #     else:
    #         self.pacientes_info()

    def cadastrar_paciente(self):
        data = {
            'nome': fake.name(),
            'idade': fake.random_int(min=1, max=100),
            'genero': fake.random_element(elements=('Masculino', 'Feminino', 'Outro')),
            'endereco': fake.address(),
            'cidade': fake.city(),
            'estado': fake.state_abbr(),
            'telefone': fake.phone_number(),
            'email': fake.email(),
            'data_admissao': fake.date_this_year(),
            'data_alta': fake.date_this_year(),
            'diagnostico': fake.sentence(),
            'tratamento': fake.text(),
            'observacoes': fake.text()
        }
        try:
            response = self.client.post('/cadastrar_paciente', data=data)
        except Exception as e:
            print("Não foi possível fazer a requisição!\n{}".format(e))

    def pacientes_info(self):
        # Assuming you have patients in the database, you can retrieve a specific patient
        id = fake.random_int(min=1, max=5000)  # Replace with a valid patient ID from your database
        try:
            response = self.client.get(f'/pacientes/{id}')
        except Exception as e:
                print("Não foi possível fazer a requisição! pacientes/{id} \n{}".format(e))
            

        # Note: You might want to add assertions or validation of the response here
