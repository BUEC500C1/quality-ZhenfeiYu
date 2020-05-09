def quality(num):
    if not isinstance(num,int):
        return "Invalid Input"
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    i = 0
    if num > 0 and num < 5000:
        while num > 0:
            for each in range(num//values[i]):
                res += numerals[i]
                num -= values[i]
            i += 1
    else:
        return "number should between 0 and 5000"
    return res
