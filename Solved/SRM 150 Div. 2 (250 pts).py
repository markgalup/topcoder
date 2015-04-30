class WidgetRepairs(object):

    def days(self, arrivals, numPerDay):

        days = 0
        overflow = 0

        for i in arrivals:
            if overflow == 0:
                if i == 0:
                    pass
                elif i <= numPerDay and i > 0:
                    days += 1
                elif i > numPerDay:
                    days += 1
                    overflow += i - numPerDay
            elif overflow > 0:
                if i + overflow <= numPerDay:
                    days += 1
                    overflow = 0
                elif i + overflow > numPerDay:
                    days += 1
                    overflow = (i + overflow) - numPerDay
        if overflow > 0:
            days += overflow / numPerDay
            if overflow % numPerDay != 0:
                days += 1

        return days


test = WidgetRepairs()
# print test.days((10, 0), 8)
print test.days((10, 0, 0, 4, 20), 8)  # Returns: 6
print test.days((0, 0, 0), 10)  # Returns: 0
print test.days((100, 100), 10)  # Returns: 20
print test.days((27, 0, 0, 0, 0, 9), 9)  # Returns: 4
print test.days((6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6), 3)  # Returns: 15
