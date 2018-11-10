import math

power = 1000

num = int(math.pow(2,power))

sum = 0
for n in str(num):
  sum += int(n)

print sum
