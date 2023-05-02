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



def main():
	print("TEST FOR CLASS")
	time.sleep(50)


	game = Game()
	
	while True:
		game.printBoard()
		print(game.message)
		game.message = ""
		startpos, endpos = game.parseInput()
		try:
			target = game.gameboard[startpos]
		except:
			game.message = "could not find piece; index probably out of range"
			target = None
		
		if target:
			print("found " + str(target))
			if target.Color != game.playersturn:
				game.message = "you aren't allowed to move that piece this turn"
				continue
			if target.isValid(startpos, endpos, target.Color, game.gameboard):
				game.message = "that is a valid move"
				game.gameboard[endpos] = game.gameboard[startpos]
				del game.gameboard[startpos]
				game.isCheck()
				if game.playersturn == "black":
					game.playersturn = "white"
				else:
					game.playersturn = "black"
			else:
				game.message = "invalid move" + str(target.availableMoves(startpos[0], startpos[1], game.gameboard))
				print(target.availableMoves(startpos[0], startpos[1], game.gameboard))
		else:
			game.message = "there is no piece in that space"

main()