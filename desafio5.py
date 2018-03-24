#Menor inteiro divisivel por todos os numeros de 1 a 20
controle = 0
numero = 20
while 1:
	for i in range(1,21):
		if numero % i == 0:
			controle = controle + 1;
			
	if controle == 20:
		print numero
		break
	else: 
		print numero 
		controle = 0
		numero = numero + 1	 
