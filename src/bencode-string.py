
def encode_string(obj):
    word = ""

    seperator = obj.split(":", 1)
    size = seperator[0]
    data = seperator[1]

    if not size.isdigit():
        raise ValueError("Malformed input")
    elif not int(size) == len(data):
        raise ValueError("Size mismatch")

    word = data

    return word

def decode_string(obj):
    pos = 0
    new_string = ""

    if obj[pos].isalpha():
        new_string += str(len(obj))
        new_string += ":"
        new_string += obj

    return new_string
