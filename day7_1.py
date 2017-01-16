import re


def findABBA(line):
    for i in range(0, len(line) - 3):
        if line[i] != line[i + 1]:
            if line[i:i + 2] == line[i + 3] + line[i + 2]:
                return True
    return False

regex = r'(\w+|\[\w+\])'
with open("day7_input.txt", "r") as input_file:
    count = 0
    for line in input_file:
        tls = False
        for part in re.findall(regex, line.strip()):
            if part[0] == '[':
                if findABBA(part[1:-1]):
                    tls = False
                    break
            elif not tls:
                tls = findABBA(part)

        if tls:
            count += 1

print(count)
