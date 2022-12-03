#!/usr/bin/python3
# each rucksack has 2 compartments
# all items of given type meant to go into 1 of the 2 compartments
# 1 type per rucksack not organized properly

# input = all items in each rucksack
# 1st type identified by a
# 2nd type identified by A

# each rucksack same size for both compartments
# 1st half => 1st department
# 2nd half => 2nd department

# same letter in both departments, shared items
# priority a - z => 1 - 26
# priority A - > => 27 - 52
import math

abc = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w" ,"x", "y", "z"]
priority = {}
UPPER = 26

for i in range(1,27):
  priority[abc[i]] = i
print(priority)
print()
f = open("example")
file = f.read()
racks = []
racks_list = []
racks_in_threes_id = 0
racks_in_threes_list = []
racks_in_threes = []
rack_id = 0
total_sum_in_rack = 0
elf_groups = {}

for rack in file:
  tmp = 0
  if rack == "\n":
    shared = ""
    first_rack = racks_list[:math.floor(len(racks_list)/2)]
    second_rack = racks_list[math.floor(len(racks_list)/2):]
    [shared := element for element in second_rack if element in first_rack] 
    if (shared in priority):
      tmp = priority[shared]
    else:
      tmp = priority[shared.lower()] + UPPER
    racks.append({
      "rack": rack_id,
      "full_rack": racks_list,
      "shared": {
        "letter": shared,
        "value": tmp
        }
      })
    total_sum_in_rack += tmp
    rack_id += 1
    if rack_id % 3 == 0 and rack_id != 0:
      print(racks_in_threes_id)
      racks_in_threes.append({
        "id": racks_in_threes_id,
        "racks": racks_in_threes_list
      })
      racks_in_threes_id += 1
      racks_in_threes_list.clear()
    racks_list.clear()
  else:
    racks_list.append(rack)
    racks_in_threes_list.append(rack)
print(racks_in_threes)