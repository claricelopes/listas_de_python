n = float(input("digite o número que deseja saber a raiz quadrada: "))
base = 2
p = (base + (n / base)) / 2 

while abs(base - p) > 0.0001:
    base = p 
    p = (base + (n / base)) / 2  

print(f"a raiz quadrada é: {p:.2f}")    