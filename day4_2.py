from collections import Counter
import re


regex = r'([a-z-]+)(\d+)\[(\w+)\]'


def decrypt_name(name, _id):
    result = ''
    shifts = _id % 26
    for char in name:
        if char == '-':
            result += ' '
        else:
            ascii_after_shifts = ord(char) + shifts
            ascii_after_shifts -= 26 if ascii_after_shifts > 122 else 0
            result += chr(ascii_after_shifts)
    return result

with open("day4_input.txt", "r") as input_file:
    total = 0
    for line in input_file:
        code, cur_id, checksum = re.findall(regex, line)[0]
        original = code
        code = code.replace('-', '')
        top5 = sorted([(-n, c) for c, n in Counter(code).most_common()])[0:5]
        calculated_checksum = "".join([c[1] for c in top5])
        if calculated_checksum == checksum:
            decrypted_name = decrypt_name(original, int(cur_id))
            if "north" in decrypted_name:
                print(cur_id)
