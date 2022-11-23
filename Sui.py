import string as sg


def check_i(x):
    return x.count("i")


def count_l(x, letter):
    return x.count(letter)


def create_file(content):
    with open("test.sui", "w") as f:
        f.write(content)


def get_file():
    with open("test.sui", "r") as f:
        return f.read().splitlines()


def addition(content):
    num = 0
    cont = content.split("+")
    for x in cont:
        if x not in "     ":
            num += check_i(x)
    return num


def subtract(content):
    num = 1
    cont = content.split("-")
    for nu, x in enumerate(cont):
        if x not in "     ":
            if nu == 0:
                num = check_i(x)
            else:
                num -= check_i(x)
    return num


def multiply(content):
    num = 1
    cont = content.split("*")
    for x in cont:
        if x not in "     ":
            num *= check_i(x)
    return num


def divide(content):
    num = 1
    cont = content.split("÷")
    for nu, x in enumerate(cont):
        if x not in "      ":
            if nu == 0:
                num = check_i(x)
            else:
                num /= check_i(x)
    return num


def string(content):
    sent = ""
    letters = {}
    u = 0
    i = 0
    for letter in sg.ascii_lowercase:
        i += 1
        u += 2
        letters[letter] = {"u": u, "i": i}
    cont = [x for x in content.split() if x != "[" and x != "]"]
    for num, x in enumerate(cont):
        if num == 0:
            for k, z in letters.items():
                if x.count("u") == z["u"] and x.count("i") == z["i"]:
                    sent += k
                else:
                    continue
        else:
            if x == "+":
                for k, z in letters.items():
                    if cont[num + 1].count("u") == z["u"] and cont[num + 1].count("i") == z["i"]:
                        sent += k
                    else:
                        continue
            if x == "_":
                for k, z in letters.items():
                    if cont[num + 1].count("u") == z["u"] and cont[num + 1].count("i") == z["i"]:
                        sent += " " + k
                    else:
                        continue
    return sent


h = f"""
suii + suiii
suiii - suii
suiii ÷ suiii
[s{'u' * 38}{'i' * 19} + s{'u' * 16}{'i' * 8} + s{'u' * 42}{'i' * 21} + s{'u' * 40}{'i' * 20} _ s{'u' * 42}{'i' * 21} + s{'u' * 32}{'i' * 16}] 
"""
# {'a': {'u': 2, 'i': 1}, 'b': {'u': 4, 'i': 2}, 'c': {'u': 6, 'i': 3}, 'd': {'u': 8, 'i': 4}, 'e': {'u': 10, 'i': 5}, 'f': {'u': 12, 'i': 6}, 'g': {'u': 14, 'i': 7}, 'h': {'u': 16, 'i': 8}, 'i': {'u': 18, 'i': 9}, 'j': {'u': 20, 'i': 10}, 'k': {'u': 22, 'i': 11}, 'l': {'u': 24, 'i': 12}, 'm': {'u': 26, 'i': 13}, 'n': {'u': 28, 'i': 14}, 'o': {'u': 30, 'i': 15}, 'p': {'u': 32, 'i': 16}, 'q': {'u': 34, 'i': 17}, 'r': {'u': 36, 'i': 18}, 's': {'u': 38, 'i': 19}, 't': {'u': 40, 'i': 20}, 'u': {'u': 42, 'i': 21}, 'v': {'u': 44, 'i': 22}, 'w': {'u': 46, 'i': 23}, 'x': {'u': 48, 'i': 24}, 'y': {'u': 50, 'i': 25}, 'z': {'u': 52, 'i': 26}}
if __name__ == "__main__":
    lines = get_file()
    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            print(string(line))
        if "+" in line and "[" not in line:
            print(addition(line))
        if "-" in line:
            print(subtract(line))
        if "÷" in line:
            print(divide(line))
        if "*" in line:
            print(multiply(line))
