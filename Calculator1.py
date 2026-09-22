import streamlit as st

"""Calculator core functions.

This module provides simple arithmetic functions that can be used
from a CLI or imported by a Streamlit app.
"""

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


def _streamlit_app():
	st.title("Simple Calculator")

	a = st.number_input("Enter value of a:", value=0.0, format="%.2f")
	b = st.number_input("Enter value of b:", value=0.0, format="%.2f")

	st.write("===============")
	st.write("**Results:**")

	if st.button("Calculate"):
		st.write(f"Addition: {add(a, b)}")
		st.write(f"Multiplication: {mul(a, b)}")
		st.write(f"Subtraction: {sub(a, b)}")

		try:
			st.write(f"Division: {div(a, b)}")
		except ZeroDivisionError:
			st.error("Division Error: Cannot divide by zero!")

		try:
			st.write(f"Modulo: {mod(a, b)}")
		except ZeroDivisionError:
			st.error("Modulo Error: Cannot perform modulo by zero!")
	st.write("===============")


if __name__ == "__main__":
	_streamlit_app()
