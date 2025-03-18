import os
import random
 
os.system("cls")
 
print('''
░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║███████║██║░░╚═╝███████║██║░░██║
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔══██║██║░░██║
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░''')
 
print("Bem-vindo ao jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 30!")
 
numero_secreto = random.randint(1, 30)
 
limite_tentativas = 4
tentativas = 0
 
 
while tentativas < limite_tentativas:
 
    palpite = int(input(f"Tentativa {tentativas + 1} de {limite_tentativas}: "))
   
 
    tentativas += 1
   
 
    if palpite < numero_secreto:
        print("O número é maior!")
    elif palpite > numero_secreto:
        print("O número é menor!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break  
 
 
if palpite != numero_secreto:
    print(f"Você atingiu o limite de tentativas. O número correto era {numero_secreto}.")