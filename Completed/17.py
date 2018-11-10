def num_spelled_out(num):
  single = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
  double = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

  s = str(num)
  l = len(s)
  if l == 1:
    return single[num]
  elif l == 2:
    if 10 <= num < 20:
      return double[num]
    elif num % 10 == 0:
      return str(double[int(s[0] + '0')])
    else:
      return str(double[int(s[0] + '0')]) + " " + num_spelled_out(int(s[1]))
  elif l == 3:
    if num % 100 == 0:
      return num_spelled_out(int(s[0])) + " hundred"
    else:
      return num_spelled_out(int(s[0])) + " hundred and " + num_spelled_out(int(s[1:3]))
  elif l == 4:
    if num % 1000 == 0:
      return num_spelled_out(int(s[0])) + " thousand"
    else:
      return num_spelled_out(int(s[0])) + " thousand " + num_spelled_out(int(s[1:4]))


target = 1000

letters = 0
for i in range(1,target+1):
  words = num_spelled_out(i).split(' ')
  print num_spelled_out(i)
  count = 0
  for word in words:
    count += len(word)
  letters += count

print letters
