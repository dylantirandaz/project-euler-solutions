#Even Fibonacci Numbers
sum = 0
ans = 0
n1 = 0 
n2 = 1
while (n2 < 4000000):
    sum = n1+n2
    if sum % 2 == 0:
        ans = ans + sum
    n1 = n2
    n2 = sum
print(ans)
