#if __name__ == "__main__":
#    n = 11
#    sum_ = 0
#    for i in range (n)
#        if i % 2 == 0
#            sum_ = sum_ + 1
#    print (sum_)
#    print([sum_ = i + 1 for i in range(n) if i % 2 == 0])

def kvadr(list_):
    list_= len([i for i in list_ if i % 2 == 0])

    return list_

if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6]
    print(kvadr(list_))