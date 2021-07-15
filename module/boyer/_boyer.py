"""
boyer contains a set of functions that are useful to Andrew Boyer

docs: https://github.com/asboyer2/boyer/tree/master/docs
"""
import sys as _sys
import time as _time
import os as _os
import random as _random

__all__ = ['hello', 'delay_print', 'clear', 'get_num', 'memify', 'clean', 'encrypt', 'decrypt', 'capitalize']

def hello(name):
    """Takes in a name, greets the person of that name with a string return

    Args:
        name[str]: the name of the person

    Returns:
        a string
    """
    string = f"Hello {name}, my name is Andrew Boyer"
    return string

def delay_print(string, level=4, end=''):
    """Takes in string, prints one character at a time on a certain interval

    Args:
        string[str]: the string to be printed
        level[int]: determines the speed at which chars are printed, the higher the level,
        the slower the chars are printed
        end[str]: the string that will be printed at the end

    Returns:
        void (returns nothing)
    """

    speed = 0.01 * level

    for char in string:
        _sys.stdout.write(char)
        _sys.stdout.flush()
        _time.sleep(speed)
    print(end)

def clear():
    """Clears the terminal screen using the appropriate command specific to the os

    Args:
        void (no args)

    Returns:
        void (returns nothing)
    """
    if _sys.platform.startswith('win32'):
        _os.system('cls')
    else:
        _os.system('clear')

def memify(text):
    """Returns the inputted string with random letters capitalized

    Args:
        text[str]: the text you want to modified

    Returns:
        new[str]: the modified text
    """
    new = []
    for i in text:
        r = _random.randint(0, 1)
        if r == 1:
            new.append(i.upper())
        else:
            new.append(i.lower())
    new = ''.join(new)
    return new

def clean(string):
    return string.strip().lower()

def encrypt(string, key=3, cipher='caesar', alphabet='abcdefghijklmnopqrstuvwxyz'):
    def find(string1, char):
        for i in range(len(string1)):
            if string1[i] == char:
                return i
        return -1
    def caesar():
        finalString = ''
        for character in string.strip():
            upper = False
            if character == character.upper():
                upper = True
            position = find(alphabet, character.lower())
            if position == -1:
                finalString += character
            else:
                newPosition = (position + key) % len(alphabet)
                if upper:
                    finalString += alphabet[newPosition].upper()
                else:
                    finalString += alphabet[newPosition]
        return finalString
    if cipher == 'caesar':
        return caesar()


def decrypt(string, key=3, cipher='caesar', alphabet='abcdefghijklmnopqrstuvwxyz'):
    def find(string1, char):
        for i in range(len(string1)):
            if string1[i] == char:
                return i
        return -1
    def caesar():
        finalString = ''
        for character in string.strip():
            upper = False
            if character == character.upper():
                upper = True
            position = find(alphabet, character.lower())
            if position == -1:
                finalString += character
            else:
                newPosition = (position - key) % len(alphabet)
                if upper:
                    finalString += alphabet[newPosition].upper()
                else:
                    finalString += alphabet[newPosition]
        return finalString
    if cipher == 'caesar':
        return caesar()

def capitalize(string, sentence=False):
    if len(string) < 2:
        return string.upper()
    if sentence:
        return string[0].upper() + string[1:]
    finalString = ""
    words = string.strip().split()
    for word in words:
        finalString += word[0].upper() + word[1:].lower() + " "
    return finalString.strip()

def get_num(prompt="Enter a number", start="default", finish="default",
            integer=False, round_up=False, round_num=0.5, error_message=False):
    """Ensures the user enters a valid number utilizing the default input() function

    Args:
        prompt[str]: the string that shows up as the prompt
        (": " are added to the end of the string)
        start[int or float]: the value that the number must be greater than (start < num)
        finish[int or float]: the value that the number must be less than (finish > num)
        integer[boolean]: true or false statement that decides if the value must be an int
        round_up[boolean]: true or false statement that decides if it will "round up" the number
        round_num[float]: float that will determine whether or not a rounding is appropriate
        error_message[boolean]: if not false, this custom error message will override all others

    Returns:
        number[double]: returns the number that meets all requirements
        will return int if integer=True
    """
    while True:
        try:
            number = float(input(f'{prompt}: '))
            if integer:
                if number - int(number) != 0:
                    if not error_message:
                        print("Please enter an integer!")
                    else:
                        print(error_message)
                    continue
                if round_up:
                    num = number - int(number)
                    if num >= round_num:
                        number = int(number) + 1
                else:
                    number = int(number)
        except ValueError:
            if not error_message:
                print("Please enter a number!")
            else:
                print(error_message)
            continue
        # if default, skip and just return num
        if finish != "default":
            if start != "default":
                if start <= number <= finish:
                    return number
                if not error_message:
                    print(f"Enter a value between {start} and {finish}")
                else:
                    print(error_message)
                continue
            if number <= finish:
                return number
            if not error_message:
                print(f"Enter a value below {finish}")
            else:
                print(error_message)
            continue
        if start != "default":
            if number >= start:
                return number
            if not error_message:
                print(f"Enter a value above {start}")
            else:
                print(error_message)
            continue
        return number
