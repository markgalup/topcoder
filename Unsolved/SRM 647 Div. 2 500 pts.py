from collections import Counter

class TravellingSalesmanEasy(object):

    def getMaxProfit(self, M, profit, city, visit):
        Counter(visit)
        maxProfitList = [[0] for i in range(1, M+1)]
        maxProfit = 0
        for i in range(len(city)):
                maxProfitList[city[i]-1].append(profit[i])
        print maxProfitList
        
        for i in visit:
             (max(maxProfitList[i-1])*Counter(visit)[i])

        return maxProfit




print TravellingSalesmanEasy().getMaxProfit(2, (3,10), (1,1), (2,1))
# 10

print TravellingSalesmanEasy().getMaxProfit(6, (77,33,10,68,71,50,89), (4,1,5,6,2,2,1), (6,5,5,6,4))
# 155

print TravellingSalesmanEasy().getMaxProfit(7, (22,91,53,7,80,100,36,65,92,93,19,92,95,3,60,50,39,36,2,30,63,84,2), (5,3,4,3,6,5,6,6,5,2,7,6,3,2,6,1,7,4,6,3,7,2,5), (5,7,1,3,6,2,5,7,3,6,3,2,7,3,1,3,1,7,2,3,1,1,3,1,6,1))

