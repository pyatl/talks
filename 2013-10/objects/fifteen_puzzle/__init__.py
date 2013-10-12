import networkx as nx


class Puzzle(object):
    """Represents a 15-puzzle

    ``size`` is the width and height of the puzzle, supporting puzzles with
    dimensions other than 4x4.

    """

    def __init__(self, size=4):
        self.size = size
        self._puzzle = nx.grid_2d_graph(size, size)

        # Label each node with its tile value, e.g. (0, 0) is tile '1' in the
        # upper left.  add_node is a NetworkX graph method to update an
        # existing node,  in this case by setting its 'value'
        for value, coordinates in enumerate(sorted(self._puzzle), 1):
            self._puzzle.add_node(coordinates, value=str(value))

        # Label the empty tile
        self._puzzle.add_node((size-1, size-1), value='_')

    @property
    def is_solved(self):
        """Indicate whether the puzzle is in a solved state"""

        # TODO: implementation left as an exercise
        return True

    def coordinates_for(self, value):
        """Determine the coordinates for the specified number value

        Returns a 2-tuple representing the coordinates for the given value,
        with (0, 0) representing the top left corner of the puzzle.

        """

        for node in self._puzzle:
            if self._puzzle.node[node]['value'] == str(value):
                return node

    def move(self, value):
        """Move a tile by sliding it to the empty square.

        Raises ValueError if the requested tile is locked in place.

        """

        empty = self.coordinates_for('_')
        origin = self.coordinates_for(value)

        if empty not in self._puzzle.neighbors(origin):
            raise ValueError('locked square at ' + str(origin))

        # "move" the tile by swapping its value with the empty tiles
        self._puzzle.add_node(empty, value=str(value))
        self._puzzle.add_node(origin, value='_')

    @property
    def valid_moves(self):
        """List of currently valid moves, returned as tile labels, e.g.

            ['15', '12']

        """

        empty = self.coordinates_for('_')

        return [self._puzzle.node[node]['value']
                for node in self._puzzle.neighbors(empty)]

    # TODO: __str__ and shuffle left as an exercise
