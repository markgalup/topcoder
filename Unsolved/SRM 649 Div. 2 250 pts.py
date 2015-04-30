class DecipherabilityEasy(object):
    def check(self, s, t):
        #s += " "
        for x in range(len(s)):
            print s[:x] + s[x+1:]
            if s[:x] + s[x+1:] == t:
                return "Possible"
                
        return "Impossible"

print DecipherabilityEasy().check("sunmke", "snuke" )