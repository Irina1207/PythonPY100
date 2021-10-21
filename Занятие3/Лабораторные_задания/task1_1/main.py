def main():
    total = 0
    n = 0
    b = 1
    bb = 0
    while True:
        if total > 500:
            break
        b = b + 1
        bb = bb + b * b
        total = 1 + bb
        n = n + 1
        print (n)
    return n

if __name__ == "__main__":
    print(main())
