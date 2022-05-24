def introduction(name):
    txt = "Heyy!! {}, Welcome to my first attempt in a program! ".format(name)
    return txt


name = "Bruno"
print(introduction(name))


def getting_info(name, age, city, fav_color):
    info = ["Enter your name: ", "Enter your age: ", "Enter your City: ","Enter your Favorite Color: "]
    for c in info:
        x = input(info[c])

getting_info()
