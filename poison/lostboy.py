#Given an array of strings with incorrect names on them, return the array with correct names in it
import sys

def mapCorrect(arr):
    for i in range(len(arr)):
        arr[i]=arr[i][::-1]
    return arr


testCases=[ ["skroWkoorB,slliHwolloH","BrookWorks,HollowHills"],["sffucSsffurC","CruffsScuffs"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    result = sys.argv[2].split(',')
    print(result)
    print(mapCorrect(input[:]))
    print(mapCorrect(input[:])==result)