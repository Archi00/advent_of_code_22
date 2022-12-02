#!/usr/bin/python3
# encrypted strategy guide
# 1st column opponents play
# 2nd column ?
# what you should play in response 

# total score = sum of scores (per round)
# round score = shape ((1 = Rock, 2 = Paper, 3 = Scissors) + outcome (0 = lost, 3 = draw, 6 = win))

f = open("input", "r")
file = f.read()
file = file.split("\n")
status = {"lost": 0, "draw": 3, "win": 6}
my_value = {"X": "A", "Y": "B", "Z": "C"}
decript = {"X": "lost", "Y": "draw", "Z": "win"}
op = {
  "A": {
    "value": 1,
    "Y": "win",
    "Z": "lost",
    "X": "draw",
  },
  "B": {
    "value": 2,
    "Y": "draw",
    "Z": "win",
    "X": "lost",
  },
  "C": {
    "value": 3,
    "Y": "lost",
    "Z": "draw",
    "X": "win",
  }
}

matching_throws = []
n_match = 0
my_total_score = 0
elf_total_score = 0
for l in file:
  play_result = status[op[l[0]][l[2]]]
  my_way_play = op[my_value[l[2]]]["value"]
  my_final_game = play_result + my_way_play

  final_round = status[decript[l[2]]]
  key = [k for k, v in op[l[0]].items() if v == decript[l[2]]]
  my_play = op[my_value[key[0]]]["value"]
  match_result = final_round + my_play

  matching_throws.append({
    "id": n_match, 
    "my_value": my_final_game,
    "elf_value": match_result,
  })

  my_total_score += matching_throws[n_match]["my_value"]
  elf_total_score += matching_throws[n_match]["elf_value"]
  n_match += 1

print(f"final list of games: {matching_throws}")
print(f"Score of my game: {my_total_score}")
print(f"Score with elf's way: {elf_total_score}")