#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

parada = 0
for a in range(1000):
	if parada == 1:
		break	
	
	for b in range (a+1,1000):
		if parada == 1:
				break	
		
		for c in range(b+1,1000):
			#se a soma bater, testa  a2 + b2 = c2
			if a+b+c == 1000:
				if (a*a)+ (b*b) == (c*c):
					parada = 1
			if parada == 1:
				break	
			
print (a-1)*(b-1)*c
