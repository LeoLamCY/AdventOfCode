import re


screen = [[0 for x in range(50)] for x in range(6)]


def rect(dimens):
    for column in range(int(dimens[0])):
        for row in range(int(dimens[1])):
            screen[row][column] = 1


def rotate_row(row, count):
    temp = [0 for x in range(50)]
    for i, v in enumerate(screen[row]):
        new_pos = i + count if i + count < 50 else i + count - 50
        temp[new_pos] = v
    screen[row] = temp


def rotate_col(col, count):
    temp = [0 for x in range(6)]
    for i in range(6):
        new_pos = i + count if i + count < 6 else i + count - 6
        temp[new_pos] = screen[i][col]
    for i in range(6):
        screen[i][col] = temp[i]

with open("day8_input.txt", "r") as input_file:
    dimens_rex = r'(\d+)x(\d+)'
    rotate_rex = r'=(\d+) by (\d+)'
    for line in input_file:
        if 'rect' in line:
            dimens = re.findall(dimens_rex, line)
            rect(dimens[0])
        elif 'row' in line:
            matches = re.findall(rotate_rex, line)
            rotate_row(int(matches[0][0]), int(matches[0][1]))
        elif 'column' in line:
            matches = re.findall(rotate_rex, line)
            rotate_col(int(matches[0][0]), int(matches[0][1]))

count = sum([x for row in screen for x in row])
print(screen)
print(count)
