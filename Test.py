import unittest
from classes import Game
from classes import Piece
from classes import Knight
from classes import Rook
from classes import Bishop
from classes import Queen
from classes import King
from classes import Pawn

#WHITE: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"}
#BLACK: {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}


class testCases(unittest.TestCase):
	
	'''TEST Game'''
	
	def test_black_pawn_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(0, 3)]), "♟")
		
	def test_white_pawn_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(0, 1)]), "♙")
		
	def test_black_rook_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(0, 7)]), "♜")
		
	def test_white_rook_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(0, 0)]), "♖")
		
	def test_black_knight_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(1, 7)]), "♞")

	def test_white_knight_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(1, 0)]), "♘")

	def test_black_bishop_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(2, 7)]), "♝")

	def test_white_bishop_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(2, 0)]), "♗")

	def test_black_king_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(3, 7)]), "♚")

	def test_white_king_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(4, 0)]), "♔")

	def test_black_queen_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(4, 7)]), "♛")

	def test_white_queen_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(3, 0)]), "♕")

	def test_players_turn_white_at_init(self):
		game = Game()
		self.assertTrue(game.playersturn == "white")
	
	def test_message_at_init(self):
		game = Game()
		self.assertEqual(game.message, "this is where prompts will go")
	
	'''TEST Piece'''
	def test_piece_name(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(piece.name, "nombre")
	def test_piece_color(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(piece.color, "rainbow")
	def test_piece_position(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(piece.position, None)
	#def test_piece_is_valid(self):
		#piece = Piece("rainbow", "nombre")
		#valid = piece.isValid((0, 0), (0, 1), "rainbow", {(0, 1): "♙", (0, 6): "♟", (1, 1): "♙", (1, 6): "♟", (2, 1): "♙", (2, 6): "♟", (3, 1): "♙", (3, 6): "♟", (4, 1): "♙", (4, 6): "♟", (5, 1): "♙", (5, 6): "♟", (6, 1): "♙", (6, 6): "♟", (7, 1): "♙", (7, 6): "♟", (0, 0): "♖", (7, 7): "♜", (1, 0): "♘", (6, 7): "♞", (2, 0): "♗", (5, 7): "♝", (3, 0): "♕", (4, 7): "♛", (4, 0): "♔", (3, 7): "♚", (5, 0): "♗", (2, 7): "♝", (6, 0): "♘", (1, 7): "♞", (7, 0): "♖", (0, 7): "♜"})
		#self.assertTrue(valid)
	#def test_piece_not_valid(self):
		#piece = Piece("rainbow", "nombre")
		#self.assertFalse(piece.isValid((0, 0), (0, 1), self.color, {(0, 1): "♙", (0, 6): "♟", (1, 1): "♙", (1, 6): "♟", (2, 1): "♙", (2, 6): "♟", (3, 1): "♙", (3, 6): "♟", (4, 1): "♙", (4, 6): "♟", (5, 1): "♙", (5, 6): "♟", (6, 1): "♙", (6, 6): "♟", (7, 1): "♙", (7, 6): "♟", (0, 0): "♖", (7, 7): "♜", (1, 0): "♘", (6, 7): "♞", (2, 0): "♗", (5, 7): "♝", (3, 0): "♕", (4, 7): "♛", (4, 0): "♔", (3, 7): "♚", (5, 0): "♗", (2, 7): "♝", (6, 0): "♘", (1, 7): "♞", (7, 0): "♖", (0, 7): "♜"}))
	def test_piece_is_in_bounds(self):
		piece = Piece("rainbow", "nombre")
		self.assertTrue(piece.isInBounds(1, 1))
	def test_piece_is_out_of_bounds(self):
		piece = Piece("rainbow", "nombre")
		self.assertFalse(piece.isInBounds(99, 99))
	def test_piece_repr_method(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(repr(piece), "nombre")
	def test_piece_str_method(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(str(piece), "nombre")
	def test_available_moves(self):
		piece = Piece("rainbow", "nombre")
		self.assertEqual(piece.availableMoves(1, 1, []), 0)
	
		
	'''TEST Knight'''
	def test_knight_available_moves_correct(self):
		knight = Knight("white","knight")
		self.assertEqual(knight.knightList(3,3,1,2)[0], (4,5))
	
	def test_knight_available_moves_incorrect(self):
		knight = Knight("white","knight")
		self.assertFalse(knight.knightList(3,3,1,2)[0] == (7,7))
		
	'''TEST Rook'''

	'''TEST Bishop'''
	'''TEST Queen'''
	'''TEST King'''
	def test_king_list_correct_at_init(self):
		king = King("white","king")
		self.assertEqual(king.kingList(3,0)[0], (4, 0))
		
	def test_king_available_moves_correct(self):
		king = King("rainbow", "king")
		#self.assert

	'''TEST Pawn'''
	def test_pawn_color_at_init(self):
		pawn = Pawn("rainbow", "nombre", 1)
		self.assertEqual(pawn.color, "rainbow")
	def test_pawn_color_at_init(self):
		pawn = Pawn("rainbow", "nombre", 1)
		self.assertEqual(pawn.name, "nombre")
	def test_pawn_direction_at_init(self):
		pawn = Pawn("rainbow", "nombre", 1)
		self.assertEqual(pawn.direction, 1)
	