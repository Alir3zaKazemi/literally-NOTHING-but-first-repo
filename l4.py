
my_list = [28,75,83,745,96,12,108,234]
def mx(my_list):
    max = 0
    x = 0
    y = len(my_list)
    for i in range(y) :
        if my_list[x] > max :
            max = my_list[x]
        x += 1
    print(max)
    print("DONE !!!!")

mx(my_list)
