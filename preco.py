cod = int(input("digite o código do produto: "))
quan = int(input("digite a quandidade comprada: ")) 
soma = 0
total = 0 

while cod != 0:
    if cod == 1:
        preço1 = 5.50
        soma = preço1 * quan
    elif cod == 2:
        preço2 = 2.30
        soma = preço2 * quan
    elif cod == 3:
        preço3 = 4.75
        soma = preço3 * quan
    elif cod == 4: 
        preço4 = 6.80
        soma = preço4 * quan
    elif cod == 5:
        preço5 = 9.30
        soma = preço5 * quan 
    else: 
        print("código inválido")
    total += soma 
    cod = int(input("digite o código do produto: "))
    quan = int(input("digite a quandidade comprada: ")) 

print("o valor total das compras é: ", total, "R$")