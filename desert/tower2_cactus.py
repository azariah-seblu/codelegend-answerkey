import sys
#Given an integer array nums, move all 0's to the end of 
# it while maintaining the relative order of the non-zero elements.
# Example 1: Input: "5,0,9,0,3" Output: "5,9,3,0,0"
# Example 2: Input "0,1,0,1,0,1,0" Output: "1,1,1,0,0,0,0"

def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
        el = nums[i]
        if el != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums
    
if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = sys.argv[2].split(',')
    result = [int(x) for x in result]
    print(result)
    print(moveZeroes(input))
    print(moveZeroes(input)==result)

