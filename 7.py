#10,001 prime
prime = []
num = 2
while (len(prime) < 10001):
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            break
    else:
        prime.append(num)
    num += 1
print(prime)
