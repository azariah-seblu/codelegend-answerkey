import sys
#Roman numerals are usually written largest to smallest from left to right. 
#However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

#Write your solution below
def romanToInt(s):
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(map(lambda x: roman_to_integer[x], s))



if __name__ == "__main__":
    input = sys.argv[1]
    result = sys.argv[2]
    print(result)
    print(romanToInt(input))
    print(str(romanToInt(input))==result)

