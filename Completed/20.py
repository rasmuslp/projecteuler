import math

fac = math.factorial(100)
l = list(str(fac))

sum = 0
for i in range(0, len(l)):
  sum += int(l[i])

print sum
