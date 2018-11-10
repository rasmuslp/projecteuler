import sys
import os.path
import traceback

class field:
	def __init__(self, r, c, init_value):
		self.r = r
		self.c = c
		self.value = 0
		self.init_value = int(init_value)
		self.possible = set( range(1,10) )

	def add_row(self, row):
		self.row = row

	def add_column(self, column):
		self.column = column

	def add_square(self, square):
		self.square = square

	def init(self):
		if self.init_value > 0:
			self.set_value( self.init_value )

	def set_value(self, value):
		self.value = value
		self.possible.clear()
		for f in self.row:
			f.remove_possible( value )
		for f in self.column:
			f.remove_possible( value )
		for f in self.square:
			f.remove_possible( value )

	def remove_possible(self, value):
		if value in self.possible:
			self.possible.remove( value )
			#if len(self.possible) == 0:
			#	print "Possible reduced to ZERO"

	def set_single(self):
		if self.no_possible() == 0 and self.value == 0:
			print "WTF"

		if self.no_possible() == 1:
			self.set_value( self.possible.pop() )
			return True
		return False

	def __str__(self):
		return str(self.value)

	def done(self):
		if self.value > 0:
			return True
		else:
			return False

	def no_possible(self):
		return len( self.possible )

	def set_hidden_single(self):
		val = self.find_hidden_single( self.row )
		if val:
			self.set_value( val )
			#print "[" + str(self.r+1) + "][" + str(self.c+1) + "] Value " + str( val )
			return True
		val = self.find_hidden_single( self.column )
		if val:
			self.set_value( val )
			#print "[" + str(self.r+1) + "][" + str(self.c+1) + "] Value " + str( val )
			return True
		val = self.find_hidden_single( self.square )
		if val:
			self.set_value( val )
			#print "[" + str(self.r+1) + "][" + str(self.c+1) + "] Value " + str( val )
			return True
		return False

	def find_hidden_single(self, ssset):
		l = []
		for f in ssset:
			if f != self:
				if not f.done():
					l.extend(list(f.possible))

		s = set()
		for x in l:
			if x not in s:
				s.add(x)

		s = self.possible.difference(s)

		if len(s) == 1:
			val = s.pop()
			if val in self.possible:
				return val
		return 0

class sudoku:
	def __init__(self, game):
		self.grid, self.gridlist = self.construct_sudoku( game )
		self.stack_grid = []
		self.stack_gridlist = []

	def construct_sudoku(self, game):
		game2 = ""
		for line in game:
			game2 += line.strip()

		grid = []
		gridlist = []
		for r in xrange(9):
			grid.append([])
			row = set()
			for c in xrange(9):
				f = field(r,c,game2[r*9+c])
				grid[r].append(f)
				gridlist.append(f)
				row.add(f)
				f.add_row(row)
		for c in xrange(9):
			column = set()
			for r in xrange(9):
				f = grid[r][c]
				column.add( f )
				f.add_column(column)
		squares = []
		for i in xrange(9):
			s = set()
			squares.append(s)
		for r in xrange(9):
			for c in xrange(9):
				if r < 3 and c < 3:
					f = grid[r][c]
					squares[0].add( f )
					f.add_square( squares[0] )
				elif r < 3 and 3 <= c < 6:
					f = grid[r][c]
					squares[1].add( f )
					f.add_square( squares[1] )
				elif r < 3 and 6 <= c:
					f = grid[r][c]
					squares[2].add( f )
					f.add_square( squares[2] )
				elif 3 <= r < 6 and c < 3:
					f = grid[r][c]
					squares[3].add( f )
					f.add_square( squares[3] )
				elif 3 <= r < 6 and 3 <= c < 6:
					f = grid[r][c]
					squares[4].add( f )
					f.add_square( squares[4] )
				elif 3 <= r < 6 and 6 <= c:
					f = grid[r][c]
					squares[5].add( f )
					f.add_square( squares[5] )
				elif 6 <= r and c < 3:
					f = grid[r][c]
					squares[6].add( f )
					f.add_square( squares[6] )
				elif 6 <= r and 3 <= c < 6:
					f = grid[r][c]
					squares[7].add( f )
					f.add_square( squares[7] )
				elif 6 <= r and 6 <= c:
					f = grid[r][c]
					squares[8].add( f )
					f.add_square( squares[8] )
		for f in gridlist:
			f.init()
		return grid, gridlist

	def __str__(self):
		s = ""
		for r in xrange(9):
			for c in xrange(9):
				s += self.grid[r][c].__str__()
				if ( c == 8 ):
					s += "\n"
		return s

	def solve(self):
		update = True
		backtrack = False
		while( update == True ):
			removals = set()
			self.gridlist.sort(key=lambda field: field.no_possible())
			for f in self.gridlist:
				if not f.done() and f.no_possible() == 0:
					backtrack = True
					break
				if f.done():
					removals.add(f)
				elif f.set_single():
					removals.add(f)
				elif f.set_hidden_single():
					removals.add(f)

			# Backtrack
			if backtrack:
				if len(self.stack_grid) == 0:
					print "Nothing to backtrack from"
					update = False
					continue
				self.grid = self.stack_grid.pop()
				self.gridlist = self.stack_gridlist.pop()
				backtrack = False
				continue

			if len(removals):
				update = True
				for f in removals:
					self.gridlist.remove( f )
				if len(self.gridlist) == 0:
					update = False
			else:
				if len(self.gridlist):
					print "Guessing !!!!"
				else:
					print "Nothing to guess from.."
				r,c = self.gridlist[0].r,self.gridlist[0].c
				guess = self.gridlist[0].possible.pop()
				self.stack_grid.append(self.grid)
				self.stack_gridlist.append(self.gridlist)
				self.grid, self.gridlist = self.construct_sudoku( self.__str__() )
				self.grid[r][c].set_value( guess )
		else:
			if len(self.gridlist) > 0:
				print "NOT solved. Need " + str(len(self.gridlist)) + " fields."
				print self.__str__()
				self.possibility_grid()
			else:
				print "Solved !!"
				print self.__str__()

	def possibility_grid(self):
		s = ""
		for r in xrange(9):
			for c in xrange(9):
				s += str(self.grid[r][c].no_possible())
				if ( c == 8 ):
					s += "\n"
		print s

	def three(self):
		return str(self.grid[0][0]) + str(self.grid[0][1]) + str(self.grid[0][2])

def main(*args):
	try:
		if len(args) != 2:
			raise Exception("You need to provide an input file.")
		else:
			if os.path.isfile(args[1]):
				f = open(args[1], 'r')
				game = ""
				size = 0
				sum = 0
				for line in f:
					if line.strip().split(' ')[0] == "Grid":
						game = ""
						size = 0
					else:
						game += line.strip() + "\n"
						size += 1
						if size == 9:
							s = sudoku(game)
							print
							s.solve()
							sum += int(s.three())
				print "Sum is " + str(sum)
			else:
				raise Exception("Could not read file: " + args[1])
	except Exception as e:
		#print e
		traceback.print_exc(file=sys.stdout)
	else:
		return 0 # exit errorlessly

if __name__ == '__main__':
  sys.exit(main(*sys.argv))

#so = sudoku("003020600900305001001806400008102900700000008006708200002609500800203009005010300")
#solution = "483921657\n967345821\n251876493\n548132976\n729564138\n136798245\n372689514\n814253769\n695417382\n"
#print so
#so.solve()
#print so
#if so.__str__() == solution:
#	print "Success"
#else:
#	print "Failure"