def factorial(nn):
    fact = 0
    a = 1
    for i in range (1, nn):
        a = a + 1
       fact = fact + fact * a

    return fact

if __name__ == "__main__":
    print(factorial(n))
