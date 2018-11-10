# 419: Look and say sequence

# Target element
n = 40
print 'n: ' + str(n)

# Current element
i = 1

# Look and say sequence
las = '1'

# Create LAS sequence of length n
while i < n:
  length = len(las)
  print length
  currentIndex = 0
  nextLas = ''
  while currentIndex < length:
    # Examine LAS
    current = las[currentIndex]
    consecutiveCount = 1
    while currentIndex+consecutiveCount <= length-1 and current == las[currentIndex+consecutiveCount]:
      # Count consecutive terms
      consecutiveCount += 1
    currentIndex += consecutiveCount
    nextLas += str(consecutiveCount) + current
  las = nextLas
  i += 1
  
print 'LAS: ' + las

# Number of 1's, 2's, and 3's in the resulting LAS
a = 0
b = 0
c = 0

index = 0
length = len(las)
while index < length:
  current = las[index]
  index += 1
  if current == '1':
    a += 1
  elif current == '2':
    b += 1
  elif current == '3':
    c += 1
  else:
    print 'Found this: ' + current

print 'A(' + str(n) + '): ' + str(a)
print 'B(' + str(n) + '): ' + str(b)
print 'C(' + str(n) + '): ' + str(c)
