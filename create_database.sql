drop database if exists `flask5k`;

create database `flask5k`;

USE flask5k;

CREATE TABLE
    pacientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT,
        genero VARCHAR(10),
        endereco VARCHAR(255),
        cidade VARCHAR(100),
        estado VARCHAR(2),
        telefone VARCHAR(255),
        email VARCHAR(100),
        data_admissao DATE,
        data_alta DATE,
        diagnostico VARCHAR(255),
        tratamento TEXT,
        observacoes TEXT
    );

select * from pacientes;