# CRUD.PY
Um Crud feito em python com conexão com MySQL
# CRUD feito em python

Este projeto é uma aplicação Python para gerenciar um banco de dados de clientes. Ele permite cadastrar, deletar, atualizar e listar usuários em uma tabela MySQL.

## Funcionalidades

- **Cadastrar Usuário**: Adiciona um novo usuário ao banco de dados.
- **Deletar Usuário**: Remove um usuário existente do banco de dados com base no ID.
- **Atualizar Usuário**: Atualiza as informações de um usuário existente.
- **Listar Usuários**: Exibe todos os usuários cadastrados no banco de dados.

## Requisitos

- Python 3.x
- MySQL
- Biblioteca `mysql-connector-python`

## Instalação

1. Clone o repositório para sua máquina local:
   ```sh
   git clone https://github.com/seu_usuario/cadastro_usuarios.git

    Navegue até o diretório do projeto:

    sh

cd cadastro_usuarios

Instale as dependências necessárias:

sh

    pip install mysql-connector-python

Configuração do Banco de Dados

Certifique-se de que o MySQL está instalado e configurado. Crie um banco de dados chamado banco_delta e uma tabela clientes com a seguinte estrutura:

sql

CREATE DATABASE banco_delta;

USE banco_delta;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    telefone VARCHAR(255),
    email VARCHAR(255),
    cidade VARCHAR(255)
);

Como Usar

    Execute o script principal:

    sh

    python main.py

    Siga as instruções no terminal para interagir com a aplicação.

Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga estas etapas:

    Faça um fork do repositório.
    Crie um branch para sua feature ou correção:

    sh

git checkout -b minha-feature

Faça um commit com suas alterações:

sh

git commit -m 'Minha nova feature'

Envie suas alterações para o repositório remoto:

sh

git push origin minha-feature

Abra um Pull Request.
