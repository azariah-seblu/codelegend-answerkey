#Given an array of wood weights, return an array sorted the way the old man wants it.

import sys

def wood(arr):
    return sorted(arr)[::-1]


testCases=[ ["1,2,3,4,5", "5,4,3,2,1"], ["1","1"], ["5,4,1,5,6,3", "6,5,5,4,3,1"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = sys.argv[2].split(',')
    result = [int(x) for x in result]
    print(result)
    print(wood(input))
    print(wood(input)==result)