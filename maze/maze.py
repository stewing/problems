#!/usr/local/bin/python3

from pprint import pprint

maze = [[1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1]]

def print_board(m, x, y):
    print(f"pos: {x}, {y}")
    for xidx in range(len(m)):
        for yidx in range(len(m[xidx])):
            print(' ', end='')
            if xidx == x and yidx == y:
                print('*', end='')
                print(m[xidx][yidx], end='')
            else:
                print(' ', end='')
                print(m[xidx][yidx], end='')
        print()

def mark_square(m, x, y, len_x, len_y, path):

    if m[x][y] == 0:
        return False

    if m[x][y] == 'v':
        return False

    m[x][y] = 'v'

    if x+1 < len_x:
        if mark_square(m, x+1, y, len_x, len_y, path):
            m[x][y] = '#'
            path.insert(0, 'D')
            return True

    if y+1 < len_y:
        if mark_square(m, x, y+1, len_x, len_y, path):
            m[x][y] = '#'
            path.insert(0, 'R')
            return True

    if x-1 >= 0:
        if mark_square(m, x-1, y, len_x, len_y, path):
            m[x][y] = '#'
            path.insert(0, 'U')
            return True

    if y-1 >= 0:
        if mark_square(m, x, y-1, len_x, len_y, path):
            m[x][y] = '#'
            path.insert(0, 'L')
            return True

    if x == len_x - 1 and y == len_y - 1:
        m[x][y] = '#'
        return True

    return False


def solve_maze(m, startx, starty):
    if m[startx][starty] == 0:
        return None
    len_x = len(m)
    len_y = len(m[0])
    path = []
    if mark_square(m, startx, starty, len_x, len_y, path):
        print(f"path exists: {path}")
        print_board(m, startx, starty)
    else:
        print("no path exists")

solve_maze(maze, 0, 0)

maze2 = [[1,0,0,0,1,0,0,0],
         [1,1,0,1,1,1,0,1],
         [0,1,0,0,0,1,0,0],
         [1,1,1,1,1,1,1,1]]

solve_maze(maze2, 0, 0)

maze3 = [[1,0,0,0,1,0,0,0],
         [1,1,1,1,1,1,0,1],
         [0,1,0,0,0,1,0,0],
         [1,1,1,1,0,1,1,1]]

solve_maze(maze3, 0, 0)

maze4 = [[1,0,0,0,1,0,0,0],
         [1,1,1,1,1,1,0,1],
         [0,1,0,0,0,1,0,0],
         [1,1,1,1,0,1,1,1]]

solve_maze(maze4, 0, 4)

maze5 = [[1,0,0,0],
         [1,1,0,1],
         [0,1,0,0],
         [1,1,1,1]]

solve_maze(maze5, 1, 3)

maze6 = [[1,0,0,0,1,0,0,0],
         [1,1,0,1,1,1,0,1],
         [0,1,0,1,0,1,0,0],
         [1,1,1,1,0,1,1,1]]

solve_maze(maze6, 0, 0)
