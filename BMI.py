peso = float(input("Insira o seu Peso em kgs: "))
altura = float(input("Insira sua altura em metros: "))

IMC = (peso /  (altura * altura))

#Magreza
if IMC<18.5:
    print(f'Seu IMC exato é {IMC:.2f} e você está no estado de magreza.')
  
#Normal
elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC éxato é {IMC:.2f} e você está normal.')

#Obesidade grau I
elif IMC >= 25 and IMC < 35:
    print(f'Seu IMC exato é {IMC:.2f}, e você está com obesidade grau I.')

#Obesidade grau II
elif IMC >= 35 and IMC < 40:
    print(f'Seu IMC exato é {IMC:.2f}, e você está com obesidade grau II.')
    
#Obesidade grau III
elif IMC>=40:
    print(f'Seu IMC exato é {IMC:.2f} e você está com obesidade grau III.')
