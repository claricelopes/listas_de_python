hora = float(input('digite o numero de horas que você trabalhou: ')) 
ganho = float(input('digite o valor que você por hora:')) 

salariob = ganho * hora
IR = (salariob * 11/100)  
INSS = (salariob * 8/100)
SI = (salariob * 5/100) 
salarioL = (salariob - IR - INSS - SI) 

print(f'seu salario bruto é: {salariob} R$')
print(f'pagou (11%) para Importo de Renda: {IR} R$')
print(f'pagou (8%) para o INSS: {INSS} R$')
print(f'pagou (5%) para o sindicato: {SI} R$') 

print(f'seu salario liquido é: {salarioL} R$') 


