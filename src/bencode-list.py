
def encode_list(obj):
    pos = 1
    num = 0
    neg = False
    arr = []
    arr2 = []

    if obj[0] != "l" or obj[-1] != "e":
        raise ValueError("Malformed input")

    while obj[pos] != "e":
        if obj[pos] == "i":
            end = obj.index("e")
            num_str = obj[pos +1:end]

            neg = num_str.startswith("-")
            digits = num_str[1:] if neg else num_str

            if not digits.isdigit():
                raise ValueError("Malformed input")

            num = int(digits)
            arr.append(-num if neg else num)
            pos = end + 1

        elif obj[pos].isdigit():
            colon = obj.index(":", pos)
            size_str = obj[pos:colon]

            size = int(size_str)
            data_start = colon + 1
            data_end = data_start + size
            data = obj[data_start:data_end]

            if not len(data) == size:
                raise ValueError("Size mismatch")

            arr.append(data)
            pos = data_end

        else:
            raise ValueError("Malformed input")
    return arr

def decode_list(obj):
    pos = 1

    if obj[0] != "[" or obj[-1] != "]":
        raise ValueError("Malformed input")

    new_word = "l"
    end = len(obj) - 1

    while pos < end:
        if obj[pos] == " " or obj[pos] == ",":
            pos += 1
            continue

        #checks for open quote
        if obj[pos] == '"':
            close_quote = obj.index('"', pos + 1)
            string_val = obj[pos + 1:close_quote]
            new_word += f"{len(string_val)}:{string_val}"
            pos = close_quote + 1

        elif obj[pos].isdigit() or obj[pos] == "-":
            num_start = pos
            pos += 1
            while pos < end and obj[pos].isdigit():
                pos += 1
            num_str = obj[num_start:pos]
            new_word += f"i{num_str}e"

    new_word += "e"
    return new_word