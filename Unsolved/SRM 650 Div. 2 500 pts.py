class TaroFillingAStringDiv2(object):
    def getNumber(self, S):
        uglies = 0
        slist = list(S)
        slist.insert(0, ".") 
        slist.append(".")
        

        for x in range(len(slist)):
            if slist[x] == "?":
                if slist[x-1] == "A" or slist[x+1] == "A":
                    slist[x] = "B"
                else:
                    slist[x] = "A"
        
        for x in range(1, len(S)+1):
            if slist[x-1] == slist[x]:
                uglies += 1
        return uglies

print TaroFillingAStringDiv2().getNumber("A??B???AAB?A???A")
print TaroFillingAStringDiv2().getNumber("ABAA")