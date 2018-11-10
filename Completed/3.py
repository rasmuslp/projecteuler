factor = 600851475143

highprime = 0
rest = factor
testprime = 3

while rest > highprime:
  if rest&1 == 0:
    rest /= 2
  elif rest % testprime == 0:
    rest /= testprime
    if testprime > highprime:
      highprime = testprime
    testprime = 3
  else:
    testprime = testprime+2 if testprime&1 else 3

print highprime


    
