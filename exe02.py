genero = str(input('digite seu genero, responda com M(mulher) ou H(homem):')) 
altura = float(input('digite sua altura: ')) 

M = (62.1 * altura) - 44.7
H = (72.7 * altura) - 58 

if genero == 'M':
    print(f'seu peso ideal é: {M}') 
else:
    print(f'seu peso ideal é: {H}')  
