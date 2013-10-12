# coding: utf-8

"""15-puzzle 

Simple 15 puzzle game. 
"""

import random


class Puzzle(object):
    """Represents a "15-puzzle"
    
    ``size`` is the width and height of the puzzle, supporting puzzles
    with dimensions other than 4x4
    
    >>> print(Puzzle())
    1   2   3   4
    5   6   7   8
    9   10  11  12
    13  14  15  _

    >>> print(Puzzle(2))
    1   2
    3   _
    """
    def __init__(self, size=4):
        self._size = size
        
        self._puzzle = []
        for row in range(self._size):
            row_start = row * self._size
            self._puzzle.append(map(str, range(row_start + 1, 
                                               row_start + 1 + self._size)))

        self._puzzle[-1][-1] = "_" 
        
    def __str__(self):
        return "\n".join(["\t".join(row) for row in self._puzzle])
        
    def move(self, row, column):
        """Move by sliding from the given square toward the empty space.
        
        >>> print(Puzzle(2).move(1,0))
        1   2
        _   3
        
        >>> print(Puzzle(2).move(0,1))
        1   _
        3   2
        
        >>> print(Puzzle(2).move(0,1).move(0,0).move(1,0))
        3   1
        _   2
        
        >>> print(Puzzle(2).move(0,0))
        Traceback (most recent call last):
            ...
        ValueError: locked square at (0, 0)
        """
        if "_" in self._puzzle[row]:
            return self._move_on_row(row, column)
        
        # transpose rows and columns
        puzzle = map(list, zip(*self._puzzle))
        
        if "_" in puzzle[column]:
            self._puzzle = puzzle
            self._move_on_row(column, row)
            self._puzzle = map(list, zip(*self._puzzle))
        else:
            raise ValueError("locked square at " + str( (row, column) ))
        
        return self
        
    def _move_on_row(self, row, column):
        """Move row-wise by sliding the given square toward the empty space.
        
        >>> print(Puzzle(2)._move_on_row(1,0))
        1   2
        _   3
        
        >>> print(Puzzle(3)._move_on_row(2,0)._move_on_row(2,1))
        1   2   3
        4   5   6
        7   _   8

        >>> print(Puzzle(2)._move_on_row(0,0))
        Traceback (most recent call last):
            …
        ValueError: list.remove(x): x not in list
        """
        self._puzzle[row].remove("_")
        self._puzzle[row].insert(column, "_")
        
        return self
    
    def valid_moves(self):
        """List the currently valid moves.
        
        >>> sorted(Puzzle(2).valid_moves()) == [(0, 1), (1, 0)]
        True
        
        >>> sorted(Puzzle(3).valid_moves()) == [(0, 2), (1, 2), \
                                                (2, 0), (2, 1)]
        True
        
        >>> sorted(Puzzle(3).move(1,2).move(1,1).valid_moves()) == \
                                               [(0, 1), (1, 0), \
                                                (1, 2), (2, 1)]
        True
        """
        for index, row in enumerate(self._puzzle):
            if "_" in row:
                _column_index = row.index("_")
                _row_index = index
                break
        
        row_moves = [(_row_index, column) 
                     for column in range(self._size)
                     if self._puzzle[_row_index][column] != "_"]
                     
        column_moves = [(row, _column_index)
                        for row in range(self._size)
                        if row != _row_index]
                     
        return row_moves + column_moves
        
    def shuffle(self, iterations=100):
        """Shuffle the puzzle"""
        
        for iteration in xrange(iterations):
            move = random.choice(self.valid_moves())
            self.move(*move)
            
        return self
        
    def is_solved(self):
        """Is the puzzle solved?
        
        >>> Puzzle().is_solved()
        True
        
        >>> Puzzle().shuffle(1).is_solved()
        False
        
        >>> Puzzle(5).is_solved()
        True
        
        >>> Puzzle(3).move(0,2).is_solved()
        False
        
        """
        
        return self._puzzle == Puzzle(self._size)._puzzle
    
# ====================================================================
# doctest test harness

def _test(_verbose=False):
    import doctest
    doctest.testmod(verbose=_verbose, optionflags=(doctest.ELLIPSIS |
                                            #doctest.REPORT_NDIFF |
                                            doctest.NORMALIZE_WHITESPACE))

# ====================================================================
# test stub: run doctests if this file is run directly

if __name__ == "__main__":
    _test()
    
    for size in [2, 3, 3, 4, 5, 10]:
        puzzle = Puzzle(size)
        puzzle.shuffle(1000 * size)
        print(puzzle)
        print("")
