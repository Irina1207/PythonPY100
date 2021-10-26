def task(list_):
    m = list_[0]
    print (m)
    n = len([i for i in list_ if i > m])
    print(n)
    # for i in list_:
    #     n = len([i for i in list_ if i > m])
    #     print (n)
    return f"количество элементов больше первого элемента в списке = {n}"

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(task(list_))
