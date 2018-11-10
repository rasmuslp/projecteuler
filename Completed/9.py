sTarget = 1000

done = False;

for m in range(2, sTarget):  
  for n in range(1, m):
    a = m*m - n*n
    b = 2 * m * n
    c = m*m + n*n
    if (a+b+c == sTarget):
      print "Found that shit " + str(a*b*c)
      done = True
      break
  if done:
    break
