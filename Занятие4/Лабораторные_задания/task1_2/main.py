#def kvadr(nn, mm):
 #   list_ = [
 #       i ** 2 if i % 2 == 1 for i in range(nn, mm +1)
  #  ]
 #   return list_


if __name__ == "__main__":
    n = 1
    m = 11
    print([i ** 2 for i in range(n, m +1) if i % 2 == 1])
 #   print(kvadr(n, m))
