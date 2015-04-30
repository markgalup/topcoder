class TheGridDivTwo(object):

    def find(self, x, y, k):
        x_moves = 0
        y_moves = 0
        o_x = 0
        o_y = 0



        for i in range(1, (k+1)):
            for m in range(len(x)):
                for n in range(len(y)):
                    if x[m] != o_x + k and y[n] == o_y + k:
                        x_moves += 1
                    elif x[m] == o_x + k and y[n] != o_y + k








print TheGridDivTwo().find((1,1,1,1), (-2,-1,0,1), 4)
# Returns: 2

print TheGridDivTwo().find((-1, 0, 0, 1), (0, -1, 1, 0), 9)
# Returns: 0

print TheGridDivTwo().find((), (), 1000)
# Returns: 1000

print TheGridDivTwo().find((1,0,0,-1,-1,-2,-2,-3,-3,-4,-4), (0,-1,1,-2,2,-3,3,-4,4,-5,5), 47)
# Returns: 31