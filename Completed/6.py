sumOfSquares = 0
squareOfSum = 0

for i in range( 1, 101 ):
  sumOfSquares += i * i
  squareOfSum += i

squareOfSum = squareOfSum * squareOfSum

print squareOfSum - sumOfSquares

