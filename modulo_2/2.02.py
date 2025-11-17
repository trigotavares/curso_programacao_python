# 2.02

# utilizador = "teste@email.com"
# password = "banana"

# print("Preencha utilizador:")
# respostaUtilizador = input()

# print("Preencha password:")
# respostaPassword = input()

# for i in range(3):
#     if(respostaUtilizador != utilizador or respostaPassword != password):
#         print("accesso negado!")
#         print("Preencha utilizador:")
#         respostaUtilizador = input()
#         print("Preencha password:")
#         respostaPassword = input()
#     else:
#         print("acesso autorizado!")
#         continue
        
# copilot
utilizador = "teste@email.com"
password = "banana"

for i in range(3):
    respostaUtilizador = input("Preencha utilizador: ")
    respostaPassword = input("Preencha password: ")
    if respostaUtilizador == utilizador and respostaPassword == password:
        print("acesso autorizado!")
        break
    else:
        print("acesso negado!")
else:
    print("Número máximo de tentativas atingido.")
