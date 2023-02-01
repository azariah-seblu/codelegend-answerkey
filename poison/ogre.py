# Given a dictionary mapping food names to the number of calories they contain, return the name of the food that will
# help the ogre achieve his goal
#Example Dictionary {"Mud_Donut":3000,"Slug_Eyes":1500,"Rat_Pasta":3500}

import sys

def ogreFood(dictionary):
    max_calories=0
    current_food=""
    for key in dictionary:
        if dictionary[key]>max_calories:
            max_calories=dictionary[key]
            current_food=key
    return current_food


testCases=[ ["Mud_Donut:3000,Slug_Eyes:1500,Rat_Pasta:3500", "Rat_Pasta"],["Gooey_Goblin_Grime:9000,Boy_Broth:8000,Poisoned_Cheese:7000", "Gooey_Goblin_Grime"]]

if __name__ == "__main__":
    input = sys.argv[1].split(',')
    final_input= {}
    for string in input:
        arr=string.split(':')
        food=arr[0]
        boolean=int(arr[1])
        final_input[food]=boolean
    input=final_input
    result = sys.argv[2]
    print(result)
    print(ogreFood(input))
    print(ogreFood(input)==result)