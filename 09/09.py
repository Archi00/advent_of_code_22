#!/usr/bin/python3

import sys

with open("example.txt") as f:
  raw_mvs = f.read().split("\n")

LENGTH = 9
PADDING = LENGTH // 2
grid = []
    
init_row = LENGTH - PADDING
init_column = LENGTH - LENGTH + PADDING -1 

ctr = 0
tail_row = LENGTH - PADDING
tail_column = LENGTH - LENGTH + PADDING -1 

for i in range(LENGTH):
  grid.append([])
  for j in range(LENGTH):
    grid[i].append(".")

def right(i, j, num_mvs):
  global ctr
  global tail_column
  global tail_row
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if j - tail_column > 1:
    tail_column = j - 1
    tail_row = i
    if grid[i][tail_column] != "T":
      grid[i][tail_column] = "T"
      ctr += 1
  if num_mvs == 0:
    return (i, j)
  return right(i, j + 1, num_mvs -1)

def left(i, j, num_mvs):
  global ctr
  global tail_column
  global tail_row
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if tail_column - j > 1:
    tail_column = j + 1
    tail_row = i
    if grid[i][tail_column] != "T":
      grid[i][tail_column] = "T"
      ctr += 1
  if num_mvs == 0:
    return (i, j)
  return left(i, j - 1, num_mvs -1)

def up(i, j, num_mvs):
  global ctr
  global tail_row
  global tail_column
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if tail_row - i > 1:
    tail_row = i + 1
    tail_column = j
    if grid[tail_row][j] != "T":
      grid[tail_row][j] = "T"
      ctr += 1
  if num_mvs == 0:
    return (i, j)
  return up(i - 1, j, num_mvs -1) 

def down(i, j, num_mvs):
  global ctr
  global tail_row
  global tail_column
  if grid[i][j] == ".":
    grid[i][j] = "#"
  if i - tail_row > 1:
    tail_row = i - 1
    tail_column = j
    if grid[tail_row][j] != "T":
      grid[tail_row][j] = "T"
      ctr += 1
  if num_mvs == 0:
    return (i, j)
  return down(i + 1, j, num_mvs -1)

def render():
  for i in range(LENGTH):
    for j in range(LENGTH):
      if (i, j) == (init_row, init_column):
        grid[i][j] = "H"
      elif (i, j) == (tail_row, tail_column):
        grid[tail_row][tail_column] = "T"
      else:
        grid[i][j] = "."
  for cell in grid:
    print(cell)
  print()
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
  render()

  grid[LENGTH-PADDING][LENGTH - LENGTH + PADDING - 1] = "S"
