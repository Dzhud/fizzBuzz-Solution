def fizzBuzz():
	for i in range(1, 16):
		 if i in [3, 6, 9, 12]:
			 i='Fizz'
		 if i in [5, 10]:
			 i='Buzz'
		 if i==15:
			 i='FizzBuzz'
		 print(i)

# Multiples of 3 and 5 return 'Fizz' and 'Buzz' respectively while 15 returns 'FizzBuzz'
