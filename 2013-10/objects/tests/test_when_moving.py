import pytest


def test_valid_horizontal_move_should_succeed(puzzle):
    puzzle.move(15)


def test_valid_horizontal_move_should_update_tile_coordinates(puzzle):
    old_empty = puzzle.coordinates_for('_')
    puzzle.move(15)

    assert old_empty == puzzle.coordinates_for(15)


def test_valid_horizontal_move_should_update_empty_tile_coordinates(puzzle):
    origin = puzzle.coordinates_for(15)
    puzzle.move(15)

    assert origin == puzzle.coordinates_for('_')


def test_valid_vertical_move_should_succeed(puzzle):
    puzzle.move(12)


def test_valid_vertical_move_should_update_tile_coordinates(puzzle):
    old_empty = puzzle.coordinates_for('_')
    puzzle.move(12)

    assert old_empty == puzzle.coordinates_for(12)


def test_valid_vertical_move_should_update_empty_tile_coordinates(puzzle):
    origin = puzzle.coordinates_for(12)
    puzzle.move(12)

    assert origin == puzzle.coordinates_for('_')


@pytest.mark.parametrize('invalid', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14))
def test_invalid_move_should_raise(puzzle, invalid):
    with pytest.raises(ValueError):
        puzzle.move(invalid)


@pytest.mark.parametrize(
    ('first', 'second'),
    [
        (15, 15),
        (15, 14),
        (15, 11),
        (12, 12),
        (12, 11),
        (12, 8),
    ]
)
def test_move_sequence_should_succeed(puzzle, first, second):
    puzzle.move(first)
    puzzle.move(second)


@pytest.mark.parametrize(
    ('first', 'invalid'),
    [
        (15, 13),
        (15, 10),
        (15, 12),
        (12, 15),
        (12, 10),
        (12, 4),
    ]
)
def test_move_sequence_with_second_invalid_should_fail(puzzle, first, invalid):
    puzzle.move(first)

    with pytest.raises(ValueError):
        puzzle.move(invalid)
