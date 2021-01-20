class Stack:
	def __init__(self):
		self.max_len = 8
		self.top = -1
		self.stack = list() 
	def push_data(self, value):
		if len(self.stack) < self.max_len:
			self.stack+=list(value)
			self.top+=1
			print('{} is successfully added to stack'.format(value))
		else:
			print('stack overflow!')		
	def pop_data(self):
		if self.top != -1:
			del self.stack[-1]	
			self.top-=1
			print('successfully removed from stack')	
	def is_empty(self):
		if self.top == -1:
			print('Stack is empty!')
		else:
			print('Stack is not empty!')
	
	def peek_data(self):
		print(self.stack)




if __name__ == '__main__':
	my_stack = Stack()
	my_stack.push_data('2')
	my_stack.push_data('1')
	my_stack.peek_data()
	my_stack.is_empty()
	my_stack.pop_data()
	my_stack.peek_data()
