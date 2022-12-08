#!/usr/bin/python3 
import pprint

with open("input.txt") as f:
  raw_coms = f.read().split("\n")

path = "/"
size = {}

for com in raw_coms:
  if "$ cd" in com:
    if com.split(" ")[-1] != ".." and com.split(" ")[-1] != "/":
      path += com.split(" ")[-1] + "/"
    if com.split(" ")[-1] == "..":
      tmp = "/".join(path.split("/")[:-2]) + "/"
      path = tmp
    if path not in size.keys():
      size[path] = 0
  elif "$ ls" not in com:
    if com.split(" ")[0].isnumeric():
      size[path] += int(com.split(" ")[0])     

ret = {}
def crawl(k, v):
  if k not in ret.keys():
    ret[k] = v
  else:
    ret[k] += v
  if k == "/":
    return
  nxt = "/".join(k.split("/")[:-2]) + "/"
  return crawl(nxt, v)

for k, v in size.items():
  crawl(k, v)
  
r = 0 
total_space = 70000000
space_need = 30000000
space_used = ret["/"]
space_unused = total_space - ret["/"]
space = space_need - space_unused 

r2 = []
for k, v in ret.items():
  if v < 100000:
    r += v
  if v > space:
    r2.append(v)
r2.sort()
print(r2[0])

# pprint.pprint(ret)
# print(r)