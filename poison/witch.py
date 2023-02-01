#Given an array of 0's and 1's, return a boolean determining if the witch is able to cross the whole 'pool of poison'
#Example [0,1,0,0,1,0,0,0,0,1]. The witch would have to jump 2 spaces (feet) to get from her starting position to index 1,
#she'd have to jump 3 spaces (feet) to get from index 1 to index 4, and she'd have to jump 5 spaces to get from index 4 to
# index 9 

import sys

def poolHop(arr):
    count = 0
    for i in range(len(arr)):
        if count==3:
            return False
        if arr[i]==1:
            count=0
        else:
            count+=1
    if count==3:
        return False
    return True


testCases=[ ["0,1,0,0,1,0,0,0,1,0", "False"],["0,1,0,0,1,0,0,1,0,0", "True"],["0,1,0,0,1,0,0,1,0,0,0", "False"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = True if sys.argv[2]=="True" else False
    print(result)
    print(poolHop(input))
    print(poolHop(input)==result)