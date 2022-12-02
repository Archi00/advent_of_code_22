#!/usr/bin/python3
# 5 elves 
# we want the "Calories" of each elf
# we have list (inventory) each individual inv is separated by a blank line
f = open("input", "r")
test_string = f.read()

test = test_string.split("\n")
test.pop()
test.pop(0)

elves = []
count_total = 0
count = 0
top_count = 0
for i in test:
    if len(i) > 0: 
        count_total += int(i)
    else:
        elves.append({"id": count, "calories": count_total})
        if count_total > top_count:
            top_count = count_total
        count += 1
        count_total = 0

top3 = sorted(elves, key=lambda d: d['calories'], reverse=True)[:3] 
total_amount = 0
for elf in top3:
    total_amount += elf["calories"]
print(top3)
print(total_amount)