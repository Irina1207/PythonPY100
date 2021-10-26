def factorial(nn):
    fact = 0
    a = 1
    for i in range (1, nn):
        fact = fact + fact * a
        a = a + 1

    return fact

if __name__ == "__main__":
    print(factorial(10))
