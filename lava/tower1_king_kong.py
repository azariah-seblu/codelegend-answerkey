import sys
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.
# Example 1: Input: s = "()" | Output: True
# Example 1: Input: s = "(]" | Output: False

#Write your solution below
def isValid(s):
    h = {'(':')', '[':']', '{':'}'}
    stack =[]
    for char in s:
        if char in h.keys():
            stack.append(char)

        elif char in h.values():
            if not stack:
                return False

            if char == h[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack)==0

if __name__ == "__main__":
    input = sys.argv[1]
    result = sys.argv[2]
    print(result)
    print(isValid(input))
    print(str(isValid(input))==result)

