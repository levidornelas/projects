
def compra():

    while True:
        preco = float(input('Insira o preço das compras: R$'))


        #Formas de pagamento:
        print('FORMAS DE PAGAMENTO:')
        print('[ 1 ] - À VISTA NO DINHEIRO OU CHEQUE')
        print('[ 2 ] - à VISTA NO CARTÃO ')
        print('[ 3 ] - 2x NO CARTÃO')
        print('[ 4 ] - 3x OU MAIS NO CARTÃO')

        formas = [1,2,3,4]
        pagamento = int(input('Insira a forma de pagamento: '))

        if pagamento not in formas:
            print('Por favor, insira uma forma válida de pagamento.')
            continue
            
        
        elif pagamento == 1:
                print(f'O preço do produto à vista com 10% de desconto é: R${preco - preco * (10/100):.2f}')

        elif pagamento == 2:
                print(f'O preço do produto à vista com 5% de desconto é: R${preco - preco * (5/100):.2f}')

        elif pagamento == 3:
                print(f'O preço do produto no cartão não recebe desconto, então será R${preco:.2f}')
                print(f'Sua compra será parcelada em 2x de R${preco / 2:.2f}')

        elif pagamento == 4:
                total = preco + preco * (20/100)
                print(f'Em 3x ou mais no cartão, o produto receberá 20% de juros. Logo, será {total:.2f}')
                totalparc = int(input('Em quantas vezes pretende parcelar? ' ))
                print(f'O produto será parcelado em {totalparc}x com 20% de Juros, com parcelas de R${total / totalparc:.2f}')
        
        print('OBRIGADO PELA PREFERÊNCIA!')
        break

compra()
