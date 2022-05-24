L2 = ['Cherry', 'Apple', 'Blueberry']

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)

L2.sort()
print(L2)


print(sorted('Apple'))
print(sorted('Apple', reverse = True))
print(sorted(L2, reverse = True))

#####################################

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
for y in L1:
    print(absolute(y))

########################################
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))

print("-------------------")

def sorting_dic(List_0):
    dic_1 = {}

    for x in List_0:
        if x in dic_1:
            dic_1[x] = dic_1[x] + 1
        else:
            dic_1[x] = 1

    y = sorted(dic_1, key=lambda k : dic_1[k], reverse = True)
    for k in y:
        print(" {} appears {} times".format(k, dic_1[k]))



fruits = ["peach", "kiwi", "apple", "blueberry", "mango", "pear"]
new_order = sorted(fruits, key=lambda fruit_name : (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)






