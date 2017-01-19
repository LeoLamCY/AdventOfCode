import re


def parse_brackets(code):
    regex_numbers = r'\((\d+)x(\d+)\)'
    m = re.search(regex_numbers, code)
    len1, num_chars = len(m.group(1)), int(m.group(1))
    len2, count = len(m.group(2)), int(m.group(2))
    block_length = len1 + len2 + 3
    return (num_chars, count, block_length)


def cal_length(code):
    length = 0
    i = 0
    while i < len(code):
        if code[i] == '(':
            num_chars, count, block_length = parse_brackets(code[i:])
            length += cal_length(code[i +
                                      block_length:i + num_chars + block_length]) * count
            i += block_length + num_chars
        else:
            length += 1
            i += 1
    return length

with open("day9_input.txt", 'r') as input_file:
    code = input_file.read().strip()
    final_length = cal_length(code)
print(final_length)
