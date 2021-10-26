def task(list_: list) -> list:
    mean = sum(list_)
    print (mean)
    return [item for item in list_ if item > mean]

if __name__ == "__main__":
    list_ = [1,2,3,4,5]
    print(task(list_))
