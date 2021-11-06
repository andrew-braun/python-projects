# FizzBuzz solution #1 (basic)
def fizz_buzz_1():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(str(number))


fizz_buzz_1()


# FizzBuzz solution #2 (using list comprehension)
def fizz_buzz_2():
    fizz_buzz_numbers = ["FizzBuzz" if (number % 3 == 0 and number % 5 == 0)
                         else "Fizz" if (number % 3 == 0)
                         else "Buzz" if (number % 5 == 0)
                         else str(number)
                         for number in range(1, 101)]
    print(*fizz_buzz_numbers, sep="\n")


fizz_buzz_2()
