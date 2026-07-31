def encode_dict(obj):
    pos = 1
    arr = []
    dict = {}
    key = None

    if obj[0] != "d" or obj[-1] != "e":
        raise ValueError("Malformed input")

    while obj[pos] != "e":
        if obj[pos] == "i":
            end = obj.index("e", pos)
            num_str = obj[pos+1:end]

            neg = num_str.startswith("-")
            digits = num_str[1:] if neg else num_str

            if not digits.isdigit():
                raise ValueError("Malformed input")

            num = int(digits)
            val = -num if neg else num
            pos = end + 1

            dict[key] = val
            key = None

        elif obj[pos].isdigit():
            colon = obj.index(":", pos)
            str_size = obj[pos:colon]

            if not str_size.isdigit():
                raise ValueError("Malformed input")

            size = int(str_size)
            data_start = colon + 1
            data_end = data_start + size
            data = obj[data_start:data_end]

            if not len(data) == size:
                raise ValueError("Size mismatch")

            pos = data_end

            if key is None:
                key = data
            else:
                dict[key] = data
                key = None

        elif obj[pos] == "l":
            #skip '1'
            list_pos = pos +1

            while obj[list_pos] != "e":
                if obj[list_pos] == "i":
                    end = obj.index("e", list_pos)
                    num_str = obj[list_pos+1:end]

                    neg = num_str.startswith("-")
                    digits = num_str[1:] if neg else num_str

                    if not digits.isdigit():
                        raise ValueError("Malformed input")

                    num = int(digits)
                    arr.append(-num if neg else num)
                    list_pos = end + 1

                elif obj[list_pos].isdigit():
                    colon = obj.index(":", list_pos)
                    str_size = obj[list_pos:colon]

                    if not str_size.isdigit():
                        raise ValueError("Malformed input")

                    size = int(str_size)
                    data_start = colon + 1
                    data_end = data_start + size
                    data = obj[data_start:data_end]

                    if not len(data) == size:
                        raise ValueError("Size mismatch")

                    arr.append(data)
                    list_pos = data_end

                else:
                    raise ValueError("Malformed input")

            #skip closing 'e' of the list
            pos = list_pos + 1

            dict[key] = arr
            key = None

        else:
            raise ValueError("Malformed input")

    return dict

def decode_dict(obj):
    pos = 1

    if obj[0] != "{" or obj[-1] != "}":
        raise ValueError("Malformed input")

    end = len(obj)-1
    word_str = "d"

    while pos < end:
        if obj[pos] == ":" or obj[pos] == " " or obj[pos] == ",":
            pos +=1
            continue

        if obj[pos] == '"':
            end_quote = obj.index('"', pos+1)
            string_val = obj[pos+1:end_quote]

            word_str += f"{len(string_val)}:{string_val}"
            pos = end_quote + 1



        #incomplete
        elif obj[pos].isdigit() or obj[pos] == "-":
            pass



        elif obj[pos] == "[":
            word_str += "l"
            close_par = obj.index("]", pos+1)
            #move past "["
            pos +=1

            while pos < close_par:
                if obj[pos] == '"':
                    end_quote2 = obj.index('"', pos+1)
                    string_val2 = obj[pos+1:end_quote2]

                    word_str += f"{len(string_val2)}:{string_val2}"
                    pos = end_quote2 + 1


                #incomplete
                elif obj[pos].isdigit() or obj[pos] == "-":
                    pass



            word_str += "e"
            pos = close_par +1

    word_str += "e"
    return word_str