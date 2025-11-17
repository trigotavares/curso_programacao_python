password = "palhaço"
passwordDigitada = ""
tentativa = 0

print("introduza a senha:")

while(tentativa < 3):
    tentativa = tentativa + 1

    passwordDigitada = input()

    if(passwordDigitada == password):
        print("password certa")
        break

    print("password errada")

#copilot
# password = "palhaço"
# tentativa = 0

# print("introduza a senha:")

# while tentativa < 3:
#     if input() == password:
#         print("password certa")
#         break
#     print("password errada")
#     tentativa += 1
