import hashlib
from collections import defaultdict

puzzle_input = "reyedfim"
i = 0
password = [-1 for k in range(8)]

while(True):
    digest = hashlib.md5((puzzle_input + str(i)).encode("UTF-8")).hexdigest()
    if digest[:5] == '00000':
        pos = digest[5]
        if pos.isdigit() and int(pos) < 8 and password[int(pos)] == -1:
            password[int(pos)] = digest[6]
        if -1 not in password or i > 1000000000:
            break
    i += 1

print("".join(password))
