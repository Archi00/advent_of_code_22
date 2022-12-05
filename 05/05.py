#!/usr/bin/python3

with open("input.txt") as f:
  lines = f.read().split("\n")

structure = True
lines_set = []
moves = []
for line in lines:
  if line == "":
    structure = False
  if structure == False and line != "":
    moves.append(line)
  if structure == True:
    lines_set.append(line)

null_ctr = 0
init_rows = []
line_ctr = 0
for line in lines_set[:-1]:
  strc = line.split(" ")
  tmp = []
  for s in strc:
    if s == "":
      null_ctr += 1
    if null_ctr == 4:
      tmp.append(0)
      null_ctr = 0
    if s != "":
      tmp.append(s)
  init_rows.append(tmp)
  line_ctr += 1

moves_ctr = 0
init_moves = []
for move in moves:
  tmp_line = move.split(" ")
  tmp = []
  for el in tmp_line:
    if el.isnumeric():
      tmp.append(int(el))
  init_moves.append(tmp)

num_colums = len(init_rows[0])
init_columns = []
for idx in range(num_colums):
  tmp = []
  for row in init_rows:
    if row[idx] != 0:
      row[idx] = row[idx][1]
    tmp.append(row[idx])
  init_columns.append(tmp)

for crate in init_columns:
  while crate[0] == 0:
    crate.pop(0)

for move in init_moves:
  ctr = 0
  num_crates_to_move = move[0] -1
  from_column = move[1] - 1
  to_column = move[2] - 1
  while ctr <= num_crates_to_move:
    init_columns[to_column].insert(0, init_columns[from_column].pop(0))
    ctr += 1

ret_crates = []
for column in init_columns:
  ret_crates.append(column[0])

ret = ""
for crate in ret_crates:
  ret += crate
print(ret)



