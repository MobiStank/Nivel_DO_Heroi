nomeHeroi = input("Digite o nome do seu Heroi: ")
exp = int(input("Digite o XP do seu Heroi: "))

if exp <= 1000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Ferro")
elif 1000 < exp <= 2000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Bronze")   
elif 2000 < exp <= 5000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Prata")
elif 5000 < exp <= 7000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Ouro")
elif 7000 < exp <= 8000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Platina")
elif 8000 < exp <= 9000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Ascendente")
elif 9000 < exp <= 10000:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Imortal")
elif exp >= 10001:
    print(f"O Heroi de nome {nomeHeroi} está no nível de Radiante")
else:
    print("Valor Inválido!")

