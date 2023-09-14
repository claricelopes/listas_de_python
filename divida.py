total = float(input("digite o valor da dívida: "))  
juros = float(input("digite a porcentagem mensal de juros(apenas números): "))   
parcela = float(input("digite o valor que será pago por mês: "))  

meses = 0
valorpag = 0
jurospag = 0 

while (valorpag < total): 
    jurospag += juros 
    valorpag += parcela
    meses += 1   

print("a dívida será paga em: ", meses)
print("o valor total que foi pago é: ", valorpag)  
print("o total pago em juros é: ", jurospag)  