class YahtzeeScore(object):

    def maxPoints(self, toss):
        high_die = max(toss)
        #return high_die     #this is for testing the input
        ones, twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0, 0

        for d in toss:
        	if d == 1: 
        		ones += 1
        	elif d == 2:
        		twos += 2
        	elif d == 3:
        		threes += 3
        	elif d == 4:
        		fours += 4
        	elif d == 5:
        		fives += 5
        	elif d == 6:
        		sixes += 6
        
        high_multiple = max(ones, twos, threes, fours, fives, sixes)

        if high_multiple > high_die:
        		return high_multiple
        return high_die




test1 = YahtzeeScore()
print test1.maxPoints((2, 2, 3, 5, 4))	#Returns: 5
print test1.maxPoints((6, 4, 1, 1, 3))	#Returns: 6
print test1.maxPoints((5, 3, 5, 3, 3))	#Returns: 10