def sumTo(aBound):
    """Return the sum of 1 + 2 + 3..."""
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber += 1
    return theSum
print(sumTo(4))
##########################################
count = 0
eve_nums = []
while count <= 15:
    if count % 2 == 0:
       eve_nums.append(count)
    count += 1
print(eve_nums)
########################################
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx += 1
print(tot)
print(idx)
##################################
def litener_loop(x):
    total = 0
    pirces = []
    while (total < x):
        y = float(input("Enter the number here: "))
        total += 1
        pirces.append(y)
    return pirces

###############################################
x = 0
while x < 10:
    print("W are increment x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done we done with our loop")
############################################
count = 0
while count <= 15:
    count += 1
####################################
def get_pos(x):

    x=x.lower()
    a=x.strip()
    c=0
    for i in a:
        i=strip_punctuation(i)
        if i in positive_words:
            c+=1
    return c





