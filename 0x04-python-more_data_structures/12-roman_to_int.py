#!/usr/bin/python3


def convert_roman(ch):
    ret = -1
    if ch == 'I':
        ret = 1
    elif ch == 'V':
        ret = 5
    elif ch == 'X':
        ret = 10
    elif ch == 'L':
        ret = 50
    elif ch == 'C':
        ret = 100
    elif ch == 'D':
        ret = 500
    elif ch == 'M':
        ret = 1000
    return ret


def roman_to_int(roman_string):
    cur_max = -1
    cur = conv = 0
    holder = []

    if roman_string is None or type(roman_string) is not str:
        return 0
    for c in roman_string:
        cur = convert_roman(c)
        if cur == -1:
            return 0
        if len(holder) == 0:
            if cur == cur_max or cur_max == -1:
                cur_max = cur
                conv += cur
            elif cur < cur_max:
                holder.append(cur)
            elif cur > cur_max:  
                cur_max = cur
                cur -= conv
                conv = cur
        else:
            if cur > holder[-1]:
                cur_max = cur
                cur -= sum(holder)
                conv += cur
                holder.clear()
            else:
                holder.append(cur)

    if len(holder) != 0:
        conv += sum(holder)
    return conv
