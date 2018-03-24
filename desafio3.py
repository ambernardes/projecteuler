#Qual o maior fator primo do numero 600851475143?

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
	
def proximo_numero_primo(primo):
	numero = primo + 1
	while 1:
		if verifica_primo(numero):
			return numero
		else: numero = numero + 1
	 
num = 600851475143
primo = 2
lista = []	

while num != 1:
	#se o numero puder ser dividido por um numero primo
	#somente adiciona, se o numero ja nao tiver sido adicionado antes
	if num % primo == 0:
		if primo not in lista:
			lista.append(primo)
		num = num/primo	
	else: primo = proximo_numero_primo(primo)

print lista
