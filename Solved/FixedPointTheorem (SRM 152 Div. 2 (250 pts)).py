from decimal import *
getcontext().prec = 17


class FixedPointTheorem(object):

    def cycleRange(self, R):
        x_max = 0
        x_min = 0
        x_values = []
        x = .25
        for i in range(200000):
            x = (R * x * (1 - x))
        for i in range(1000):
            x = (R * x * (1 - x))
            x_values.append(Decimal(x))
        x_range = max(x_values) - min(x_values)
        return x_range

test = FixedPointTheorem()
print test.cycleRange(0.1)  # Returns: 0.0
print test.cycleRange(3.05)  # Returns:       0.14754098360655865
print test.cycleRange(3.4499)  # Returns:   0.4175631735867292
print test.cycleRange(3.55)  # Returns:       0.5325704489850351
print test.cycleRange(3.565)  # Returns:   0.5454276003030636
print test.cycleRange(3.5689)  # Returns:   0.5489996297493569
print test.cycleRange(3.00005)  # Returns:   0.004713996108955176
