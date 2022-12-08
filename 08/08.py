#!/usr/bin/python3
with open("input.txt") as f:
  grid_rows = f.read().split("\n")

vis = []
top_bottom = grid_rows[0] + grid_rows[-1]
vis.append(top_bottom)
for row in grid_rows[1:-1]:
  vis.append(row[0])
  vis.append(row[-1])

def top(i, j, iy):
  if iy == 0:
    if grid_rows[i][j] > grid_rows[iy][j]:
      # return True
      return i
  if grid_rows[i][j] > grid_rows[iy][j]:
    return top(i, j, iy-1)
  else:
    # return False
    return i - iy

def bottom(i, j, iy):
  if iy == len(grid_rows) - 1:
    if grid_rows[i][j] > grid_rows[iy][j]:
      # return True
      return iy - i
  if grid_rows[i][j] > grid_rows[iy][j]:
    return bottom(i, j, iy + 1)
  else:
    # return False
    return iy - i

def right(i, j, jy):
  if jy == len(grid_rows) - 1:
    if grid_rows[i][j] > grid_rows[i][jy]:
      # return True
      return jy - j
  if grid_rows[i][j] > grid_rows[i][jy]:
    return right(i, j, jy + 1)
  else:
    # return False
    return jy - j

def left(i, j, jy):
  if jy == 0:
    if grid_rows[i][j] > grid_rows[i][jy]:
      # return True
      return j
  if grid_rows[i][j] > grid_rows[i][jy]:
    return left(i, j, jy - 1)
  else:
    # return False
    return j - jy

r2 = []
for i in range(len(grid_rows)):
  for j in range(len(grid_rows)):
    if i > 0 and i < len(grid_rows) -1 and j > 0 and j < len(grid_rows) -1:
      print(f"idx: {i} j_idx: {j}")
      print(grid_rows[i][j])
      top_trees = top(i, j, i-1)
      bottom_trees = bottom(i,j, i + 1)
      right_trees = right(i, j, j + 1)
      left_trees = left(i, j, j - 1)
      r2.append(top_trees * bottom_trees * right_trees * left_trees)
      # if top_trees or bottom_trees or right_trees or left_trees:
      #   vis.append(grid_rows[i][j])


# print(len("".join(vis)))
r2.sort(reverse=True)
print(r2[0])