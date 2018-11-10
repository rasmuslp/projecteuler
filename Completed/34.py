import math

limitFound = False
facMax = math.factorial(9)
digitLimit = 1
while True:
  if digitLimit < len(str(facMax*digitLimit)):
    digitLimit += 1
  else:
    break

numbers = set()
for i in range(3,10**digitLimit):
  if i % 10000 == 0:
    print "At " + str(i)

  fac = 0
  for n in str(i):
    fac += math.factorial(int(n))
  if i == fac:
    print i
    numbers.add(i)

print "Sum of numbers: " + str(sum(numbers))
