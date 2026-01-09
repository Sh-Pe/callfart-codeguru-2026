from math import inf
import os
from pprint import pprint
from typing import LiteralString
path = "../../assembly/final_code"
irelevant_chars:list[LiteralString] = [" ", "\n", "\r", "   "]

totals_our_code: dict[str, int] = dict()
filepath_old = path
exit_status: int = os.system(f"ndisasm \"{filepath_old}\" | awk '{{print $2}}' > cache")
with open("cache", "r") as file:
    content: str = file.read()

for char in irelevant_chars:
    content = content.replace(char, "")
content = content[10:]

for i in range(len(content) - 7):
    if i % 2 == 1: continue
    seq: str = content[i:i + 8]
    totals_our_code[seq] = totals_our_code[seq] + 1 if seq in totals_our_code else 1

totals_new_code: dict[str, int] = dict()
filepath_new = "/home/shpe/Downloads/nasm.out"

exit_status: int = os.system(f"ndisasm \"{filepath_new}\" | awk '{{print $2}}' > cache")
with open("cache", "r") as file:
    content: str = file.read()

for char in irelevant_chars:
    content = content.replace(char, "")
content = content[10:]

for i in range(len(content) - 7):
    if i % 2 == 1: continue
    seq: str = content[i:i + 8]
    totals_new_code[seq] = totals_new_code[seq] + 1 if seq in totals_new_code else 1


totals_list_old: list[tuple[str, int]] = list(totals_our_code.items())
list_old: list[str] = [k for k, v in totals_list_old]
totals_list_new: list[tuple[str, int]] = list(totals_new_code.items())
# totals_list.sort(key=lambda x: x[1], reverse=True)
for adrs, count in totals_list_new:
    # print(seq)
    if adrs in list_old:
        print(adrs)
    # if count == 1:
    #     print(f"mov [0x{adrs[0][2:] + adrs[0][:2]}], CC")
# pprint(totals_list)