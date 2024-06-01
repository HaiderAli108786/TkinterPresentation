from tkinter import *
from center_window import center_window

class Calculator:
	def __init__(self, root):
		self.root = root
		self.root.title("Simple Calculator")

		self.e = Entry(self.root, width=35, borderwidth=5)
		self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

		self.math = None
		self.f_num = None

		self.create_buttons()
		center_window(self.root)

	def create_buttons(self):
		button_1 = Button(self.root, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
		button_2 = Button(self.root, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
		button_3 = Button(self.root, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
		button_4 = Button(self.root, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
		button_5 = Button(self.root, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
		button_6 = Button(self.root, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
		button_7 = Button(self.root, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
		button_8 = Button(self.root, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
		button_9 = Button(self.root, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
		button_0 = Button(self.root, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
		button_add = Button(self.root, text="+", padx=39, pady=20, command=self.button_add)
		button_equal = Button(self.root, text="=", padx=91, pady=20, command=self.button_equal)
		button_clear = Button(self.root, text="Clear", padx=79, pady=20, command=self.button_clear)

		button_subtract = Button(self.root, text="-", padx=41, pady=20, command=self.button_subtract)
		button_multiply = Button(self.root, text="*", padx=40, pady=20, command=self.button_multiply)
		button_divide = Button(self.root, text="/", padx=41, pady=20, command=self.button_divide)

		button_1.grid(row=3, column=0)
		button_2.grid(row=3, column=1)
		button_3.grid(row=3, column=2)

		button_4.grid(row=2, column=0)
		button_5.grid(row=2, column=1)
		button_6.grid(row=2, column=2)

		button_7.grid(row=1, column=0)
		button_8.grid(row=1, column=1)
		button_9.grid(row=1, column=2)

		button_0.grid(row=4, column=0)
		button_clear.grid(row=4, column=1, columnspan=2)
		button_add.grid(row=5, column=0)
		button_equal.grid(row=5, column=1, columnspan=2)

		button_subtract.grid(row=6, column=0)
		button_multiply.grid(row=6, column=1)
		button_divide.grid(row=6, column=2)

	def button_click(self, number):
		current = self.e.get()
		self.e.delete(0, END)
		self.e.insert(0, str(current) + str(number))

	def button_clear(self):
		self.e.delete(0, END)

	def button_add(self):
		first_number = self.e.get()
		self.math = "addition"
		self.f_num = int(first_number)
		self.e.delete(0, END)

	def button_equal(self):
		second_number = self.e.get()
		self.e.delete(0, END)

		if self.math == "addition":
			self.e.insert(0, self.f_num + int(second_number))

		if self.math == "subtraction":
			self.e.insert(0, self.f_num - int(second_number))

		if self.math == "multiplication":
			self.e.insert(0, self.f_num * int(second_number))

		if self.math == "division":
			self.e.insert(0, self.f_num / int(second_number))

	def button_subtract(self):
		first_number = self.e.get()
		self.math = "subtraction"
		self.f_num = int(first_number)
		self.e.delete(0, END)

	def button_multiply(self):
		first_number = self.e.get()
		self.math = "multiplication"
		self.f_num = int(first_number)
		self.e.delete(0, END)

	def button_divide(self):
		first_number = self.e.get()
		self.math = "division"
		self.f_num = int(first_number)
		self.e.delete(0, END)


root = Tk()
calculator = Calculator(root)
root.mainloop()
