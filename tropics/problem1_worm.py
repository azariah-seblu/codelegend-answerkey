import sys
#Example 1:Input: x = 121, Output: True
# Explanation: 121 reads as 121 from left to right and from right to left.
#Example 2: Input: x = 10, Output: False
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

#Write your solution here
def isPalindrome(x):
	return False if x < 0 else x == int(str(x)[::-1])



if __name__ == "__main__":
    input = int(sys.argv[1])
    result = sys.argv[2]
    print(result)
    print(isPalindrome(input))
    print(str(isPalindrome(input))==result)


 