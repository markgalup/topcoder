from fractions import gcd

class LCMRange(object):
    def lcm(self, first, last):
        def lcm_eq(a, b):
            return a * b // gcd(a, b)

        def lcmm(*args):
            return reduce(lcm_eq, args)

        return lcmm(*range(first, last+1))


print LCMRange().lcm(1, 5)
# 60
print LCMRange().lcm(4, 5)
# 20
print LCMRange().lcm(1, 12)
#27720
