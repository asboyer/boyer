import boyer

"""
All functions:
- hello
- delay_print
- clear
- get_num
"""

print('\n_____hello()_____')
# input is a name

# prints output
print(boyer.hello("Eric"))
# output: "Hello Eric, my name is Andrew Boyer"

# stores output in variable
hello = boyer.hello("Kevin")
print(hello + ".")
# output: "Hello Kevin, my name is Andrew Boyer." 

print('\n_____delay_print()______')
# input is a string
# optional input includes: level(speed), end(ending string)
#                          default: 4    default: ''

boyer.delay_print("Hello, I am a computer")
# output: "Hello, I am a computer" (each char is printed after 40 milliseconds)

boyer.delay_print("Hello, I am a computer", level=10)
# boyer.delay_print("Hello, I am a computer", 10)
# specification: functions can be used as positional arguments, or specify
# output: "Hello, I am a computer" (each char is printed after 100 milliseconds)

boyer.delay_print("Hello, I am a computer", end='!')
# output: "Hello, I am a computer!" ('!' is added to the end)

# use with all positional arguments:
boyer.delay_print("Hello, I am a computer", 1, '.')
# output: "Hello, I am a computer." (each char is printed after 10 milliseconds)

print('\n_____clear()_____')
# no input

boyer.clear()
# output: none (just clears the screen)

print('\n_____memify()_____')
# input: text you wanted 'memified'

print(boyer.memify('hello there'))
# output: random, could be 'hELlO tHeRe' or 'hELLo THERE'

print('\n_____get_num()_____')
# input: all optional
# optional input includes: prompt(str),                start(lowest possible value)
#                          default: "Enter a number"   default: "none"

# finish(highest possible value), integer(boolean, requires integer)
# default: "none"                 default: False

# round_up(boolean, specifies if rounding up), round_num(the minimum remainder for rounding up)
# default: False                               default: 0.5

# error_message(boolean, but can be any string)
# default: False

# for all cases below, output: "Output: (number entered)"

print(f"Output: {boyer.get_num()}")
# specifications: if a number is not entered, "Please enter a number!" will be printed
#                 prompt is "Enter a number: "

print(f"Output: {boyer.get_num(prompt='Please enter a number')}")
# specification: prompt is "Please enter a number: " (NOTE: the ": " are automatically added)

print(f"Output: {boyer.get_num(start=0)}")
# specification: if you enter a number less than 0, you will be prompted to try again

print(f"Output: {boyer.get_num(finish=0)}")
# specification: if you enter a number greater than 0, you will be prompted to try again

print(f"Output: {boyer.get_num(integer=True)}")
# specification: prompt will only accept integer values, if you enter a float, you will be prompted to try again

print(f"Output: {boyer.get_num(round_up=True)}")
# specification: the final value will be "rounded up" if the value is greater than or equal to 0.5

print(f"Output: {boyer.get_num(round_up=True, round_num=0.7)}")
# specification: the final value will be "rounded up" if the value is greater than or equal to 0.7

print(f"Output: {boyer.get_num(error_message="Wrong numba!")}")
# specification: rather than the default error messages, every error message will prompt with "Wrong numba!"

print(f"Output: {boyer.get_num('Number', 5, 10, False, True, 0.9, "Enter the right number!")}")
# NOTE: these are all positional arguments
# specifications: prompt is "Number:"
#                 minimum accepted value is 5
#                 maximum accepted value is 10
#                 integer input is not required
#                 rounding up is will happen if the tens the place is greater than or equal to 9
#                 all error messages will be "Enter the right number!"