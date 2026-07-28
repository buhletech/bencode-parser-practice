
def encode(obj):
    count = 1
    num = 0
    neg = False

    if obj[0] != "i" or obj[-1] != "e":
        raise ValueError("Malformed input")

    while count <= len(obj):
        if obj[count].isdigit():
            num = num*10 + int(obj[count])
            count+=1
        elif obj[count] == "-":
            neg = True
            count+=1

        if obj[count] == "e":
            break
    return -num if neg else num

def decode(obj):
    pos = 0
    num = 0
    num_str = ""

    while pos <= len(obj):
        if obj[pos].isdigit():
            if not num_str.startswith("i"):
                num_str += "i"

                num_str += str(obj[pos])
                pos+=1
            else:
                num_str += str(obj[pos])
                pos+=1
        if pos == len(obj):
            num_str += "e"
            break

    return num_str


