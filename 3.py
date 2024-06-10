#Largest Prime Factor
num = 600851475143 
factors = []
factor = 2
while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
print(factors[-1])
