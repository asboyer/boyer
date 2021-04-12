"""
boyer contains a set of functions that are useful to Andrew Boyer

docs: https://github.com/asboyer2/boyer/tree/master/docs
"""
import sys as _sys
import time as _time
import os as _os

__all__ = ['hello', 'delay_print', 'clear', 'get_num']

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

def get_num(prompt="Enter a number", start="default", finish="default",
            integer=False, round_up=False, round_num=0.5):
    """Ensures the user enters a valid number utilizing the default input() function

    Args:
        prompt[str]: the string that shows up as the prompt
        (": " are added to the end of the string)
        start[int or float]: the value that the number must be greater than (start < num)
        finish[int or float]: the value that the number must be less than (finish > num)
        integer[boolean]: true or false statement that decides if the value must be an int
        round_up[boolean]: true or false statement that decides if it will "round up" the number
        round_num[float]: float that will determine whether or not a rounding is appropriate

    Returns:
        number[double]: returns the number that meets all requirements
        will return int if integer=True
    """
    while True:
        try:
            number = float(input(f'{prompt}: '))
            if integer:
                if number - int(number) != 0:
                    print("Please enter an integer!")
                    continue
                if round_up:
                    num = number - int(number)
                    if num >= round_num:
                        number = int(number) + 1
                else:
                    number = int(number)
        except ValueError:
            print("Please enter a number!")
            continue
        if finish != "default":
            if start != "default":
                if start < number < finish:
                    return number
                print(f"Enter a value between {start} and {finish}")
                continue
            if number < finish:
                return number
            print(f"Enter a value below {finish}")
            continue
        if start != "default":
            if number > start:
                return number
            print(f"Enter a value above {start}")
            continue
        return number
