from fifteen_puzzle import Puzzle

import pytest


def test_should_succeed():
    Puzzle()


def test_default_size_should_be_4(puzzle):
    assert 4 == puzzle.size


@pytest.mark.parametrize('size', (2, 3, 5))
def test_can_set_puzzle_size(size):
    assert size == Puzzle(size).size


def test_new_puzzle_should_be_solved(puzzle):
    assert puzzle.is_solved


@pytest.mark.parametrize(
    ('location', 'value'),
    [
        ((0, 0), '1'),
        ((0, 1), '2'),
        ((0, 2), '3'),
        ((0, 3), '4'),
        ((1, 0), '5'),
        ((1, 1), '6'),
        ((1, 2), '7'),
        ((1, 3), '8'),
        ((2, 0), '9'),
        ((2, 1), '10'),
        ((2, 2), '11'),
        ((2, 3), '12'),
        ((3, 0), '13'),
        ((3, 1), '14'),
        ((3, 2), '15'),
    ]
)
def test_new_puzzle_should_be_in_order(puzzle, location, value):
    assert location == puzzle.coordinates_for(value)


def test_new_puzzle_empty_should_be_bottom_right(puzzle):
    assert (3, 3) == puzzle.coordinates_for('_')
