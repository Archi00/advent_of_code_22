#!/usr/bin/python3
# every section have a unique ID number
# many of the assigns overlap
# big list of the section assignments for each pair

with open("input.txt") as ids:
  groups = ids.read().split("\n")

indx = 0
yep = 0
for sec in groups:
  elves = sec.split(",")
  elf01 = elves[0].split("-")
  elf02 = elves[1].split("-")
  elf01_first_sec = int(elf01[0])
  elf01_second_sec = int(elf01[1])
  elf02_first_sec = int(elf02[0])
  elf02_second_sec = int(elf02[1])
  contained = False
  overlap = False

  if len(elf01) < 2 and (elf01_first_sec <= elf02_second_sec or elf01_first_sec >= elf02_second_sec):
    contained = True
    overlap = True
  if elf01_first_sec <= elf02_first_sec and elf01_second_sec >= elf02_second_sec:
    contained = True
  if len(elf02) < 2 and (elf02_first_sec <= elf01_second_sec or elf02_first_sec >= elf01_second_sec):
    contained = True
    overlap = True
  if elf02_first_sec <= elf01_first_sec and elf02_second_sec >= elf01_second_sec:
    contained = True
  
  if contained:
    indx += 1
    
  if elf01_first_sec <= elf02_first_sec and elf01_second_sec >= elf02_first_sec:
    overlap = True
  if elf02_first_sec <= elf01_first_sec and elf02_second_sec >= elf01_first_sec:
    overlap = True

  if contained or overlap:
    yep += 1 
  
print(yep)