#Given an array of poison amounts of different cheeses, return an array of the indices of cheese the rat should 
# steal to achieve his poison quota
#Example [10,10,30,40,10]. If the rat took cheese 0, 1, and 2, he would end up with 50 grams of poison

import sys 

def cheesePoison(arr):
    return


testCases=[ ["10,10,30,40,10","0,1,4"],["10,20,30,40,5,5","1,1,4"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    input = [int(x) for x in input]
    result = sys.argv[2].split(',')
    result = [int(x) for x in result]
    print(result)
    print(cheesePoison(input))
    print(cheesePoison(input)==result)