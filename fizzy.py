# Multiples of 3 and 5 return 'Fizz' and 'Buzz' respectively while 15 returns 'FizzBuzz'

def fizzBuzz():
	# Solution 1
	'''
	for i in range(1, 16):
		 if i in [3, 6, 9, 12]:
			 i='Fizz'
		 if i in [5, 10]:
			 i='Buzz'
		 if i==15:
			 i='FizzBuzz'
		 print(i)
	'''
	# Solution 2
	for ii in range(1, 16):
                if ii == 15:
                        ii='FizzBuzz'
                elif ii % 3 == 0:
                        ii='Fizz'
                elif ii % 5 == 0:
                        ii='Buzz'
                print(ii)

if __name__ == "__main__":
	fizzBuzz()
