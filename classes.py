class Game:
	def __init__(self):
		self.playersturn = "white"
		self.message = "this is where prompts will go"
		self.gameboard = {}
		self.placePieces()
	
	def placePieces(self):
		
		for i in range(0, 8):
			self.gameboard[(i, 1)] = Pawn("white", uniDict["white"][Pawn], 1)
			self.gameboard[(i, 6)] = Pawn("black", uniDict["black"][Pawn], -1)
		
		placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
		
		for i in range(0, 8):
			self.gameboard[(i, 0)] = placers[i]("white", uniDict["white"][placers[i]])
			self.gameboard[((7 - i), 7)] = placers[i]("black", uniDict["black"][placers[i]])
		placers.reverse()
	
	def isCheck(self):
		king = King
		kingDict = {}
		pieceDict = {"black": [], "white": []}
		for position, piece in self.gameboard.items():
			if type(piece) == King:
				kingDict[piece.Color] = position
			print(piece)
			pieceDict[piece.Color].append((piece, position))
		if self.canSeeKing(kingDict["white"], pieceDict["black"]):
			self.message = "White player is in check"
		if self.canSeeKing(kingDict["black"], pieceDict["white"]):
			self.message = "Black player is in check"
	
	def canSeeKing(self, kingpos, piecelist):
		for piece, position in piecelist:
			if piece.isValid(position, kingpos, piece.Color, self.gameboard):
				return True
		return False
	
	def parseInput(self):
		try:
			a, b = input().split()
			a = ((ord(a[0]) - 97), int(a[1]) - 1)
			b = (ord(b[0]) - 97, int(b[1]) - 1)
			print(a, b)
			return (a, b)
		except:
			return ((-1, -1), (-1, -1))
	
	def printBoard(self):
		print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
		for i in range(0, 8):
			print("-" * 32)
			print(chr(i + 97), end="|")
			for j in range(0, 8):
				item = self.gameboard.get((i, j), " ")
				print(str(item) + ' |', end=" ")
			print()
		print("-" * 32)


class Piece:
	
	def __init__(self, color, name):
		self.name = name
		self.position = None
		self.color = color
	
	def isValid(self, startpos, endpos, Color, gameboard):
		if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
			return True
		return False
	
	def __repr__(self):
		return self.name
	
	def __str__(self):
		return self.name
	
	def availableMoves(self, x, y, gameboard):
		return 0
	
	def AdNauseum(self, x, y, gameboard, Color, intervals):
		answers = []
		for xint, yint in intervals:
			xtemp, ytemp = x + xint, y + yint
			while self.isInBounds(xtemp, ytemp):
				target = gameboard.get((xtemp, ytemp), None)
				if target is None:
					answers.append((xtemp, ytemp))
				elif target.Color != Color:
					answers.append((xtemp, ytemp))
					break
				else:
					break
				xtemp, ytemp = xtemp + xint, ytemp + yint
		return answers
	
	def isInBounds(self, x, y):
		if x >= 0 and x < 8 and y >= 0 and y < 8:
			return True
		return False
	
	def noConflict(self, gameboard, initialColor, x, y):
		if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor): return True
		return False


class Knight(Piece):
	def knightList(self, x, y, int1, int2):
		"""sepcifically for the rook, permutes the values needed around a position for noConflict tests"""
		return [(x + int1, y + int2), (x - int1, y + int2),
		        (x + int1, y - int2), (x - int1, y - int2),
		        (x + int2, y + int1), (x - int2, y + int1),
		        (x + int2, y - int1), (x - int2, y - int1)]
	
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		return [(xx, yy) for xx, yy in self.knightList(x, y, 2, 1) if self.noConflict(gameboard, Color, xx, yy)]


class Rook(Piece):
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		return self.AdNauseum(x, y, gameboard, Color, [(1, 0), (0, 1), (-1, 0), (0, -1)])


class Bishop(Piece):
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		return self.AdNauseum(x, y, gameboard, Color, [(1, 1), (-1, 1), (1, -1), (-1, -1)])


class Queen(Piece):
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		return self.AdNauseum(x, y, gameboard, Color,
		                      [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (-1, 1), (1, -1), (-1, -1)])


class King(Piece):
	def kingList(self, x, y):
		return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
		        (x - 1, y - 1)]
	
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		return [(xx, yy) for xx, yy in kingList(x, y) if self.noConflict(gameboard, Color, xx, yy)]


class Pawn(Piece):
	def __init__(self, color, name, direction):
		self.name = name
		self.Color = color
		self.direction = direction
	
	def availableMoves(self, x, y, gameboard, Color=None):
		if Color is None: Color = self.Color
		answers = []
		if (x + 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x + 1,
		                                                                y + self.direction): answers.append(
			(x + 1, y + self.direction))
		if (x - 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x - 1,
		                                                                y + self.direction): answers.append(
			(x - 1, y + self.direction))
		if (x, y + self.direction) not in gameboard and Color == self.Color: answers.append((x, y + self.direction))
		return answers


uniDict = {"white": {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
           "black": {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}}