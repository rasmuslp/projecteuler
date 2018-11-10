a = 100
b = 100

num = set()

for i in range(2,a+1):
  for j in range(2,b+1):
    num.add(i**j)

print "Number of distint terms: " + str(len(num))
