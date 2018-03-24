#Achar a diferenca da soma 
soma = 0
for i in range(101):
	soma = soma + (i*i)

soma2 = 0
for j in range(101):
	soma2 = soma2 + j
	
soma2= soma2*soma2
print soma2 - soma	
