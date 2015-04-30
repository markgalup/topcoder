from collections import Counter

class PeacefulLine (object):


    def makeLine(self, x):
        possible = 0
        
        Counter(x)
        
        for i in Counter(x):
            if Counter(x)[i] > round(len(x)/2.0):
                possible += 1
    
        if possible != 0:
            return "impossible"
        else:
            return "possible"
                




print PeacefulLine().makeLine((1, 2, 3, 4))
# Returns: "possible"

print PeacefulLine().makeLine((1,1,1,2))
# Ret: "impossible"

print PeacefulLine().makeLine((1,1,2,2,3,3,4,4))
# Ret: "possible"


print PeacefulLine().makeLine((3,3,3,3,13,13,13,13))


print PeacefulLine().makeLine((3,7,7,7,3,7,7,7,3))
# "impossible"
print PeacefulLine().makeLine((3,3,3,3,13,13,13,13,3))
# "poss"


