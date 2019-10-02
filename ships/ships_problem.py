"""
Ship Counting.

Count the ships on the given board. Your function must
take a matrix and return the number of ships present. The
board is composed of squares marked with "X" or "." only.

Ships are represented by a vertical or horizontal sequence
of "X" characters.

Water is represented by a period (".").

Ships may not be directly above, below or side-by-side.
They may be diagonally adjacent. Here are example boards:

Valid:

     0 1 2 3

  0  X X . X
  1  . . . X
  2  X . X .
  3  X . X .

  Result: 4

Invalid:

     0 1 2 3 4

  0  X X X . .
  1  . . X X X
  2  . . . . .

Your code *does not* need to handle invalid boards in any way.

"""

def count_ships(b) -> int:
  """
  Count the number of ships in the given matrix.

  Return:
    An integer, the number of ships in the matrix.
  """


board = [
        [ 'X', 'X', 'X', '.', '.'],
        [ '.', '.', '.', '.', 'X'],
        [ '.', '.', '.', '.', 'X'],
        [ 'X', 'X', 'X', '.', '.']
        ]

print("board has {} ships".format(count_ships(board)))
