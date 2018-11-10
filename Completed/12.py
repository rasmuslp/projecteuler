def tri(n):
  return (n*(n+1))>>1

target = 500

done = False
n = 2

while True:
  triangle = tri(n)
  divisors = set([1,triangle])

  upper = triangle
  lower = 1
  div = lower+1

  while True:
    if upper <= div:
      break
    if triangle % div == 0:
      upper = triangle/div
      lower = div
      divisors.add(upper)
      divisors.add(lower)
#      print "Divisors: " + str(len(divisors))
      div = lower + 1
    else:
      div += 1

  print "Done with triangle number " + str(n) + " " + str(tri(n)) + " with " + str(len(divisors)) + " divisors"

  if len(divisors) > target:
    break

  n += 1

print n
print tri(n)
print len(divisors)
print "DONE"

