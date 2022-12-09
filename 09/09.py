#!/usr/bin/python3

with open("example.txt") as f:
  raw_mvs = f.read().split("\n")

LENGTH = 25
PADDING = LENGTH // 2
grid = []
    
init_row = LENGTH - PADDING
init_column = LENGTH - LENGTH + PADDING -1 

for i in range(LENGTH):
  grid.append([])
  for j in range(LENGTH):
    grid[i].append(".")

def right(i, j, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if num_mvs == 0:
    return (i, j)
  return right(i, j + 1, num_mvs -1)

def left(i, j, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if num_mvs == 0:
    return (i, j)
  return left(i, j - 1, num_mvs -1)

def up(i, j, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if num_mvs == 0:
    return (i, j)
  return up(i - 1, j, num_mvs -1) 

def down(i, j, num_mvs):
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if num_mvs == 0:
    return (i, j)
  return down(i + 1, j, num_mvs -1)

for mvs in raw_mvs: 
  direction, mv = mvs.split()
  if direction == "R":
    (init_row, init_column) = right(init_row, init_column, int(mv))
  if direction == "L":
    (init_row, init_column) = left(init_row, init_column, int(mv))
  if direction == "U":
    (init_row, init_column) = up(init_row, init_column, int(mv))
  if direction == "D":
    (init_row, init_column) = down(init_row, init_column, int(mv))

grid[LENGTH-PADDING][LENGTH - LENGTH + PADDING - 1] = "S"

for cell in grid:
  print(cell)
