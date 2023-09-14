l1 = float(input('digite o lado 1 de um triangulo: '))
l2 = float(input('digite o lado 2 de um triangulo: ')) 
l3 = float(input('digite o lado 3 de um triangulo: ')) 

if l1 == l2 == l3: 
    print('esse é um triangulo Equilátero') 
elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):  
    print('esse é um triangulo Isósceles:') 
else: 
   print('esse é um triangulo Escaleno') 