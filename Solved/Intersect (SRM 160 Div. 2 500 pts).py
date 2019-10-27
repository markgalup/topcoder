class Intersect(object):

    def area(self, x, y):
        # top = 0
        # bott = 0
        # left = 0
        # right = 0

        # for i in range(1):
        #     if x[i] < x[i + 1]:
        #         left = x[i]
        #     else:
        #         left = x[i + 1]
        # for i in range(1):
        #     if x[i] > x[i + 1]:
        #         right = x[i]
        #     else:
        #         right = x[i + 1]
        # for i in range(1):
        #     if y[i] > y[i + 1]:
        #         top = y[i]
        #     else:
        #         top = y[i + 1]
        # for i in range(1):
        #     if y[i] < y[i + 1]:
        #         bott = y[i]
        #     else:
        #         bott = y[i + 1]

        # print top, bott, left, right

        top = 11111
        bott = -11111
        left = -11111
        right = 11111

        for i in range(0, len(x), 2):
            if x[i] < x[i + 1]:
                if x[i] < right:
                    if x[i] > left:
                        left = x[i]
                else:
                    return 0
            else:
                if x[i + 1] < right:
                    if x[i + 1] > left:
                        left = x[i + 1]
                else:
                    return 0

        for i in range(0, len(x), 2):
            if x[i] > x[i + 1]:
                if x[i] > left:
                    if x[i] < right:
                        right = x[i]
                else:
                    return 0
            else:
                if x[i + 1] > left:
                    if x[i + 1] < right:
                        right = x[i + 1]
                else:
                    return 0

        for i in range(0, len(y), 2):
            if y[i] < y[i + 1]:
                if y[i] < top:
                    if y[i] > bott:
                        bott = y[i]
                else:
                    return 0
            else:
                if y[i + 1] < top:
                    if y[i + 1] > bott:
                        bott = y[i + 1]
                else:
                    return 0

        for i in range(0, len(y), 2):
            if y[i] > y[i + 1]:
                if y[i] > bott:
                    if y[i] < top:
                        top = y[i]
                else:
                    return 0
            else:
                if y[i + 1] > bott:
                    if y[i + 1] < top:
                        top = y[i + 1]
                else:
                    return 0

        # print left, bott, right, top

        return (top-bott) * (right-left)

print Intersect().area((0,2,3,-4), (17,1000,18,6))
# Returns: 2

print Intersect().area((10000,-10000), (-10000,10000))
# Returns: 400000000

print Intersect().area((3,8,6,12,10,15), (7,17,7,17,7,17))
# Returns: 0

print Intersect().area((0,0,0,0,0,0,0,0), (5,5,5,5,5,5,5,5))
# Returns: 0

print Intersect().area((2,100,5,32,1000,-20,47,12), (29,-1000,-800,-200,-900,300,-600,-650))
# Returns: 1000

print Intersect().area((1,7,12,3,16,8,3,12), (-90,-60,-70,3,-60,-90,-80,-100))
# Returns: 0
