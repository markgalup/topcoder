class BacteriesColony(object):

    def performTheExperiment(self, colonies):
        colonies = list(colonies)
        colonies_final = ()
        cont = True

        while cont:

            colonies_check = colonies [:]
            for i in range(1, len(colonies)-1):
                if colonies_check[i] > colonies_check[i-1] and colonies_check[i] > colonies_check[i+1]:
                    colonies[i] -= 1

                elif colonies_check[i] < colonies_check[i-1] and colonies_check[i] < colonies_check[i+1]:
                    colonies[i] += 1
            if colonies_check == colonies[:]:
                cont = False


        for i in colonies:
            colonies_final += (i,)
        return colonies_final






print BacteriesColony().performTheExperiment((5, 3, 4, 6, 1))

# # Returns: {5, 4, 4, 4, 1 }

print BacteriesColony().performTheExperiment((1, 5, 4, 9))

# Returns: {1, 4, 5, 9 }

print BacteriesColony().performTheExperiment((78, 34, 3, 54, 44, 99))
# Returns: 78, 34, 34, 49, 49, 99

print BacteriesColony().performTheExperiment((24, 61, 79, 36, 16, 51, 63, 14, 53, 18, 47, 73, 79, 59, 24, 44, 62, 12, 4, 56, 32, 58, 54, 27, 21, 78, 29, 54, 20, 23, 41, 72, 99, 30, 77, 62, 96, 26, 40, 6, 41, 67, 62, 72, 57, 8, 85, 73, 64, 16))
# Returns: 24, 61, 61, 36, 36, 51, 51, 35, 35, 36, 47, 73, 73, 59, 44, 44, 44, 12, 12, 44, 44, 54, 54, 27, 27, 42, 42, 41, 23, 23, 41, 72, 72, 69, 69, 70, 70, 33, 33, 33, 41, 64, 65, 65, 57, 57, 73, 73, 64, 16
# print BacteriesColony().performTheExperiment
