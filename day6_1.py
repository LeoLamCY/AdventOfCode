from collections import defaultdict


freq = [defaultdict(lambda: 0) for k in range(8)]
max_freq = [0 for k in range(8)]
max_freq_char = [0 for k in range(8)]

with open("day6_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        for i, char in enumerate(line):
            freq[i][char] += 1
            if freq[i][char] > max_freq[i]:
                max_freq[i] = freq[i][char]
                max_freq_char[i] = char

    print("".join([max_freq_char[i] for i in range(8)]))
