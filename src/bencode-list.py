
def encode_list(obj):
    pos = 1
    num = 0
    neg = False
    arr = []
    arr2 = []

    if obj[0] != "l" or obj[-1] != "e":
        raise ValueError("Malformed input")
    else:
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

value = input()
print(encode_list(value))