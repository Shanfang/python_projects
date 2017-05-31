"""
INPUT: a sequence of numbers
OUTPUT: type of credit card, or message informing that the card number is invalid

alogrithm: luhn validation
regex: www.regular-expressions.info/creditcard.html
 	   and https://github.com/dotslash/Projects/blob/master/solutions/credit_card_validator.py
"""

import re
import sys
import pdb

visa = r'^4[0-9]{12}(?:[0-9]{3})?$', "Visa"
mastercard = r'^5[1-5][0-9]{14}$', "Master Card"
am_express = r'^3[47][0-9]{13}$', "American Express"
diners_club = '^3(?:0[0-5]|[68][0-9])[0-9]{11}$', "Diners Club"
discover = r'^6(?:011|5[0-9]{2})[0-9]{12}$', "Discover"
jcb = r'^(?:2131|1800|35\d{3})\d{11}$', "JCB"

cards = [visa, mastercard, am_express]
invalid_message = "Invalid Card Number"
unidentified_message = "Unidentified Card Type"
def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

#check a given card number using the above function
def is_luhn_valid(card_number):
	return luhn_check(card_number) == 0


def main(card_str):
	card_str1 = card_str.replace(' ', '')
	card_number = int(card_str1.replace('-', ''))
	#print('Befor the try except block...')
	try:
		if not is_luhn_valid(card_number):
			#print('This is not a valid number!!!')
			return invalid_message
		for exp,message in cards:
			match_result = re.match(exp, str(card_number))
			if match_result:
				return message

		return unidentified_message

	except:
		return invalid_message	
		#return 'in the except block'

if __name__ == "__main__":
	print("Please enter a sequence of numbers, I'll check if it is a valid credit card number")
	card_str = input()
	print(main(card_str))
	#print('The number is:') + is_luhn_valid(card_number)
	