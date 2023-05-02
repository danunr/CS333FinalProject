from TestUnit import testCases

test_case = testCases()

'''test Game'''
test_case.test_black_pawn_at_init()
test_case.test_white_pawn_at_init()
test_case.test_black_rook_at_init()
test_case.test_white_rook_at_init()
test_case.test_black_knight_at_init()
test_case.test_white_knight_at_init()
test_case.test_black_bishop_at_init()
test_case.test_white_bishop_at_init()
test_case.test_black_king_at_init()
test_case.test_white_king_at_init()
test_case.test_black_queen_at_init()
test_case.test_white_queen_at_init()
test_case.test_players_turn_white_at_init()
test_case.test_message_at_init()

'''test Piece'''
test_case.test_piece_name()
test_case.test_piece_color()
test_case.test_piece_position()
test_case.test_piece_is_in_bounds()
test_case.test_piece_is_out_of_bounds()
test_case.test_piece_repr_method()
test_case.test_piece_str_method()
test_case.test_available_moves()


test_case.test_knight_available_moves_correct()
test_case.test_king_list_correct_at_init()
test_case.test_pawn_color_at_init()
test_case.test_pawn_color_at_init()
test_case.test_pawn_direction_at_init()
