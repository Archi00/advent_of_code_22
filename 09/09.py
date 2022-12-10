#!/usr/bin/python3

with open("example.txt") as f:
  raw_mvs = f.read().split("\n")

LENGTH = 35
PADDING = LENGTH // 2
grid = []
    
init_row = LENGTH - PADDING
init_column = LENGTH - LENGTH + PADDING -1 

knots = {
  "H" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "1" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "2" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "3" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "4" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "5" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "6" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "7" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "8" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1},
  "9" : {"x": LENGTH - PADDING, "y": LENGTH + PADDING -1}
}

# create grid
def create_grid():
  for i in range(LENGTH):
    grid.append([])
    for j in range(LENGTH):
      grid[i].append(".")

def print_grid():
  print_positions(1)
  grid[LENGTH-PADDING][LENGTH + PADDING - 1] = "S"
  print()
  for cell in grid:
    print(cell)
  print()

def check_first_knot(key):
  # check right
  if knots["H"]["y"] - knots["1"]["y"] > 1:
    knots["1"]["y"] = knots["H"]["y"] - 1
    knots["1"]["x"] = knots["H"]["x"]
  # check left
  if knots["1"]["y"] - knots["H"]["y"] > 1:
    knots["1"]["y"] = knots["H"]["y"] + 1
    knots["1"]["x"] = knots["H"]["x"]
  # check bottom
  if knots["H"]["x"] - knots["1"]["x"] > 1:
    knots["1"]["x"] = knots["H"]["x"] - 1
    knots["1"]["y"] = knots["H"]["y"]
  # check up
  if knots["1"]["x"] - knots["H"]["x"] > 1:
    knots["1"]["x"] = knots["H"]["x"] + 1
    knots["1"]["y"] = knots["H"]["y"]
  # print "1" to grid

def check_position(key):
  # check right
  if knots[str(int(key) - 1)]["y"] - knots[str(key)]["y"] > 1:
    knots[str(key)]["y"] = knots[str(int(key) - 1)]["y"] -1 
  # check left
  if knots[str(key)]["y"] - knots[str(int(key) - 1)]["y"]> 1:
    knots[str(key)]["y"] = knots[str(int(key) - 1)]["y"] + 1 
  # check up
  if knots[str(key)]["x"] - knots[str(int(key) - 1)]["x"] > 1:
    knots[str(key)]["x"] = knots[str(int(key) - 1)]["x"] + 1 
  # check down
  if knots[str(int(key) - 1)]["x"] - knots[str(key)]["x"] > 1:
    knots[str(key)]["x"] = knots[str(int(key) - 1)]["x"] - 1 
  
  if key == (len(knots) - 1):
    return
  return check_position(key + 1)

def print_positions(key):
  grid[knots["H"]["x"]][knots["H"]["y"]] = "H"
  grid[knots[str(int(key))]["x"]][knots[str(key)]["y"]] = str(key)
  if key == (len(knots) - 1):
    return
  return print_positions(key + 1)

def right(i, j, num_mvs):
  knots["H"]["y"] = j
  check_first_knot(1)
  check_position(2)
  if num_mvs == 0:
    knots["H"]["y"] = j
    return (i, j)
  return right(i, j + 1, num_mvs -1)

def left(i, j, num_mvs):
  knots["H"]["y"] = j
  check_first_knot(1)
  check_position(2)
  if num_mvs == 0:
    knots["H"]["y"] = j
    return (i, j)
  return left(i, j - 1, num_mvs -1)

def up(i, j, num_mvs):
  knots["H"]["x"] = i
  check_first_knot(1)
  check_position(2)
  if num_mvs == 0:
    knots["H"]["x"] = i
    return (i, j)
  return up(i - 1, j, num_mvs -1) 

def down(i, j, num_mvs):
  knots["H"]["x"] = i
  check_first_knot(1)
  check_position(2)
  if num_mvs == 0:
    knots["H"]["x"] = i
    return (i, j)
  return down(i + 1, j, num_mvs -1)

create_grid()
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

print_grid()
print(knots.items())