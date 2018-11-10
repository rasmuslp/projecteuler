sum = 0

input1 = 0
input2 = 1
new = 0

while new < 4000000 :
  new = input1 + input2
  input1 = input2
  input2 = new

  if new&1 == 0:
    sum += new

print sum
