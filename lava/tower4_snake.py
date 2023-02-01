import sys
#Example 1 Input: ransomNote = "a", magazine = "b" Output: False
#Example 2 Input: ransomNote = "aa", magazine = "aab" Output: True

def canConstruct(ransomNote, magazine):
    magazine = list(magazine)
    for i in ransomNote:
        if i in magazine:
            magazine.remove(i)
        else:
            return False
    return True


if __name__ == "__main__":
    input = sys.argv[1].split(',')
    result = sys.argv[2]
    print(result)
    print(canConstruct(input[0], input[1]))
    print(str(canConstruct(input[0], input[1]))==result)

