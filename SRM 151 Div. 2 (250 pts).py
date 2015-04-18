class PrefixCode(object):

    def isOne(self, words):
        if len(words) == 1:
            return "Yes"
        elif len(words) > 1:
            for i in words:
                for x in words:
                    if x.startswith(i) and x != i:
                        return "No, %d" % words.index(i)
            else:
                return "Yes"

test = PrefixCode()
print test.isOne(("trivial",))
print test.isOne(("10001", "011", "100", "001", "10"))
print test.isOne(("no", "nosy", "neighbors", "needed"))
print test.isOne(("1010", "11", "100", "0", "1011"))
print test.isOne(("No", "not"))
