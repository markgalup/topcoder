class GuessTheNumber(object):

    def noGuesses(self, upper, answer):
        lower = 1
        guesses = 0
        x = (int(round((upper - lower) / 2.0)))
        
        while True:
            guesses += 1
            if x == answer:
                return guesses
            elif x > answer:
                upper = x
                x = (int(round((upper-lower) /2.0) + lower))
            else:
                lower = x
                x = (int(round((upper-lower) /2.0) + lower))

print GuessTheNumber().noGuesses(9, 6)  #Returns: 3
print GuessTheNumber().noGuesses(1000, 750) #Returns: 2
print GuessTheNumber().noGuesses(643, 327)  #Returns: 7
print GuessTheNumber().noGuesses(157, 157)  #Returns: 8
print GuessTheNumber().noGuesses(128, 64)   #Returns: 1
