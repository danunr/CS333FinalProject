'''
created by Github user: rsheldiii
source: https://gist.github.com/rsheldiii/2993225
'''

from classes import Game
from classes import Piece
from classes import Knight
from classes import Rook
from classes import Bishop
from classes import Queen
from classes import King
from classes import Pawn
import time


def printBoard(game):
	print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
	for i in range(0, 8):
		print("-" * 32)
		print(chr(i + 97), end="|")
		for j in range(0, 8):
			item = game.gameboard.get((i, j), " ")
			print(str(item) + ' |', end=" ")
		print()
	print("-" * 32)

def parseInput():
	try:
		a, b = input().split()
		a = ((ord(a[0]) - 97), int(a[1]) - 1)
		b = (ord(b[0]) - 97, int(b[1]) - 1)
		print(a, b)
		return (a, b)
	except:
		return ((-1, -1), (-1, -1))

def main():
	game = Game()
	
	while True:
		printBoard(game)
		startpos, endpos = parseInput()
		try:
			target = game.gameboard[startpos]
		except:
			target = None
		
		if target:
			print("found " + str(target))
			if target.color != game.playersturn:
				continue
			if target.isValid(startpos, endpos, target.color, game.gameboard):
				game.gameboard[endpos] = game.gameboard[startpos]
				del game.gameboard[startpos]
				game.isCheck()
				if game.playersturn == "black":
					game.playersturn = "white"
				else:
					game.playersturn = "black"
			else:
				print(target.availableMoves(startpos[0], startpos[1], game.gameboard))
		else:
			pass
main()