from Test import unitTestCases
from Test import integrationTestCases

'''This file contains both Unit and Integration Tests'''

'''instantiate unit_test object'''
unit_test = unitTestCases()


'''TEST Game'''
unit_test.test_black_pawn_at_init()
unit_test.test_white_pawn_at_init()
unit_test.test_black_rook_at_init()
unit_test.test_white_rook_at_init()
unit_test.test_black_knight_at_init()
unit_test.test_white_knight_at_init()
unit_test.test_black_bishop_at_init()
unit_test.test_white_bishop_at_init()
unit_test.test_black_king_at_init()
unit_test.test_white_king_at_init()
unit_test.test_black_queen_at_init()
unit_test.test_white_queen_at_init()
unit_test.test_players_turn_white_at_init()

'''TEST Piece'''
unit_test.test_piece_name()
unit_test.test_piece_color()
unit_test.test_piece_position()
unit_test.test_piece_is_in_bounds()
unit_test.test_piece_is_out_of_bounds()
unit_test.test_piece_conflict()
unit_test.test_piece_repr_method()
unit_test.test_piece_str_method()
unit_test.test_available_moves()

'''TEST Knight'''
unit_test.test_knight_available_moves_correct()

unit_test.test_knight_available_moves_incorrect()
unit_test.test_knight_valid_move()
'''TEST Rook'''
unit_test.test_rook_color_at_init()
unit_test.test_rook_color_at_init()
unit_test.test_rook_valid_move()

'''TEST Bishop'''
unit_test.test_bishop_color_at_init()
unit_test.test_bishop_color_at_init()
unit_test.test_bishop_valid_move()

'''TEST Queen'''
unit_test.test_queen_color_at_init()
unit_test.test_queen_color_at_init()
unit_test.test_queen_valid_move()

'''TEST King'''
unit_test.test_king_color_at_init()
unit_test.test_king_color_at_init()
unit_test.test_king_valid_move()

'''TEST Pawn'''
unit_test.test_pawn_color_at_init()
unit_test.test_pawn_color_at_init()
unit_test.test_pawn_direction_at_init()

''''''
'''Instantiate integration_test object'''
integration_test = integrationTestCases()

'''Execute integration tests'''
integration_test.test_rook_available_moves_at_game_init()
integration_test.test_knight_available_moves_at_game_init()
integration_test.test_bishop_available_moves_at_game_init()
integration_test.test_queen_available_moves_at_game_init()
integration_test.test_king_available_moves_at_game_init()
