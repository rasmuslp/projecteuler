import math

def printMatrix():
  output = str()

  for r in xrange(n):
    for c in xrange(n):
      output += ' ' + str(matrix[r][c])
      if c == n-1:
        output += '\r\n'

  print output[:-2]

n = 1001
matrix = [[0 for x in xrange(n)] for x in xrange(n)]

# Find center of NxN matrix (0-indexed)
r_center = int(math.floor(n/2))
c_center = int(math.floor(n/2))

r_current = r_center
c_current = c_center

count = 0;
while count < n*n:
  count += 1
  if 0 <= r_current and r_current < n and 0 <= c_current and c_current < n and matrix[r_current][c_current] != 0:
    print 'ERROR, not 0'
  matrix[r_current][c_current] = count
  
  # Calculate next position
  # Right used ?
  right = False
  if c_current+1 < n and matrix[r_current][c_current+1] != 0:
    right = True
    
  # Bottom used ?
  bottom = False
  if r_current+1 < n and matrix[r_current+1][c_current] != 0:
    bottom = True
    
  # Left used ?
  left = False
  if 0 <= c_current-1 and matrix[r_current][c_current-1] != 0:
    left = True
    
  # Top used ?
  top = False
  if 0 <= r_current-1 and matrix[r_current-1][c_current] != 0:
    top = True

  # Initial position
  if not right and not bottom and not left and not top:
    c_current += 1
    continue

  # Second position  
  if left and not right and not top and not bottom:
    r_current += 1
    continue

  if top and not left:
    c_current -= 1
    continue
    
  if top and left:
    r_current += 1
    continue
  
  if not top and right:
    r_current -= 1
    continue
    
  if not top and not right:
    c_current += 1
    continue

printMatrix()

diagSum = 0

print 'Diagonal 1'
for r in xrange(n):
  for c in xrange(n):
    if r == c:
      diagSum += matrix[r][c]
      print matrix[r][c]

print 'Diagonal 2'
for r in xrange(n-1,-1,-1):
  for c in xrange(n):
    if r + c == n - 1:
      diagSum += matrix[r][c]
      print matrix[r][c]
      
# Subtract center, as it was counted twice
diagSum -= 1
      
print 'DONE'
print 'Result:'
print diagSum
