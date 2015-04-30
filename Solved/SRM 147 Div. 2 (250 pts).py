import string

class CCipher(object):
	
	def encode(self, cipherText, shift):

		cipherList = list(cipherText)
		translateList = []

		for ch in cipherList:
			if ch.islower():
				alphabet = string.ascii_lowercase
				shifted_alphabet = alphabet[shift:] + alphabet[:shift]
				table = string.maketrans(alphabet, shifted_alphabet)
				cipherLetterLower = ch.translate(table)
				translateList.append(cipherLetterLower)
			elif ch.isupper():
				alphabet = string.ascii_uppercase
				shifted_alphabet = alphabet[shift:] + alphabet[:shift]
				table = string.maketrans(alphabet, shifted_alphabet)
				cipherLetterUpper = ch.translate(table)
				translateList.append(cipherLetterUpper)
		translateString = "".join(translateList)
		return translateString

	def decode(self, cipherText, shift):

		cipherList = list(cipherText)
		translateList = []
		shift = -shift

		for ch in cipherList:
			if ch.islower():
				alphabet = string.ascii_lowercase
				shifted_alphabet = alphabet[shift:] + alphabet[:shift]
				table = string.maketrans(alphabet, shifted_alphabet)
				cipherLetterLower = ch.translate(table)
				translateList.append(cipherLetterLower)
			elif ch.isupper():
				alphabet = string.ascii_uppercase
				shifted_alphabet = alphabet[shift:] + alphabet[:shift]
				table = string.maketrans(alphabet, shifted_alphabet)
				cipherLetterUpper = ch.translate(table)
				translateList.append(cipherLetterUpper)
		translateString = "".join(translateList)
		return translateString


test = CCipher()
print test.decode("VQREQFGT", 2)	#Returns: "TOPCODER"
print test.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)	#Returns: "QRSTUVWXYZABCDEFGHIJKLMNOP"
print test.decode("TOPCODER", 0)	#Returns: "TOPCODER"
print test.decode("ZWBGLZ", 25)	#Returns: "AXCHMA"
print test.decode("DBNPCBQ", 1)	#Returns: "CAMOBAP"
print test.decode("LIPPSASVPH", 4)	#Returns: "HELLOWORLD"

