def task(epsilon=0.00010):
    sum = 0
    n = 1
    item_n = 1 / 2 ** n
    while item_n >= epsilon:
        sum_ += item_n
        n += 1

    while True:
        item_n >= epsilon:
        if not (item_n >= epsilon):
            break

        sum_ += item_n
        n += 1

    return sum_

if __name__ == "__main__":
    print(task)



