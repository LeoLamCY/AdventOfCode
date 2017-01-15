from collections import Counter
import re


regex = r'([a-z-]+)(\d+)\[(\w+)\]'
with open("day4_input.txt", "r") as input_file:
    total = 0
    for line in input_file:
        code, cur_id, checksum = re.findall(regex, line)[0]
        code = code.replace('-', '')
        top5 = sorted([(-n, c) for c, n in Counter(code).most_common()])[0:5]
        calculated_checksum = "".join([c[1] for c in top5])
        if calculated_checksum == checksum:
            total += int(cur_id)

print(total)
