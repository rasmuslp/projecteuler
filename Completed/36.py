def isPalindrome( x ):
  string = str( x )
  if string == string[::-1]:
    return True
  else:
    return False

target = 1000000
sum = 0

for i in range(target):
  b = bin(i)[2:]
  if isPalindrome(i) and isPalindrome(b):
    sum += i

print "Sum of all palindromic numbers in base 10 and base 2 under " + str(target) +": " + str(sum)
