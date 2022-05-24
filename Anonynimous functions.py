def f(x):
    return x - 1
print(f(3))
print(f)
print(type(f))

print(lambda x : x - 1)

lf = lambda x : x-1


#############################
def last_char(s):
    return s[-1]

last_char = lambda  s: s[-1]



def test(x, y = True, dict1 = {2:3, 4:5, 6:8} ):
    if y == True:
        for key in dict1:
            idx = 0
            if key == x:
                return dict1[key]
            else:
                y = False
            idx += 1
    return y



def checkingIfIn(string_1, direction = True, d = {"apple" : 2, "pear" : 1, "fruit" : 19, "orange" : 5, "banana" : 3, "grapes" : 2, "watermelon" : 7}):
    if direction == True:
        for key in d:
            if key == string_1:
                direction = True

    elif direction == False:
        for key in d:
            if string_1 != key:
                 return True
            else:
                return False
    return direction


###################################
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]




print(checkingIfIn("carrot"))



