num = float(input("digite um número: "))
maior = num
menor = num
soma = num 

while (num != -1):   
    if maior < num:
        maior = num 
    if menor > num:
        menor = num 
    soma += num 
    num = float(input("digite um número: ")) 

print("o maior número  é: ", maior)
print("o menor número é: ", menor)
print("e a soma entre eles é: ", soma)  