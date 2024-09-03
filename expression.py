#expression.py
#defines an expression class which models a mathematical expression
#for use with simpleCalculator.py

import re

#todo: refactor with normal class naming conventions
class Expression:
	#initializes expression to a StringVar which represents the
	#expression as a string
	#todo: handle errors using exceptions
	def __init__(self, stringVar):
		self.expression = stringVar
		self.errorFlag = False

	#concatenates user inputs into a string for evaluation
	#todo: handle error using exceptions
	def append(self, newCharacter):
		if self.errorFlag:
			self.clear()
			self.errorFlag = False
		self.expression.set(self.expression.get()+newCharacter)

	#calculates expression and replaces expression with the result
	#todo: handle errors using exceptions
	def calculate(self):
		if self.isValidExpression():
			precision = 0.00000001
			value = eval(self.convertIntsToFloats())
			truncatedValue = int(value)#this doesn't actually 
			#perform a truncation so it does not work as expected
			#in all cases
			#todo: use a function that performs truncation
			if abs(value - truncatedValue) < precision:
				self.expression.set(truncatedValue)
			else:
				self.expression.set(value)
		else:
			self.expression.set("Error")
			self.errorFlag = True

	#resets value of expression to ""
	def clear(self):
		self.expression.set("")

	#deletes last character from expression
	def delete(self):
		newExpression = self.expression.get()[:-1]
		self.expression.set(newExpression)

	#returns true if expression represents a valid mathematical expression
	def isValidExpression(self):
		return re.match(r"((\d*\.\d+)|(\d+)){1}([+\-*/]{1}((\d*\.\d+)|(\d+)){1})*\Z",
				self.expression.get()) != None

	#returns a new string where all integers in expression have been 
	#converted to floats
	def convertIntsToFloats(self):
		numbers = re.split(r"[-+/*]", self.expression.get())
		operations = re.split(r"\d*\.*\d*", self.expression.get())[1:-1]
		newexpr = ""
		for num in numbers:
			num = str(float(num))
			op = operations.pop(0) if operations else ""
			newexpr += num + op
		return newexpr

