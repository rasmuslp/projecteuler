import sys
import os.path

def alphabeticalValue(string):
  alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
  dic = dict(zip(alph,num))

  value = 0
  for s in string.lower():
    value += dic[s]
  
  return value
  

def main(*args):
  try:
    if len(args) != 2:
      raise Exception("You need to provide an input file.")
    else:
      if os.path.isfile(args[1]):
        f = open(args[1], 'r')
        # Read names and and to list
        names = f.read().split(",")
        for i in range(0,len(names)):
          names[i] = names[i].strip('"')
        # Sort list
        names.sort()
        # Calculate
        totalValue = 0
        for i in range(0,len(names)):
          totalValue += (i+1) * alphabeticalValue(names[i])

        print "Total: " + str(totalValue)
      else:
        raise Exception("Could not read file: " + args[1])
  except Exception as e:
    print "Something bad... "
    print e
  else:
    return 0 # exit errorlessly

if __name__ == '__main__':
  sys.exit(main(*sys.argv))
