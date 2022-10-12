## Factorial

'''def factorial(x):
    factorials = 1
    for i in range(1, x + 1):
        factorials = factorials * i
        i += 1

    print(factorials)


user_input = int(input("Enter the number"))
factorial(user_input)
'''


'''def sqsum(y):
    sum1 = 0
    for i in range(1, y + 1):
        sum1 = i ** 2 + sum1
    print(sum1)

user_input1 = int(input("Enter the number"))
sqsum(user_input1)
'''


'''def prime(z):
        if z % 2 == 0:
            print(f'{z}' + " is a prime number")
        else:
            print(f'{z}' + " is not a prime number")


user_input2 = int(input("Enter the number: "))
prime(user_input2)
'''

#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6

'''def number(a):
    for i in range(a+1):
        if i == 3 or i == 6:
            continue
        print(i)


number(6)'''


'''def fizzbuzz(a):
    for i in range(1, a+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")
        elif i % 5:
            print("Buzz")

fizzbuzz(50)'''


def matrix(x, y):
    n = [[0], [0]]
    n[0] = x
    n[1] = y
    for i in n:
        for j in i:
            print(n[0], n[1])


ab = int(input("Enter the number 1: "))
ba = int(input("Enter the number 2 : "))

matrix(ab, ba)

