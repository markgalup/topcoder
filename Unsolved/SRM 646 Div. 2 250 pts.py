class TheConsecutiveIntegersDivTwo(object):

    def find(self, numbers, k):
        numbers_copy = sorted(numbers)

        min_difference = 20000000

        if k == 1:
            return 0
        else:
            for i in range(len(numbers_copy) - 1):
                combos = len(numbers_copy)-i
                for j in range(1, combos):
                    difference = 0
                    difference += abs(numbers_copy[i] - numbers_copy[i+j])
                    if difference < min_difference:
                        min_difference = difference
        return min_difference - 1





print TheConsecutiveIntegersDivTwo().find((4, 47, 7), 2)
# Returns: 2

print TheConsecutiveIntegersDivTwo().find((1, 100), 1)
# Returns: 0

print TheConsecutiveIntegersDivTwo().find((-96, -53, 82, -24, 6, -75), 2)
# Returns: 20

print TheConsecutiveIntegersDivTwo().find((64, -31, -56), 2)
# Returns: 24
