"""
nome=input("Digite o seu nome: ")
if (nome == "Kaique"):
    print("Você é lindo")
"""
import os
num1=int(input("Digite o primeiro valor: "))
num2=int(input("Digite o segundo valor: "))
soma = num1+num2
print("A soma é " + str(soma))
opc=input("Deseja fazer mais alguma soma? [s/n]: ")
if opc == 's' or opc == 'S':
    print("Eu não ligo meu parcero")
    print("Tchau :3")
    xing=input("Está me xingando? [s]: ") 
    if xing=='s' or xing == 'S':
        os.system('clear')
        print("Fodasi :$")

