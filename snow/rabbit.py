#Given an array of diameters (numbers) return the same array back with its diameters adjusted accoding to the rabbit's needs

import sys

def rabbitHoles(arr):
    for i in range(len(arr)):
        if arr[i]>6:
            arr[i]=6
    return arr


testCases=[ ["4,5,6,7,8,9", "4,5,6,6,6,6"],["20,51,1,1,8,9", "6,6,1,1,6,6"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = sys.argv[2].split(',')
    result = [int(x) for x in result]
    print(result)
    print(rabbitHoles(input))
    print(rabbitHoles(input)==result)