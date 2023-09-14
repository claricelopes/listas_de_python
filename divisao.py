num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))
contador = 0

while (num1 >= num2):
    contador += 1 
    num1 -= num2 

print("o resultado da divisão é: ", contador)
print("o resto da divisão é: ", num1) 

 