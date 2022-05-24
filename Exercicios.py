count = 0
eve_nums = []
while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count += 1
#####################################################
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = elem + tot

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx += 1

def stop_count(list1):
    new_list = []
    count = 0
    limit  = 4
    while count < limit:

        new_list.append(list1[count])
        count += 1
    return new_list

list_1 = [2, 5, 6, 7, 8, 9, 1, 25, 30, 6, 33]

print(stop_count(list_1))

##################################################
def sublist(list_3):
    new_list = []
    idx = 0
    while idx < len(list_3):

        if list_3[idx] == "STOP":
            break
        else:
            new_list.append(list_3[idx])
        idx += 1
    return new_list