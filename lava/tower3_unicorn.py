import sys
# Input: nums = [5,7,3,9,4,9,8,3,1] | Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
# Example 2: Input: nums = [9,9,8,8] | Output: -1
# Explanation: There is no number that occurs only once.


def largestUniqueNumber(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] +=1
        else:
            d[num] = 1
    maxi = [k for k,v in d.items() if v ==1]
    if maxi:
        return(max(maxi))
    else:
        return(-1)


if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = int(sys.argv[2])
    print(result)
    print(largestUniqueNumber(input))
    print(largestUniqueNumber(input)==result)

