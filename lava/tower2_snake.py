import sys
#Given an array of strings strs, group the anagrams together. 
#You can return the answer in any order.
#Example 1: Input: strs = ["eat","tea","tan","ate","nat","bat"] 
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Example 2: Input: strs = ["a"]
#Output: Output: [["a"]]

def groupAnagrams(s):
    d={}
    for words in s:
        key=tuple(sorted(words))
        d[key]=d.get(key,[])+[words]
    return d.values()



if __name__ == "__main__":
    input = sys.argv[1].split(",")
    # this_does_nothing = sys.argv[2]
    d= defaultdict(list)
    for w in input:
        d[''.join(sorted(w))].append(w)
    result = d.values()

    print(list(result))
    print(list(groupAnagrams(input)))
    print(list(groupAnagrams(input))==list(result))

