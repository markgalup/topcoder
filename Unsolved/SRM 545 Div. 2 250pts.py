from operator import __and__

class ANDEquation(object):

    def restoreY(self, A):
        A = list(A)
        for i in range(len(A)):
            if A[i] == reduce(__and__, A[:i] + A[i+1:]):
                return A[i]
        else:
            return -1


print ANDEquation().restoreY((1, 3, 5))
# 1
print ANDEquation().restoreY((31, 7))
# -1
print ANDEquation().restoreY((31, 7, 7))
# 7
print ANDEquation().restoreY((191411,256951,191411,191411,191411,256951,195507,191411,192435,191411,
 191411,195511,191419,191411,256947,191415,191475,195579,191415,191411,
 191483,191411,191419,191475,256947,191411,191411,191411,191419,256947,
 191411,191411,191411))


