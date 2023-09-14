x =70000
y = 180000
anos = 0

while (y > x):
    x =  x * 1.035
    y = y * 1.015
    anos += 1 

print("o número de anos necessários para a população x ultrapassar a população y é: ", anos)