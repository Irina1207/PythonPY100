def task(list_):
    list2 = []
    a = 0
    for i in list_:
        if i > a:
            list2.append(i**3)
        if i < a:
            list2.append(0)
    print (list2)
    return list2

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print (task(list_))
