import sys
#Given a string s consisting of lowercase English letters, return the letter to appear twice.
#Example: Input: s = "abcdd" | Output: "d"


def repeatedCharacter(s):
    s1 = {}
    for i in s:
        if i in s1:
            return i
        else:
            s1[i] = 1


    
if __name__ == "__main__":
    input = sys.argv[1]
    result = sys.argv[2]
    print(result)
    print(repeatedCharacter(input))
    print(repeatedCharacter(input)==result)

