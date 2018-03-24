#Encontrar a soma dos numeros primos inferiores a 2 bilhoes
import math
#Teste se um numero e primo
def verifica_primo(numero):
	controle = 0
	aux = int(round(math.sqrt(numero)))
	for i in range(2, aux+1):
		if numero % i == 0:
			print numero
			controle = 1
			break
	#Controle informa se o retorno da funcao sera primo ou nao
	if controle == 0:
		return 1		
	else: return 0

x = 2;
controle = 0

while x < 2000000:
	if verifica_primo(x):
		print x
		controle = controle + x
	
	x = x+1			
			
print controle		


