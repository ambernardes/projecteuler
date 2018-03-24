#Considerando uma sequencia fibonacci cujos termos nao excedam 4 miloes, achar 
#a somas dos valores pares.

atual = 1
anterior = 0
prox = 1
soma = 0 

while prox < 4000000:
	atual = prox
	if atual % 2 == 0:
		soma = soma + atual
	prox = anterior + atual
	
	anterior = atual 
print soma
	
