def task(list_):
    m = len([i for i in list_ if i % 2 == 0])
    n = len([i for i in list_ if i % 2 == 1])
    print(m)
    print(n)
    if n < m:
        # print('Больше четных')
        return 'Больше четных'
    elif n > m:
        # print("Больше нечетных")
        return "Больше нечетных"
    elif n == m:
        # print("колличество четных и нечетных равно")
        return "количество четных и нечетных равно"


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(task(list_))
