nome = input("digite o nome da aluna: ")
idade = int(input("Digite idade da aluna: "))
altura = float(input("Digite a altura da aluna: "))
hobbies = input("Digite os hobbies da aluna separados por virgula: ")
hobbies1 = hobbies.split(",")# transforma os hobbies em uma lista
endereco_rua = input("Digite o nome da rua da aluna: ")
endereco_numero = int(input("Digite o numero da casa da aluna: "))
endereco_cidade = input('Digite a cidade da aluna: ')
endereco = (endereco_rua, endereco_numero , endereco_cidade)#cria tupla com o endereco
email = input("Digite o email da aluna: ")
telefone = input("Digite o telefone da aluna: ")
contato ={"email" : email, "telefone" : telefone}#cria um dicionario com o contato

print ("\nOlá, segue inforamções sobre a alunea: ")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Hobbies:", hobbies1)
print("Endereço:", endereco)
print("Contato:", contato)



