class TaroJiroDividing(object):
    def getNumber(self, A, B):
        count = 0
        low = min(A, B)

        if max(A, B)%min(A, B) != 0:
            return count
        elif low % 2 != 0:
            
            return count
        else:
            count += 1
            while low % 2 == 0:
                count += 1
                low /= 2
        return count


print TaroJiroDividing().getNumber(8, 4)
# 3
print TaroJiroDividing().getNumber(4, 7)
# 0
print TaroJiroDividing().getNumber(12, 12)
# 3
print TaroJiroDividing().getNumber(24, 96)
# 4
print TaroJiroDividing().getNumber(1000000000, 999999999)
# 0
print TaroJiroDividing().getNumber(1, 12)
# 0
print TaroJiroDividing().getNumber(9, 27)
# 0
print TaroJiroDividing().getNumber(6952, 869)
# 1