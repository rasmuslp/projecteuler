def divisors(num):
  sum = 1

  upper = num
  div = 2  
  while True:
    if div >= upper:
      break
    if num % div == 0:
      # Found divisor!
      upper = num/div
      sum += upper
      sum += div

    div += 1

  return sum

target = 10000

sum = 0
checked = [False]*target
for a in range(0,target):
  if not checked[a]:
    b = divisors(a)
    if a != b and a == divisors(b):
      # Found amicable pair!
      sum += a + b
      checked[a] = True
      checked[b] = True

print sum
