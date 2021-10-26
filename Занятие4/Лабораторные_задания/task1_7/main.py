def task(list_):
     from statistics import mean
     mean_ = mean(list_)
     print (mean_)
     list2 = []
     for i in list_:
         list2.append(i-mean_)
     print (list2)
     return list2

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    # list2 = []
    # from statistics import mean
    # mean_ = mean(list_)
    # for i in list_:
    #     list2.append(i-mean_)
    # print (list2)
    print(task(list_))
