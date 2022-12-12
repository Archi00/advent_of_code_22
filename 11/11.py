#!/usr/bin/python3
import math

with open("input.txt") as f:
    lines = f.read().split("\n")

class Monkey:
    def __init__(self, num, starting_items, operation, test, passed, failed):
        self.num = num 
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.passed = passed
        self.failed = failed
        self.items = list(starting_items)
        self.items_inspected = 0
    
    # def __str__(self):
    #     return f"""Monkey {self.num} started with {self.starting_items}
    #         has items: {self.items} 
    #         performs the operation: {self.operation}
    #         his test is: {self.test} if this is true throws item to: {self.passed} 
    #         if this is false it throws item to: {self.failed}
            # """
    def get_test(self):
        return int(self.test)

    def has_items(self):
        print(f"Monkey {self.num} has {self.items}")
    
    def inspected(self):
        # print(f""" Monkey {self.num} has inspected: {self.items_inspected} items""")
        return self.items_inspected
    
    def worry_much(self, old):
        self.items_inspected += 1
        result = eval(self.operation)
        if result > 9699690:
            result = result % 9699690
        # return math.floor(result / 3)
        return result

    def yoink(self, item):
        self.items.append(item)
        # return print(f"Monkey {self.num} has received {item} now has: {self.items}")
    
    def yeet(self):
        while len(self.items) > 0:
            inspected_item = self.worry_much(int(self.items[0]))
            if inspected_item % int(self.test) == 0:
                # print(f"Monkey {self.num} has thrown {inspected_item} to {self.passed}")
                monkeys[self.passed].yoink(inspected_item)
            else:
                # print(f"Monkey {self.num} has thrown {inspected_item} to {self.failed}")
                monkeys[self.failed].yoink(inspected_item)
            self.items.remove(self.items[0])
        print()

monkeys = dict()
for line in lines:
    if "Monkey" in line:
        monkey_num = line.split(" ")[1][0].strip()
    if "items" in line:
        starting_items = line.split(":")[1].strip().split(",")
    if "Operation" in line:
        operation = line.split("=")[1].strip()
    if "Test" in line:
        test = line.split(" ")[-1].strip()
    if "true" in line:
        true_send_to = line.split(" ")[-1].strip()
    if "false" in line:
        false_send_to = line.split(" ")[-1].strip()
        monkey = Monkey(monkey_num, starting_items, operation, test, true_send_to, false_send_to)
        monkeys[monkey_num] = monkey

M = 1
for mo in monkeys:
    M *= monkeys[mo].get_test()

print(M)

for n in range(0, 10000):
    for m_num in monkeys:
        monkeys[m_num].yeet()
    print(f"Round {n} | Rounds to go: {10000 - n}")
    print("\r") 

ret_list = list()
for m_num in monkeys:
    ret_list.append(monkeys[m_num].inspected())

print(sorted(ret_list, reverse=True))
print(sorted(ret_list, reverse=True)[0] * sorted(ret_list, reverse=True)[1])