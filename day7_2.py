import re


def findABA(line, ABAs):
    for i in range(len(line) - 2):
        if line[i] != line[i + 1] and line[i] == line[i + 2]:
            ABAs.append(line[i + 1] + line[i] + line[i + 1])
    return ABAs


def findBAB(hypernet, ABAs):
    for ABA in ABAs:
        if re.findall(ABA, hypernet, 1):
            return True
    return False

regex = r'(\w+|\[\w+\])'
with open("day7_input.txt", "r") as input_file:
    count = 0
    for line in input_file:
        hypernets = []
        ABAs = []
        for part in re.findall(regex, line.strip()):
            if part[0] == '[':
                hypernets.append(part)
            else:
                findABA(part, ABAs)

        if ABAs:
            for hypernet in hypernets:
                if findBAB(hypernet, ABAs):
                    count += 1
                    break

print(count)
