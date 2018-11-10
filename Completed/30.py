numbers = set()

for i in range(2,1000000):
  power = 0
  for n in str(i):
    power += int(n)**5
  if i == power:
    print i
    numbers.add(i)

print "Sum of numbers: " + str(sum(numbers))
