#!/usr/bin/env python3


def greet_programmer():
    pass
    print("Hello, programmer!")


greet_programmer()


def greet(name="Engineer"):
    pass
    print(f"Hello, {name}!")


greet()


def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")


greet_with_default()


def add(num1=45, num2=55):
    pass
    return num1 + num2


add()


def halve(number=6.0):
    pass
    return number / 2


halve()
