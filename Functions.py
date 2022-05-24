
x = "Segura peao"

def hello(x, y):
    print("Hello World I am getting there !! " + x , y)

hello("Pastor", 15)

def add(a, b):
    total = a + b
    print(total)
my_var = 11

add(my_var, 3)
#############################################
def square(x):
    y = x * x
    return y
to_square = 10
square_result = square(to_square)
print("Hello people this was the value entered: {} and this is the final result : {}".format(to_square, square_result))
print(square(15))
################################################
def weird():
    print("here")
    return 5
x = weird()
print(x)
######################################################################
def longer_than_five(list_of_names):
    for names in list_of_names:
        if len(names) > 5:
            return True
    return False

list1 = ["Leco", "Leo", "Aya", "Iago", "Caio", "Omar"]
list2 = ["Barbara", "Bruno", "Rosane", "Tabata", "Olivia", "Geraldo"]
print(longer_than_five(list1))
print(longer_than_five(list2))
#################################################################
def total(lst):
    lst = [1, 5, 7]
    tot = 0
    for num in lst:
        tot = tot + num
    return tot
#################################################
def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c

a = -5
b = 2
c = 10

result = sum_of_squares(a, b, c)
print(result)

def f(a, L = []):
    L.append(a)
    return L
print(f(2))
print(f(4))

###########################################
initial = 7
def f2(x, y = 3, z = initial):
    print("x, y, z are: " + str(x) + ", " + str(y) + ", " + str(z))
print(f2(2))
print(f2(2, 5))
print(f2(2, 5, 8))
##############################################
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
    ####################################
    # this works
    names = ["Jack", "Jill", "Mary"]
    for n in names:
        print("'{}!' she yelled. '{}! {}, {}!'".format(n, n, n, "say hello"))

    # but this also works!
    names = ["Jack", "Jill", "Mary"]
    for n in names:
        print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n, "say hello"))


