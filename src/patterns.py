smily = [
    "        ",
    "        ",
    "  1  1  ",
    "  1  1  ",
    "        ",
    " 1    1 ",
    "  1111  ",
    "        ",
]

not_smily = [
    "        ",
    "        ",
    "  1  1  ",
    "  1  1  ",
    "        ",
    "  1111  ",
    " 1    1 ",
    "        ",
]

akiba = [
    "                                      ",
    "   11    11  11  1111  11111     11   ",
    "  1111   11 11    11   11  11   1111  ",
    " 11  11  1111     11   111111  11  11 ",
    " 111111  1111     11   11  11  111111 ",
    " 11  11  11 11    11   11  11  11  11 ",
    " 11  11  11  11  1111  111111  11  11 ",
    "                                      ",
]

def get_eight_col(pattern, start, end):
    retval = []
    for row in pattern:
        retval.append(row[start:end])
    return retval
