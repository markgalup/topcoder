class StreetParking(object):

    def freeParks(self, street):
        spots = 0
        street_list = list(street)

        street_list[len(street_list):] = ".", "."
        for i in range(2):
            street_list.insert(0, ".")
        x_list = street_list[:]

        for i in range(len(street_list)):
            if street_list[i] == "B":
                for j in range((i-2), (i+1)):
                    x_list[j] = "X"
            elif street_list[i] == "S":
                for j in range((i-1), (i+2)):
                    x_list[j] = "X"
            elif street_list[i] == "D":
                x_list[i] = "X"

        for i in x_list:
            if i == "-":
                spots += 1
        return spots


print StreetParking().freeParks("---B--S-D--S--")
# Returns: 4
print StreetParking().freeParks("DDBDDBDDBDD")
# Returns: 0
print StreetParking().freeParks("--S--S--S--S--")
# Returns: 2
print StreetParking().freeParks("SSD-B---BD-DDSB-----S-S--------S-B----BSB-S--B-S-D")
# Returns: 14
print StreetParking().freeParks("-S---------DDDB---BB----SSD---D-B---S-B-----DD---S")
# Returns: 24
print StreetParking().freeParks("------DD--S--D--S-S-DSS---B--D--S---B----S----DD-")
# Returns: 19
print StreetParking().freeParks("B")
# Returns: 0