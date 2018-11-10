targetDigits = 1000

done = False

count = 1
f1 = 0
f2 = 1

while not done:
  tmp = f2
  f2 = f1+f2
  f1 = tmp
  count += 1
  if len(list(str(f2))) == targetDigits:
    done = True

print "First term in fibonacci sequence to contain " + str(targetDigits) + " digits: " + str(count) + "th"
