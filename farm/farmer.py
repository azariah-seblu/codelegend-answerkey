# Given a normal name (string), return it to the farmer in the way 
# he wants it

def name_horse(name):
    return name[-1].upper()+name[::-1][1:].lower()