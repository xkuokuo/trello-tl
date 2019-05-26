def isPositiveInt(s):
    try:
        return int(s) >= 0
    except ValueError:
        return False

def align_str_len(s, max_print_length):
    # well of course this is very hard coded for Chinese language...
    original_print_length = get_print_length(s)
    s = s.ljust(max_print_length)
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
        # a chinese char...
        byte_length = byte_length - 3
        return s.encode("utf-8")[:byte_length].decode('utf-8', 'ignore') + "…"

    aligned_str = s.encode("utf-8")[:byte_length].decode('utf-8', 'ignore')
    if original_print_length > max_print_length:
        if is_chinese_char(aligned_str[-1]):
            aligned_str = aligned_str[:-1] + " …"
        else:
            aligned_str = aligned_str[:-1] + "…"
    return aligned_str

def get_print_length(s):
    print_length = 0
    for c in s:
        if is_chinese_char(c):
            print_length += 2
        else:
            print_length += 1
    return print_length

def is_chinese_char(c):
    return  (u'\u4e00' <= c <= u'\u9fff') or (u'\uff01' <= c <= u'\uff5e') or (u'\u3000' <= c <= u'\u303F')
