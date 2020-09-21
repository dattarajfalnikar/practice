

def demo(a, b):
	print a
	print b

class command:
	def __init__(self, cmd, *args):
		self.cmd = cmd
		self.args= args
	
	def __call__(self):
		return apply(self.cmd, self.args)


c = command(demo, 'str1_test', 'another')
print c()
