class Substitute(object):

    def getValue(self, key, code):
        number = []

        for x in code:
            for i, j in enumerate(key):
                if j == x:
                    if i == 9:
                        number.append("0")
                    else:
                        number.append(str(i + 1))

        final_number = int(''.join(number))
        return final_number





print Substitute().getValue("TRADINGFEW", "LGXWEV")
# Returns: 709
print Substitute().getValue("ABCDEFGHIJ", "XJ")
# Returns: 0
print Substitute().getValue("CRYSTALBUM", "MMA")
# Returns: 6