#Sum Square Difference
SumOfSq = 0
SqOfSum = 0
for i in range(101):
    SumOfSq = SumOfSq + i*i
    SqOfSum = SqOfSum + i
print((SqOfSum*SqOfSum) - SumOfSq)
