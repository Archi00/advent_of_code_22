#!/usr/bin/python3
# 5 elves 
# we want the "Calories" of each elf
# we have list (inventory) each individual inv is separated by a blank line
f = open("input", "r")
test_string = f.read()

test = test_string.split("\n")
test.pop()
test.pop(0)
tmp = []
count_total = 0
count = 0
top_count = 0
for i in test:
    if len(i) > 0: 
        count_total += int(i)
    else:
        tmp.append({"id": count, "calories": count_total})
        if count_total > top_count:
            top_count = count_total
        count += 1
        count_total = 0

print(top_count)