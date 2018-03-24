#Achar o maior palandrimo resultante da multiplicacao de dois numeros de 3-digitos

def verifica_palindrome(numero):
	#conveter o numero para string
	palavra = str(numero)
	palindrome = palavra[::-1]
	
	if palavra == palindrome:
		return 1
	else: return 0


lista = []
for i in range(100,1000):
	for j in range(100,1000):
		numero = i*j
		if verifica_palindrome(numero):
			lista.append(numero)

print max(lista)
