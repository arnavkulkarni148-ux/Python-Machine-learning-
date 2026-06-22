def main():
    from sys import getsizeof

    number1 = 10
    number2 = 20.2
    Great = "Hello"

    print(type(number1))
    print(type(number1))
    print(type(Great))

    print(id(number1))
    print(id(number2))
    print(id(Great))

    print(getsizeof(number1))
    print(getsizeof(number2))
    print(getsizeof(Great))


if __name__ == "__main__":
    main()