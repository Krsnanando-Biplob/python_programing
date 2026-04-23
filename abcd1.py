n = int(input("Give me one number: "))

sum = 0

for x in range(1, n+1):
    sum = x + sum
print("sum =", sum)