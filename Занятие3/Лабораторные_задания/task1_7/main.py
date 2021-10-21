def skolko_meczev (a, b, c):

    # total = (a + b) - c
    n = 0
    while True:
        if a + b < c:
            break

        a = (a + b) - c
        c = c + c * 0.03
        n = n + 1
        print (n)
    return n

if __name__ == "__main__":
    nakopl = 7
    stip = 100
    rashod = 105
    print(skolko_meczev(nakopl, stip, rashod))
