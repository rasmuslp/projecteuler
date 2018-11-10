def isPalindrome( x ):
  string = str( x )
  if string == string[::-1]:
    return True
  else:
    return False

largestPalindrome = 0

for i in range(999,0,-1):
  for j in range(999,0,-1):
    product = i*j
    if isPalindrome( product ):
      if product > largestPalindrome:
        largestPalindrome = product

print largestPalindrome
