i = 2520

done = False

while not done:
  if (i % 11 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 16 == 0) and (i % 17 == 0) and (i % 18 == 0) and (i % 19 == 0):
    done = True
  else:
    i += 20

print i

