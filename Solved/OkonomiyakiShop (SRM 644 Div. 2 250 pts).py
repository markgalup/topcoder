class OkonomiyakiShop(object):

    def count(self, osize, K):
        meals = 0
        

        for i in range(len(osize)-1):
            combos = len(osize)-i
            for j in range(1, (combos)):
                if abs(osize[i] - osize[i+j]) <= K:
                    meals += 1
        return meals




print OkonomiyakiShop().count((1,4,6,7,9), 3)
# Returns: 6
print OkonomiyakiShop().count((1,1,3,3,3), 2)
# Returns: 10

print OkonomiyakiShop().count((1,5,9,14,20), 3)
# Returns: 0

print OkonomiyakiShop().count((7,2,6,3,4,2,7,8,3,4,9,1,8,4,3,7,5,2,1,9,9,4,5), 6)
# Returns: 234
