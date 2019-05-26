def isPositiveInt(s):
    try:
        return int(s) >= 0
    except ValueError:
        return False

def align_str_len(s, max_print_length):
    # well of course this is very hard coded for Chinese language...
    print_length = 0
    byte_length = 0
    i = 0
    while i < len(s) and print_length < max_print_length:
        if is_chinese_char(s[i]):
            #print("yes" + s[i])
            print_length += 2
            byte_length += 3
        else:
            #print("No" + s[i])
            print_length += 1
            byte_length += 1
        i += 1

    if print_length > max_print_length:
        #print("Print_length is " + str(print_length))
        # a chinese char...
        byte_length = byte_length - 3
        return s.encode("utf-8")[:byte_length].decode('utf-8', 'ignore') + " "

    # print("2 Print_length is " + str(print_length))
    #print("2 byte_length is " + str(byte_length))
    #print(s.encode("utf-8")[:byte_length])
    return s.encode("utf-8")[:byte_length].decode('utf-8', 'ignore')

def is_chinese_char(c):
    return  (u'\u4e00' <= c <= u'\u9fff') or (u'\uff01' <= c <= u'\uff5e') or (u'\u3000' <= c <= u'\u303F')
