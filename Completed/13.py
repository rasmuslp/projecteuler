import sys
import os.path

def main(*args):
  try:
    if len(args) != 2:
      raise Exception("You need to provide an input file.")
    else:
      if os.path.isfile(args[1]):
        f = open(args[1], 'r')

        sum = 0
        for line in f:
          sum += int(line)

        print "Sum " + str(sum)
        print "First 10 digits of sum " + str(sum)[0:10]

      else:
        raise Exception("Could not read file: " + args[1])
  except Exception as e:
    print "Something bad... "
    print e
  else:
    return 0 # exit errorlessly

if __name__ == '__main__':
  sys.exit(main(*sys.argv))
