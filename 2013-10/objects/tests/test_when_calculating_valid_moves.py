def test_initial_valid_moves_should_be_twelve_and_fifteen(puzzle):
    assert ['12', '15'] == sorted(puzzle.valid_moves, key=int)


def test_valid_after_horizontal_move(puzzle):
    puzzle.move(15)

    assert ['11', '14', '15'] == sorted(puzzle.valid_moves, key=int)


def test_valid_after_vertical_move(puzzle):
    puzzle.move(12)

    assert ['8', '11', '12'] == sorted(puzzle.valid_moves, key=int)


def test_valid_after_move_sequence(puzzle):
    puzzle.move(12)
    puzzle.move(11)
    puzzle.move(10)
    puzzle.move(6)

    assert ['2', '5', '6', '7'] == sorted(puzzle.valid_moves, key=int)
