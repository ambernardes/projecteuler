#Encontrar o 10001th numero primo

#Teste se um numero e primo
def verifica_primo(numero):
	controle = 0
	for i in range(2, numero):
		if numero % i == 0:
			controle = 1
			break
	#Controle informa se o retorno da funcao sera primo ou nao
	if controle == 0:
		return 1		
	else: return 0

x = 2;
controle = 0

while 1:
	if verifica_primo(x):
		controle = controle + 1
	if controle == 10001:
			break
	x = x+1			
			
print x			
	
