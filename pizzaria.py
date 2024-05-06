while True:
  temperatura = input('Insira a temperatura do forno em °C: ')

  if temperatura.isdigit():
      temperatura = int(temperatura)

      if temperatura <= 48:
          print('A pizza ficará crua.')
      elif 49 <= temperatura <= 54:
          print('O queijo vai derreter, porém a massa não crescerá.')
      elif 55 <= temperatura <= 65:
          print('Recheio e massas estarão no ponto certo.')
      elif temperatura > 65:
          print('A pizza vai queimar.')
      break
  else:
      print('Por favor, insira uma temperatura em números')
        
