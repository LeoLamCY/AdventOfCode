from collections import defaultdict


freq = [defaultdict(lambda: 0) for k in range(8)]
min_freq = [0 for k in range(8)]
min_freq_char = [0 for k in range(8)]

with open("day6_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        for i, char in enumerate(line):
            freq[i][char] += 1
    result = ''
    for i in range(8):
        min_freq = 99
        for char, n in freq[i].items():
            if n < min_freq:
                min_char = char
                min_freq = n
        result += min_char
    print(result)
