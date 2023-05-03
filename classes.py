class Game:
	def __init__(self):
		self.playersturn = "white"
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
				kingDict[piece.color] = position
			pieceDict[piece.color].append((piece, position))
	
	def canSeeKing(self, kingpos, piecelist):
		for piece, position in piecelist:
			if piece.isValid(position, kingpos, piece.color, self.gameboard):
				return True

class Piece:
	def __init__(self, color, name):
		self.name = name
		self.position = None
		self.color = color
	
	def isValid(self, startpos, endpos, color, gameboard):
		if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, color=color):
			return True
		return False
	def __repr__(self):
		return self.name
	
	def __str__(self):
		return self.name
	
	def availableMoves(self, x, y, gameboard):
		return 0
	
	def AdNauseum(self, x, y, gameboard, color, intervals):
		answers = []
		for xint, yint in intervals:
			xtemp, ytemp = x + xint, y + yint
			while self.isInBounds(xtemp, ytemp):
				target = gameboard.get((xtemp, ytemp), None)
				if target is None:
					answers.append((xtemp, ytemp))
				elif target.color != color:
					answers.append((xtemp, ytemp))
					break
				xtemp, ytemp = xtemp + xint, ytemp + yint
		return answers
	
	def isInBounds(self, x, y):
		if x >= 0 and x < 8 and y >= 0 and y < 8:
			return True
		else:
			return False

	def noConflict(self, gameboard, initialcolor, x, y):
		if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].color != initialcolor):
			return True
		else:
			return False

class Knight(Piece):
	def knightList(self, x, y, int1, int2):
		return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2), (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]
	
	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		return [(xx, yy) for xx, yy in self.knightList(x, y, 2, 1) if self.noConflict(gameboard, color, xx, yy)]

class Rook(Piece):
	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		return self.AdNauseum(x, y, gameboard, color, [(1, 0), (0, 1), (-1, 0), (0, -1)])

class Bishop(Piece):
	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		return self.AdNauseum(x, y, gameboard, color, [(1, 1), (-1, 1), (1, -1), (-1, -1)])

class Queen(Piece):
	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		return self.AdNauseum(x, y, gameboard, color,
		                      [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (-1, 1), (1, -1), (-1, -1)])

class King(Piece):
	def kingList(self, x, y):
		return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
		        (x - 1, y - 1)]

	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		return [(xx, yy) for xx, yy in self.kingList(x, y) if self.noConflict(gameboard, color, xx, yy)]

class Pawn(Piece):
	def __init__(self, color, name, direction):
		self.name = name
		self.color = color
		self.direction = direction
	
	def availableMoves(self, x, y, gameboard, color=None):
		if color is None: color = self.color
		answers = []
		if (x + 1, y + self.direction) in gameboard and self.noConflict(gameboard, color, x + 1,
		                                                                y + self.direction): answers.append(
			(x + 1, y + self.direction))
		if (x - 1, y + self.direction) in gameboard and self.noConflict(gameboard, color, x - 1,
		                                                                y + self.direction): answers.append(
			(x - 1, y + self.direction))
		if (x, y + self.direction) not in gameboard and color == self.color: answers.append((x, y + self.direction))
		return answers


uniDict = {"white": {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
           "black": {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}}