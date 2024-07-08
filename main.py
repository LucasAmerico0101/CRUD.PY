from mysql.connector import connect, Error
import sys

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )
    return connection

connection = mysql_connection('localhost', 'root', 'root', 'banco_delta')

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    tel = input("Digite o telefone do usuário: ")
    email = input("Digite o email do usuário: ")
    cidade = input("Digite a cidade do usuário: ")

    query = '''
    INSERT INTO clientes (nome, telefone, email, cidade)
    VALUES (%s, %s, %s, %s)
    '''
    values = (nome, tel, email, cidade)

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("-----CADASTRO FEITO COM SUCESSO!!-----")
    except Error as e:
        print(f"Erro ao cadastrar usuário: {e}")

def deletar_usuario():
    id = input("Digite o ID do usuário: ")

    query = '''
    DELETE FROM clientes WHERE id = %s
    '''
    values = (id,)

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("-----USUÁRIO DELETADO COM SUCESSO!!-----")
    except Error as e:
        print(f"Erro ao deletar usuário: {e}")

def atualizar_usuario():
    id = input("Digite o ID do usuário: ")
    coluna = input("Que coluna deseja atualizar: ")
    valor = input("Digite o novo valor: ")

    query = f'''
    UPDATE clientes SET {coluna} = %s WHERE id = %s
    '''
    values = (valor, id)

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("-----USUÁRIO ATUALIZADO COM SUCESSO!!-----")
    except Error as e:
        print(f"Erro ao atualizar usuário: {e}")

def listar_usuarios():
    print("----LISTA DE USUÁRIOS-----")
    query = '''
    SELECT * FROM clientes
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Error as e:
        print(f"Erro ao listar usuários: {e}")

def menu():
    print("MENU")
    print("1 - Cadastrar Usuário")
    print("2 - Deletar Usuário")
    print("3 - Atualizar Usuário")
    print("4 - Listar Usuários")
    print("5 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        deletar_usuario()
    elif opcao == "3":
        atualizar_usuario()
    elif opcao == "4":
        listar_usuarios()
    elif opcao == "5":
        print("-----PROGRAMA FINALIZADO-----")
        sys.exit()
    else:
        print("-----OPÇÃO INVÁLIDA-----")

def main():
    while True:
        print("-----CADASTRO DE USUÁRIOS-----")
        menu()

if __name__ == "__main__":
    main()
