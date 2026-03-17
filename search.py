mylist = [2, 4, 5]
def search(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            return 1
        