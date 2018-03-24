#Encontrar a soma de todos os multiplos de 3 ou 5, abaixo de 1000.

soma = 0
for i in range(1000):
	
	if i % 3 == 0 or i % 5 == 0:
		soma = soma +i

#Retorna o soma		
print soma
