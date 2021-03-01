class A():
	def __init__(self, a='a'):
		self.a = a

	def get_a(self):
		return self.a

	def set_a(self, a):
		self.a=a

	def print_(self):
		print("a =", self.a)

	def print_branch(self):
		print("On branch local main")
