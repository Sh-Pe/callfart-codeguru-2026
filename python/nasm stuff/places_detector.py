from math import inf
import os
from pprint import pprint
from typing import LiteralString
path = "/home/shpe/Downloads/online/"
irelevant_chars:list[LiteralString] = [" ", "\n", "\r", "   "]
totals: dict[str, int] = dict()
size_threshold: int = 250
count = 0
opcode_to_reg: dict[str, str] = {
    # "A3" : "ax",
    "891E" : "bx",
    "890E" : "cx",
    "8916" : "dx",
    "8936" : "si",
    "893E" : "di",
    "892E" : "bp",
}
charcount = 4

reg_to_total_freq: dict[str, dict[str, int]] = {reg : dict() for reg in opcode_to_reg.values()}
for filename in os.listdir(path):
    filepath = path + filename
    exit_status: int = os.system(f"ndisasm {filepath} | awk '{{print $2}}' > cache")
    if exit_status != 0: "something went wrong"
    if os.path.getsize(filepath) <= size_threshold:
        continue
    count += 1

    with open("cache", "r") as file:
        content: str = file.read()

    for char in irelevant_chars:
        content = content.replace(char, "")

    for i in range(len(content) -charcount - 3):
        if i % 2 == 1: continue
        seq: str = content[i:i + charcount + 4]
        reg = seq[:charcount]
        if reg in opcode_to_reg:
            if seq[charcount:] in reg_to_total_freq[opcode_to_reg[reg]]:
                reg_to_total_freq[opcode_to_reg[reg]][seq[charcount:]] += 1
            else:
                reg_to_total_freq[opcode_to_reg[reg]][seq[charcount:]] = 1

totals_list: dict[str, list[tuple[str, int]]] = {k: list(v.items()) for k, v in reg_to_total_freq.items()}
for k, v in totals_list.items(): v.sort(key=lambda x: x[1], reverse=False)
pprint(totals_list)
for lst in totals_list.values():
    for adrs in lst:
        if adrs[1] > 1:
            print(f"mov byte[0x{adrs[0][2:] + adrs[0][:2]}], 0xCC")
