import string

class FormatAmt(object):

	def amount(self, dollars, cents):
		if cents == 0:
			cents_string = "00"
			dollars_string = '{:,}'.format(dollars)
			total_amount = "$" + dollars_string + "." + cents_string
		elif cents > 9:
			cents_string = str(cents)
			dollars_string = '{:,}'.format(dollars)
			total_amount = "$" + dollars_string + "." + cents_string
		else:
			cents_float = cents * .01
			total_integer = dollars + cents_float
			total_string = '{:,}'.format(total_integer)
			total_amount = "$" + total_string

		
		
		return total_amount


test = FormatAmt()
print test.amount(123456, 0)	#Returns: "$123,456.00"
print test.amount(49734321, 9)	#Returns: "$49,734,321.09"
print test.amount(0, 99)	#Returns: "$0.99"
print test.amount(249, 30)	#Returns: "$249.30"
print test.amount(1000, 1)	#Returns: "$1,000.01"