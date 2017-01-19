
with open("day9_input.txt", 'r') as input_file:
    code = input_file.read().strip()
    result = ''
    i = 0
    while i < len(code):
        if code[i] == ' ':
            i += 1
            continue
        if code[i] == '(':
            temp = ''
            i += 1
            while code[i] != ')':
                temp += code[i]
                i += 1
            i += 1
            num_chars, count = [int(a) for a in temp.split('x')]

            result += code[i:num_chars + i] * count
            i += num_chars
        else:
            result += code[i]
            i += 1
    print(result)
    print(len(result))
