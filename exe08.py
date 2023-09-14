valor = float(input('digite o valor do produto comprado: ')) 
pag = str(input('digite a forma de pagamento escolhida (dinheiro, cheque ou cartão): ')) 

div = valor * 0.9 

if pag == 'dinheiro' and valor >= 100: 
    print(f'o valor a ser pago é: {div} R$') 
elif pag == 'cheque' or pag == 'dinheiro' and valor < 100:  
    print(f'o valor a ser pago é: {valor} R$')
elif pag == 'cartão': 
    tip = str(input('digite tipo de pagamento (crédito ou debito): ')) 
    if tip == 'debito': 
     print(f'o valor a ser pago é: {valor} R$') 
    elif tip == 'crédito':
     parcelas = int(input('digite o número de vezes que gostaria de parcelar (até 3): ')) 
     if parcelas == 1:
      print(f'o valor a ser pago é: {valor} R$')  
     elif parcelas == 2:
       print(f'o valor a ser pago é 2 parcelas de {valor/2}')
     elif parcelas == 3:
       print(f'o valor a ser pago é 3 parcelas de {valor/3}') 
     else:
       print(f'número de parcelas inválido') 
          
