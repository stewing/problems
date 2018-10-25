#!/usr/local/bin/python3


def mark_ship(board, ix, ij):
    if board[ix][ij] == 'X':
        board[ix][ij] = 'V'
    else:
        return
    if ix > 0:
        mark_ship(board, ix - 1, ij)
    if ij > 0:
        mark_ship(board, ix, ij - 1)
    if ix < len(board) - 1:
        mark_ship(board, ix + 1, ij)
    if ij < len(board[ix]) - 1:
        mark_ship(board, ix, ij + 1)


def count_ships(board):
    ships = 0
    for ix in range(len(board)):
        for ij in range(len(board[ix])):
            if board[ix][ij] == 'X':
                ships = ships + 1
                mark_ship(board, ix, ij)
    return ships


board01 = [
        [ 'X', 'X', 'X', '.', '.'],
        [ '.', '.', '.', '.', 'X'],
        [ '.', '.', '.', '.', 'X'],
        [ 'X', 'X', 'X', '.', '.']
        ]

print("board01 has {} ships".format(count_ships(board01)))

board02 = [
        [ '.', '.', '.', '.', '.'],
        [ '.', '.', '.', '.', '.'],
        [ '.', '.', '.', '.', '.'],
        [ '.', '.', '.', '.', '.']
        ]

print("board02 has {} ships".format(count_ships(board02)))

board03 = [
        [ 'X', 'X', 'X', '.', 'X'],
        [ '.', '.', '.', '.', '.'],
        [ '.', '.', '.', 'X', 'X'],
        [ 'X', 'X', 'X', '.', '.']
        ]

print("board03 has {} ships".format(count_ships(board03)))

board04 = [
        [ 'X', '.', '.', '.', '.'],
        [ '.', 'X', '.', '.', '.'],
        [ '.', '.', 'X', '.', 'X'],
        [ '.', '.', '.', 'X', '.']
        ]

print("board04 has {} ships".format(count_ships(board04)))

board05 = [
        [ 'X', '.', 'X', '.', '.'],
        [ 'X', '.', '.', 'X', 'X'],
        [ 'X', '.', '.', '.', '.'],
        [ 'X', '.', 'X', '.', '.']
        ]

print("board05 has {} ships".format(count_ships(board05)))
