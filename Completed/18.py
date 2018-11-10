import sys
import os.path

class Node:
  def __init__(self, cost):
    self.cost = cost
    self.child1 = None
    self.child2 = None
    self.costMax = -1

  def addChild(self, child):
    if self.child1 == None:
      self.child1 = child
    elif self.child2 == None:
      self.child2 = child
    else:
      raise Exception("This node allready has two children..")

  def determineMaxCostToLeaf(self):
    if self.costMax != -1:
      return self.costMax
    elif self.child1 == None and self.child2 == None:
      self.costMax = self.cost
      return self.costMax
    else:
      self.costMax = self.cost + max(self.child1.determineMaxCostToLeaf(), self.child2.determineMaxCostToLeaf())
      return self.costMax

  def __str__(self):
    return self.cost
 
def main(*args):
  try:
    if len(args) != 2:
      raise Exception("You need to provide an input file.")
    else:
      if os.path.isfile(args[1]):
        f = open(args[1], 'r')
        waitingForChildren = []
        underConstruction = []
        for line in f: # Iterate over the levels of the tree
          waitingForChildren = underConstruction
          underConstruction = []
          costs = line.strip().split(' ')
          for i in range(0, len(costs)): # Iterates over the nodes in a level
            node = Node(int(costs[i]))
            underConstruction.append(node)
            if len(costs) == 1:
              # This must be the root
              root = node
            else:
              if i == 0:
                # As this child is on the edge of the triangle, it only has one parent
                waitingForChildren[i].addChild(node)
              elif i == len(costs)-1:
                # As this child is on the edge of the triangle, it only has one parent
                waitingForChildren[i-1].addChild(node)
              else:
                # Has two parents
                waitingForChildren[i-1].addChild(node)
                waitingForChildren[i].addChild(node)
        print "Printing max cost from root to leaf: " + str(root.determineMaxCostToLeaf())
      else:
        raise Exception("Could not read file: " + args[1])
  except Exception as e:
    print e
  else:
    return 0 # exit errorlessly

if __name__ == '__main__':
  sys.exit(main(*sys.argv))
