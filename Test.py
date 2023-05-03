import unittest
from classes import *


'''This file contains classes for '''
class unitTestCases(unittest.TestCase):
	
	'''TEST Game'''
	def test_black_pawn_at_init(self):
		game = Game()
		self.assertEqual(str(game.gameboard[(0, 6)]), "♟")
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
	def test_piece_conflict(self):
		piece = Piece("rainbow", "nombre")
		self.assertFalse(piece.noConflict([], "rainbow", 9, 9))
	#def test_piece_no_conflict(self):
		#piece = Piece("rainbow", "nombre")
		#self.assertTrue(piece.noConflict("white", 0, 0))
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
	def test_knight_valid_move(self):
		knight = Knight("rainbow", "nombre")
		valid = knight.availableMoves(0, 3, {}, knight.color)
		self.assertTrue(valid)

	'''TEST Rook'''
	def test_rook_color_at_init(self):
		rook = Rook("rainbow", "nombre")
		self.assertEqual(rook.color, "rainbow")
	def test_rook_color_at_init(self):
		rook = Rook("rainbow", "nombre")
		self.assertEqual(rook.name, "nombre")
	def test_rook_valid_move(self):
		rook = Rook("rainbow", "nombre")
		valid = rook.availableMoves(0, 3, {}, rook.color)
		self.assertTrue(valid)

	'''TEST Bishop'''
	def test_bishop_color_at_init(self):
		bishop = Bishop("rainbow", "nombre")
		self.assertEqual(bishop.color, "rainbow")
	def test_bishop_color_at_init(self):
		bishop = Bishop("rainbow", "nombre")
		self.assertEqual(bishop.name, "nombre")
	def test_bishop_valid_move(self):
		bishop = Bishop("rainbow", "nombre")
		valid = bishop.availableMoves(0, 3, {}, bishop.color)
		self.assertTrue(valid)

	'''TEST Queen'''
	def test_queen_color_at_init(self):
		queen = Queen("rainbow", "nombre")
		self.assertEqual(queen.color, "rainbow")
	def test_queen_color_at_init(self):
		queen = Queen("rainbow", "nombre")
		self.assertEqual(queen.name, "nombre")
	def test_queen_valid_move(self):
		queen = Queen("rainbow", "nombre")
		valid = queen.availableMoves(0, 3, {}, queen.color)
		self.assertTrue(valid)

	'''TEST King'''
	def test_king_color_at_init(self):
		king = King("rainbow", "nombre")
		self.assertEqual(king.color, "rainbow")
	def test_king_color_at_init(self):
		king = King("rainbow", "nombre")
		self.assertEqual(king.name, "nombre")
	def test_king_valid_move(self):
		king = King("rainbow", "nombre")
		valid = king.availableMoves(0, 3, {}, king.color)
		self.assertTrue(valid)

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


class integrationTestCases(unittest.TestCase):
	def test_rook_available_moves_at_game_init(self):
		rook = Rook("white", "rook")
		game = Game()
		self.assertEqual(rook.availableMoves(0,0,game.gameboard,rook.color), [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
	def test_knight_available_moves_at_game_init(self):
		knight = Knight("white", "knight")
		game = Game()
		self.assertEqual(knight.availableMoves(0,0,game.gameboard,knight.color), [(1, 2)])
	def test_bishop_available_moves_at_game_init(self):
		bishop = Bishop("white", "rook")
		game = Game()
		self.assertEqual(bishop.availableMoves(0,0,game.gameboard,bishop.color), [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
	def test_queen_available_moves_at_game_init(self):
		queen = Queen("white", "queen")
		game = Game()
		self.assertEqual(queen.availableMoves(0,0,game.gameboard,queen.color), [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
	def test_king_available_moves_at_game_init(self):
		king = King("white", "rook")
		game = Game()
		self.assertEqual(king.availableMoves(0,0,game.gameboard,king.color), [])