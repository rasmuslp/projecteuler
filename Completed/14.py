target = 1000000
start = 2

highStart = 0
highCount = 0

while start < target+1:
  value = start
  count = 0

  while value != 1:
    if value&1: # Odd
      value = 3*value+1
      count += 1
    else: # Even
      value = value>>1
      count += 1
  else:
    if count > highCount:
      highStart = start
      highCount = count

  start += 1 

print "Starting number " + str(highStart) + " got a chain length of " + str(highCount)
