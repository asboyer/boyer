import sys as _sys
import time as _time

__all__ = ['hello', 'delay_print', 'get_int']

def hello(name):
	string = f"Hello {name}, my name is Andrew Boyer"
	print(string)
	return string

def delay_print(s, end=''):
	for c in s:
		_sys.stdout.write(c)
		_sys.stdout.flush()
		_time.sleep(0.04)
	print(end)

def get_int(prompt, start=0, finish=0):
	while True:
		try:
			x = int(input(f"{prompt}: "))
		except ValueError:
			print("Please enter an integer!")
		if finish != 0: 
			if start != 0:
				if x < finish and x > start:
					return x
			elif x < finish:
				return x
			else:
				print(f"Enter a value between {start} and {finish}")
