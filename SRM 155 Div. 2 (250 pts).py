class Quipu(object):

    def readKnots(self, knots):
        knots = knots.split("-")
        knots.pop(0)
        knots.pop(-1)

        knot_count = []
        for i in knots:
            knot_count.append(str(len(i)))

        return ''.join(knot_count)


print Quipu().readKnots("-XX-XXXX-XXX-")  # Returns: 243
print Quipu().readKnots("-XX--XXXX---XXX-")  # Returns: 204003
print Quipu().readKnots("-X-")  # Returns: 1
print Quipu().readKnots("-X-------")  # Returns: 1000000
print Quipu().readKnots("-XXXXXXXXX--XXXXXXXXX-XXXXXXXXX-XXXXXXX-XXXXXXXXX-")
# Returns: 909979
