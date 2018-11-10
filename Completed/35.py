def rotate_string(string,n):
  l1 = list(string)
  l2 = l1[n:] + l1[:n]
  return "".join(l2)

def euler_sieve(n):
  # Create a candidate list within which non-primes will
  # marked as None, noting that only candidates below
  # sqrt(n) need be checked.
  candidates = range(n+1)
  fin = int(n**0.5)

  # Loop over the candidates, marking out each multiple.
  # If the current candidate is already checked off then
  # continue to the next iteration.
  for i in xrange(2, fin+1):
    if not candidates[i]:
      continue

    candidates[2*i::i] = [None] * (n//i - 1)

  # Filter out non-primes and return the list.
  return [i for i in candidates[2:] if i]

target = 1000000
primes = set(euler_sieve(target))

circ = set()
for n in primes: # For all primes
  for i in range(len(str(n))): # For each rotation of the prime
    num = int(rotate_string(str(n),i))
    if num not in primes:
      break
  else:
    circ.add(n)

print "Number of circular primes: " + str(len(circ))
