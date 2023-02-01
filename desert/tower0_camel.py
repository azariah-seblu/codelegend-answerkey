import sys
# Python program to convert given sentence to camel case
#Example: Input: Hi Josh it is your cousin Drake from Sahara 
# Output: HiJoshItIsYourCousinDrakeFromSahara

#Write your solution here
def convertToCamel(s):
    if(len(s) == 0):
        return
    s1 = ''
    s1 += s[0].upper()
    for i in range(1, len(s)):
        if (s[i] == ' '):
            s1 += s[i + 1].upper()
            i += 1
        elif(s[i - 1] != ' '):
            s1 += s[i]
    return(s1)    



if __name__ == "__main__":
    input = sys.argv[1]
    result = sys.argv[2]
    print(result)
    print(convertToCamel(input))
    print(str(convertToCamel(input))==result)


