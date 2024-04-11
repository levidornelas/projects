#jogador:
jogador = {
    "nome": input("Insira seu nome: "),
    "HP": 100
}

#inimigo:
inimigo = {
    "nome": "Marciano",
    "HP": 100,
    "drop": "Crânio de marciano"
}
inimigo2 = {
    "nome": "Inimigo surpresa", 
    "danoinimigo": 100
}

#ataques do jogador:
ataques = {
    "atk1": "lapada seca", "dano1": 100,
    "atk2": "bate fofo", "dano2":  50,
    "ação": "desviar"
}

print("INFORMAÇÕES DO JOGADOR:")
print("------------------------")
print("NOME:", jogador["nome"])
print("HP:", jogador["HP"])
print("-------------------------")
print("INFORMAÇÕES DO MONSTRO:")
print("------------------------")
print("NOME:", inimigo["nome"])
print("HP:", inimigo["HP"])


ataquejogador = input("Jogador, insira seu ataque: (lapada seca/bate fofo): ")

#jogo em si
if ataquejogador == "lapada seca":
    print(jogador["nome"],"Usou o golpe lapada seca!")
    print("--------------------------------------------")
    print("Parabéns, o", inimigo["nome"], "foi derrotado e está com", inimigo["HP"] - ataques["dano1"], "de vida!")
    print(jogador["nome"],"recebeu", inimigo["drop"])

elif ataquejogador == "bate fofo":
    print("Meu Deus!",jogador["nome"],"bateu fofo!!!!")
    print("-------------------------------------------")
    print("Foi tão fofo que o ", inimigo["nome"], "recuperou ainda mais vida, agora ele está com", inimigo["HP"] + ataques["dano2"], "de HP!")


print("______________________________________________________")
print("OPA! UM inimigo surpresa estava a espreita! ")
print("Ele acerta", jogador["nome"],"Com um golpe fatal! ")
print("_____________________________________________________")
    
acaojogador = input("Qual a sua ação, jogador? ")

if acaojogador == "desviar":
    print(jogador["nome"], "desviou!! Ainda permanece com",jogador["HP"],"de vida!!")

else:
    print("Droga! o ", inimigo2["nome"],"lhe acertou em cheio!",jogador["nome"],"foi eliminado!")
    print(jogador["nome"],"largou",inimigo["drop"])
