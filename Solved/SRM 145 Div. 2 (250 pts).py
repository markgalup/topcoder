class ImageDithering(object):
	
	def count(self, screen, dither):

		#screenlist = list(screen)

		total = 0
		for i in dither:
			for n in i:
				for x in screen:
					if n == x:
						total += 1

		return total



test = ImageDithering()
print test.count("BW", ("AAAAAAAA",
 "ABWBWBWA",
 "AWBWBWBA",
 "ABWBWBWA",
 "AWBWBWBA",
 "AAAAAAAA")) 	#Returns: 24

print test.count("BW", ("BBBBBBBB",
 "BBWBWBWB",
 "BWBWBWBB",
 "BBWBWBWB",
 "BWBWBWBB",
 "BBBBBBBB"))	#Returns: 48

print test.count("ACEGIKMOQSUWY", ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX"))	#Returns: 150

print test.count("CA", ("BBBBBBB",
 "BBBBBBB",
 "BBBBBBB"))	#Returns: 0

print test.count("DCBA", ("ACBD"))	#Returns: 4
