#largest palindrome product
list = []
for i in range (100, 999):
    for j in range(100, 999):
        pal = i * j
        if (str(pal) == str(pal)[::-1]):
            list.append(pal)
print(max(list))
