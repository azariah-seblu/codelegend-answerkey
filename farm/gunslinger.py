# You are given an array of strings that either say 
# “clean” or “dirty.”
# Return an array of the indices of only his clean guns

def gun_clean(arr):
    final = []
    for i in range(len(arr)):
      if arr[i]=="clean":
        final.append(i)
    return final