

def diffDates(tup1, tup2):
    output = ''
    yy1, mm1, dd1 = tup1
    yy2, mm2, dd2 = tup2

    diff_yr = yy2 - yy1
    diff_mm = mm2 - mm1
    diff_dd = dd2 - dd1

    if diff_dd < 0 or diff_yr < 0 or diff_mm < 0:
        raise ValueError(
            f'Check to see if the values in {tup1} are smaller than the values in {tup2}')

    if diff_yr > 0:
        output += f'{diff_yr} year(s)'
    if diff_mm > 0:
        output += f' {diff_mm} month(s)'
    if diff_dd > 0:
        output += f' {diff_dd} day(s)'

    print(output)


diffDates((2014, 7, 2), (2014, 7, 11))
