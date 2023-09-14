n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: ')) 

media = (n1 + n2) / 2

if 9.0 < media <= 10.0:
    print('conceito: A')
elif 7.5 < media <= 9.0:
    print('conceito: B')
elif 6.0 < media <= 7.5:
    print('conceito: C') 
elif 4.0 < media <= 6.0:
    print('conceito: D')
elif 4.0 >= media >= 0.0:
    print('conceito: E') 
else:
    print('media inválida') 