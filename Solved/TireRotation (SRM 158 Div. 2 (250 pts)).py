class TireRotation(object):

    def getCycle(self, initial, current):

        if initial == current:
            return 1
        elif \
        current[0] == initial[3] \
        and current[1] == initial[2] \
        and current[2] == initial[0] \
        and current[3] == initial[1]:
            return 2
        elif \
        current[0] == initial[1] \
        and current[1] == initial[0] \
        and current[2] == initial[3] \
        and current[3] == initial[2]:
            return 3
        elif \
        current[0] == initial[2] \
        and current[1] == initial[3] \
        and current[2] == initial[1] \
        and current[3] == initial[0]:
            return 4
        else:
            return -1







print TireRotation().getCycle("ABCD", "ABCD")
# Returns: 1
print TireRotation().getCycle("ABCD", "DCAB")
# Returns: 2

# The initial locations of the tires are:

# A B
# C D

# After one rotation, the locations of the tires are:

# D C
# A B

print TireRotation().getCycle("ABCD", "CDBA")
# Returns: 4

# Continuing the rotation, we get the following for phase 3:

# B A
# D C

# And finally, on phase 4:

# C D
# B A


print TireRotation().getCycle("ABCD", "ABDC")
# Returns: -1
print TireRotation().getCycle("ZAXN", "XNAZ")
# Returns: 4
