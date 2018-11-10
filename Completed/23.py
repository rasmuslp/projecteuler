def sumOfProperDivisors(num):
  # num must be at least 1 for this function to work

  s = 1
  upper = num**0.5
  div = 2

  while upper > div:
    if num % div == 0:
      upper = num/div
      s += upper
      if upper != div:
        # To avoid adding the same divisor twice; the case with 4/2
        s+= div
    div += 1

  return s

# Hurtigere (LOL)
def sumOfProperDivisors2(num):
  s = 1

  for i in xrange(2, int(num**0.5) + 1):
    if num % i == 0:
      s += i
      t = num/i
      if i != t:
        s += t

  return s

target_limit = 28123

abundant_limit = (target_limit+1)>>1
abundant = []
for i in xrange(1,target_limit+1):
  if sumOfProperDivisors2(i) > i:
    abundant.append(i)

flaged = [False] * target_limit
for i in xrange(0,len(abundant)):
  for j in xrange(i,len(abundant)):
    num = abundant[i]+abundant[j]
    if num < target_limit:
      flaged[num] = True

ss = 0
for i in xrange(len(flaged)):
  if not flaged[i]:
    ss += i

print "Sum is " + str(ss)
