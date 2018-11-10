target = 1000

sum = 0
for i in range(1,target+1):
  sum += i**i

s = str(sum)

print s[len(s)-10:len(s)]
