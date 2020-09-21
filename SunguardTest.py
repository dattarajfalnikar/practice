

def fizzBuzz(n):
    if n:
      if n % 15 == 0:
	  print('fizzbuzz')
      elif n % 3==0:
          print('fizz')
      elif n % 5==0:
          print('buzz')
      else:
          return 0


fizzBuzz(10)
fizzBuzz(3)
fizzBuzz(15)
fizzBuzz(30)
fizzBuzz(35)
