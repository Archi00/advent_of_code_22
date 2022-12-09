#!/usr/bin/python3

with open("input.txt") as f:
  raw_mvs = f.read().split("\n")

LENGTH = 500
PADDING = LENGTH // 2
grid = []
    
init_row = LENGTH - PADDING
init_column = LENGTH - LENGTH + PADDING -1 

tail_row = LENGTH - PADDING
tail_column = LENGTH - LENGTH + PADDING -1 

for i in range(LENGTH):
  grid.append([])
  for j in range(LENGTH):
    grid[i].append(".")

r = []

def tail_right(tail_column, j):
  grid[tail_row][tail_column + 1] = "T"

def tail_left(tail_column, j):
  grid[tail_row][tail_column - 1] = "T"

def tail_up(tail_row, i):
  grid[tail_row - 1][tail_column] = "T"

def tail_down(tail_row, i):
  grid[tail_row + 1][tail_column] = "T"



def right(i, j, tail_column, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if j - tail_column > 1:
    tail_right(tail_column, j)
    r.append(0)
  if j - tail_column > 2:
    tail_column += 1
    tail_right(tail_column, j)
  if num_mvs == 0:
    return (i, j, tail_column + 1)
  return right(i, j + 1, tail_column, num_mvs -1)

def left(i, j, tail_column, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if tail_column - j > 1:
    tail_left(tail_column, j)
    r.append(0)
  if tail_column - j > 2:
    tail_column -= 1
    tail_left(tail_column, j)
  if num_mvs == 0:
    return (i, j, tail_column - 1)
  return left(i, j - 1, tail_column, num_mvs - 1)

def up(i, j, tail_row, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if tail_row - i > 1:
    tail_up(tail_row, i)
    r.append(0)
  if tail_row - i > 2:
    tail_row -= 1
    tail_up(tail_row, i)
  if num_mvs == 0:
    return (i, j, tail_row -1)
  return up(i - 1, j, tail_row, num_mvs -1) 

def down(i, j, tail_row, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if i - tail_row > 1:
    tail_down(tail_row, i)
    r.append(0)
  if i - tail_row > 2:
    tail_row += 1
    tail_down(tail_row, i)
  if num_mvs == 0:
    return (i, j, tail_row + 1)
  return down(i + 1, j, tail_row, num_mvs -1)

for mvs in raw_mvs: 
  direction, mv = mvs.split()
  if direction == "R":
    (init_row, init_column, tail_column) = right(init_row, init_column, tail_column, int(mv))
  if direction == "L":
    (init_row, init_column, tail_column) = left(init_row, init_column, tail_column, int(mv))
  if direction == "U":
    (init_row, init_column, tail_row) = up(init_row, init_column, tail_row, int(mv))
  if direction == "D":
    (init_row, init_column, tail_row) = down(init_row, init_column, tail_row, int(mv))

grid[LENGTH-PADDING][LENGTH - LENGTH + PADDING - 1] = "S"

for cell in grid:
  print(cell)

print(len(r))
