# Use uma imagem base do Python
FROM python:3.9-slim-buster

# Defina o diretório de trabalho no container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config

# Copie os arquivos de requisitos para o container
COPY requirements.txt .
# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o container
COPY . .

# Set the environment variables
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=flask2k

# Exponha a porta que o Flask vai rodar
EXPOSE 5000

# Defina a variável de ambiente para o Flask saber que está em produção
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Inicie a aplicação
CMD ["flask", "run"]
