target = 10001

primes = []
number = 2

while len(primes) != target:
  # Determine if number is prime
  for i in primes:
    if number % i == 0:
      break
  else:
    # It was prime
    primes.append(number)

  number += 1

print primes[target-1]
