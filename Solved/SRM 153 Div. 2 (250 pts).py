class MostProfitable(object):

	def bestItem(self, costs, prices, sales, items):
		costs, prices, sales, items = list(costs), list(prices), list(sales), list(items)
		profit = []
		for i in range(len(items)):
			margin = prices[i] - costs[i]
			profit.append(margin * sales[i])
		best_profit_index = profit.index(max(profit))
		if max(profit) > 0:
			return items[best_profit_index]
		else:
			return ""


test = MostProfitable()
print test.bestItem((100,120,150,1000), (110,110,200,2000), (20,100,50,3), ("Video Card","256M Mem","CPU/Mobo combo","Complete machine"))	#Returns: "Complete machine"
print test.bestItem((100,), (100,), (134,), ("Service, at cost",))	#Returns: ""
print test.bestItem((38,24), (37,23), (1000,643), ("Letter","Postcard"))	#Returns: ""
print test.bestItem((10,10), (11,12), (2,1), ("A","B"))	#Returns: "A"
