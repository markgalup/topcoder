class DivisorDigits(object):

    def howMany(self, number):
    	num_list = list(str(number))
        num_list = map(int, num_list)
        divisors = 0

        for i in num_list:
        	if i > 0 and number % i == 0:
        		divisors += 1
        return divisors



test = DivisorDigits()
print test.howMany(12345)	#Returns: 3
print test.howMany(661232)	#Returns: 3
print test.howMany(5252752527)	#Returns: 0
print test.howMany(730000000)	#Returns: 0