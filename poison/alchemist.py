#Given a monomial as a string, depicted as (coefficient)(x)(^)(exponent), for instance 3x^2, return the
#coefficient of derivative as a number. Assume all numbers are whole
#Example Input: "3x^2", Output: "6"

import sys
def alchemy(expression):
    me = expression.split('^')
    me[0]=me[0][:-1]
    return str(int(me[0])*int(me[1]))


testCases=[ ["3x^2", "6"], ["25x^3","75"], ["9x^3", "27"]]

if __name__ == "__main__":
    input = sys.argv[1]
    result = sys.argv[2]
    print(result)
    print(alchemy(input))
    print(str(alchemy(input))==result)
