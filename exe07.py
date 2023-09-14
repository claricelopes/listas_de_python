valor = float(input('digite o valor do produto comprado: ')) 
pag = str(input('digite a forma de pagamento escolhida (dinheiro ou cheque): '))

div = valor * 0.9   

if pag == 'dinheiro' and valor >= 100: 
    print(f'o valor a ser pago é: {div} R$') 
elif pag == 'cheque' or pag == 'dinheiro' and valor < 100:  
    print(f'o valor a ser pago é: {valor} R$') 
else:
    print(f'forma de pagamento inválida')  
