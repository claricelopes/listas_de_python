num = 0
soma = 0

while num <= 500: 
    if (num % 2) != 0:
        print(num) 
        soma += num 
    num += 3 

print("a soma dos números ímpares menor do que 500 é:  ", soma)   