from math import inf
import os
from pprint import pprint
from typing import LiteralString
path = "/home/shpe/Downloads/zombies"
filename: str = "zom20b"
filepath = path + filename

irelevant_chars:list[LiteralString] = [" ", "\n", "\r", "   "]
relevant_bytes_zombie_A = """"""
relevant_bytes_zombie_B = """"""

for char in irelevant_chars:
    relevant_bytes_zombie_A: str = relevant_bytes_zombie_A.replace(char, "")
for char in irelevant_chars:
    relevant_bytes_zombie_B: str = relevant_bytes_zombie_B.replace(char, "")

totals: dict[str, int] = dict()
exit_status: int = os.system(f"ndisasm {filepath} | awk '{{print $2}}' > cache")
if exit_status != 0: "something went wrong"
print("exit status: " + str(exit_status))
with open("cache", "r") as file:
    content: str = file.read()

for char in irelevant_chars:
    content: str = content.replace(char, "")

for i in range(len(content) - 3):
    if i % 2 == 1: continue
    seq: str = content[i:i + 4]
    totals[seq] = totals[seq] + 1 if seq in totals else 1

totals_list: list[tuple[str, int]] = list(totals.items())
totals_list.sort(key=lambda x: x[1], reverse=True)
for seq, count in totals_list:
    # print(seq)
    if seq in relevant_bytes_zombie_B:
        print(f"({seq}, {count})")
# pprint(totals_list)