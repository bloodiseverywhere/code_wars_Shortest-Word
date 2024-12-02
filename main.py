def find_short(s):
    s = s.split()
    s_len = min(s, key=len)
    return len(s_len)
