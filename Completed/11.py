import sys
import os.path

def main(*args):
  try:
    if len(args) != 2:
      raise Exception("You need to provide an input file.")
    else:
      if os.path.isfile(args[1]):
        f = open(args[1], 'r')
        # Read grid from file
        grid = {}
        row = 0
        for line in f:
          column = 0
          for element in line.strip().split(' '):
            grid[row,column] = int(element)
            column += 1
          row += 1

        # Print grid
        for r in range(row):
          for c in range(column):
            print str(grid[r,c]).zfill(2),
          print ""

        # Assuming grid is wellformed; i.e. all rows have equal length
        if row < 4 or column < 4:
          raise Exception("Grid not large enough to search.")

        greatestProduct = 0

        # Check horizontally
        for r in range(row):
          for c in range(column-3):
            product = grid[r,c] * grid[r,c+1] * grid[r,c+2] * grid[r,c+3]
            if product > greatestProduct:
              greatestProduct = product

        # Check vertically
        for r in range(row-3):
          for c in range(column):
            product = grid[r,c] * grid[r+1,c] * grid[r+2,c] * grid[r+3,c]
            if product > greatestProduct:
              greatestProduct = product

        # Check diagonally
        for r in range(row):
          for c in range(column-3):
            if r < row-3:
              product = grid[r,c] * grid[r+1,c+1] * grid[r+2,c+2] * grid[r+3,c+3]
              if product > greatestProduct:
                greatestProduct = product
            if r > 2:
              product = grid[r,c] * grid[r-1,c+1] * grid[r-2,c+2] * grid[r-3,c+3]
              if product > greatestProduct:
                greatestProduct = product

        print "Greatest 4-product in grid: " + str(greatestProduct)

      else:
        raise Exception("Could not read file: " + args[1])
  except Exception as e:
    print "Something bad... "
    print e
  else:
    return 0 # exit errorlessly

if __name__ == '__main__':
  sys.exit(main(*sys.argv))
