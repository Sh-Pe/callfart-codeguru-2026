from math import inf
import os
from pprint import pprint
from typing import LiteralString
path = "/home/shpe/Downloads/blackened/"

# our code
our_opcodes: set = set()
with open("/home/shpe/GSA2_dis", "r") as file:
    content: str = file.read()
for char in ["\n", "\r"]:
    content = content.replace(char, "")
for i in range(len(content) - 3):
    if i % 2 == 1: continue
    our_opcodes.add(content[i:i + 4])

size_threshold: int = 170
count = 0
opcodes_count: dict[str, list[int | bool]] = dict()
popularity_threshold: int = 12

for filename in os.listdir(path):
    filepath = path + filename
    exit_status: int = os.system(f"ndisasm {filepath} | awk '{{print $2}}' > cache")
    if exit_status != 0: "something went wrong"
    if os.path.getsize(filepath) <= size_threshold:
        continue
    count += 1

    with open("cache", "r") as file:
        content: str = file.read()

    for char in ["\n", "\r"]:
        content = content.replace(char, "")

    for i in range(len(content) - 3):
        if i % 2 == 1: continue
        seq: str = content[i:i + 4]
        if seq in opcodes_count:
            opcodes_count[seq][0] += 1
        else:
            opcodes_count[seq] = [1]
        if seq in our_opcodes:
            opcodes_count[seq].append(True)
        else:
            opcodes_count[seq].append(False)

totals_list: list[tuple[str, list[int | bool]]] = list(opcodes_count.items())
totals_list.sort(key=lambda x: x[1], reverse=False)
totals_list.pop()
totals_list.pop()
# pprint(totals_list)
for opcode, popularity in totals_list:
    if popularity[0] >= popularity_threshold:
        if popularity[1] == True:
            print("shown in our code:")
        print(f"db 0x{opcode[:2]}\ndb 0x{opcode[2:]}")

print(count)