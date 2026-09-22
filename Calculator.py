
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a / b

def mod(a, b):
	if b == 0:
		raise ZeroDivisionError("modulo by zero")
	return a % b


def _cli():
	try:
		a = float(input("enter value of a: "))
		b = float(input("enter value of b: "))
	except ValueError:
		print("Invalid input — please enter numbers.")
		return

	print("===============")
	print("sample calculator")
	print("===============")
	print("addition=", add(a, b))
	print("multiplication=", mul(a, b))
	print("sub=", sub(a, b))
	try:
		print("div=", div(a, b))
	except ZeroDivisionError:
		print("div= Error (division by zero)")
	try:
		print("Rem=", mod(a, b))
	except ZeroDivisionError:
		print("Rem= Error (modulo by zero)")
	print("===============")


if __name__ == "__main__":
	_cli()
