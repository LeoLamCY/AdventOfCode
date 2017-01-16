import hashlib

puzzle_input = "reyedfim"
i = 0
password = ""

while(True):
    digest = hashlib.md5((puzzle_input + str(i)).encode("UTF-8")).hexdigest()
    if digest[:5] == '00000':
        password += digest[5]
        if len(password) == 8 or i > 1000000000:
            break
    i += 1

print(password)
