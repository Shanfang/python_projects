"""
INPUT: positive number greater than 1
OUTPUT: factorization of the number
"""
import pdb
factors = lambda n: [x for x in range(1, n+1) if n % x == 0]
is_prime = lambda n: len(factors(n)) == 2
prime_factors = lambda n: list(filter(is_prime, factors(n)))


def prime_factorization(n):
	n = int(n)
	f = prime_factors(n)

	if is_prime(n):
		return str(n)
	else:
		#pdb.set_trace()

		return str(f[0]) + ' * ' + prime_factorization(n/f[0])

if __name__ == '__main__':

		print('Enter a number to be factorized, or enter exit to exit the program.')
		number = 0
		#take input from the console until the user input exit
		while True:
			if number:
				print(prime_factorization(number))
			print('>>>', end = ' ')
			number = input()
			if number == 'quit':
				break