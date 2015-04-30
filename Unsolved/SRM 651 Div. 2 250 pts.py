class RobotOnMoonEasy(object):
    def isSafeCommand(self, board, S):
        pos_x = 0
        pos_y = 0
        board_x = len(board) + 1
        board_y = len(board[0]) + 1
        #board = list(board)
        #print len(board)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if  board[x][y] == 'S':
                    pos_x = x
                    pos_y = y
        print pos_x, pos_y, board_x, board_y

        for each in S:
            if each == 'U':

                if board[pos_x-1][pos_y] != '#' and pos_x-1 <= board_x or pos_x-1 >= 0:
                    pos_x -= 1
                else:
                    pass
            elif each == 'D':

                if board[pos_x+1][pos_y] != '#' and pos_x+1 <= board_x or pos_x+1 >= 0:
                    pos_x += 1
                else:
                    pass
            elif each == 'L':

                if board[pos_x][pos_y-1] != '#' and pos_y-1 <= board_y or pos_y-1 >= 0:
                    pos_y -= 1
                else:
                    pass
            elif each == 'R':

                if board[pos_x][pos_y+1] != '#' and pos_y+1 <= board_y or pos_y+1 >= 0:
                    pos_y += 1
                else:
                    pass
        if pos_x > board_x or pos_y > board_y:
            return "Dead"
        else:
            return "Alive"



print RobotOnMoonEasy().isSafeCommand((".....",
 ".###.",
 "..S#.",
 "...#."), "URURURURUR")
# "Alive"
 
print RobotOnMoonEasy().isSafeCommand((".....",
 ".###.",
 "..S..",
 "...#."), "URURURURUR")
# #  #"Dead"
 
print RobotOnMoonEasy().isSafeCommand((".....",
 ".###.",
 "..S..",
 "...#."), "URURU")
# #  # "Alive"
 
#  