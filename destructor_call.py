
class A:
	def __init__(self):
		print ('Init Called')

#	def __new__(cls):
#		print('new called')


	def __del__(self):
		print('Delete Called')



a=A()
del a
