class Target(object):

    def draw(self, n):
        x = n
        drawing_tup = ()
        rows = 0
        l_bounds = '# '
        r_bounds = ' #'
        bound_num = 0

        while rows < n:

            if rows < n/2:
                drawing_tup += ((l_bounds*bound_num) + ('#' * x) + (r_bounds*bound_num),)
                drawing_tup += ((l_bounds*bound_num) + '#' + (' ' * (x-2)) + '#' + (r_bounds*bound_num),)
                x -= 4
                rows += 2
                bound_num += 1

            elif rows > n/2:
                drawing_tup += ((l_bounds*bound_num) + '#' + (' ' * (x-2)) + '#' + (r_bounds*bound_num),)
                drawing_tup += ((l_bounds*bound_num) + ('#' * x) + (r_bounds*bound_num),)
                x += 4
                rows += 2
                bound_num -= 1

            else:
                drawing_tup += ((l_bounds*bound_num) + ('#' * x) + (r_bounds*bound_num),)
                rows += 1
                x += 4
                bound_num -=1

        return drawing_tup

print Target().draw(5)
# Returns: ("#####", 
#           "#   #", 
#           "# # #", 
#           "#   #", 
#           "#####")

print Target().draw(9)
#Returns: 
# ("#########",
#  "#       #",
#  "# ##### #",
#  "# #   # #",
#  "# # # # #",
#  "# #   # #",
#  "# ##### #",
#  "#       #",
#  "#########" )

print Target().draw(13)
# Returns: 
# ("#############",
#  "#           #",
#  "# ######### #",
#  "# #       # #",
#  "# # ##### # #",
#  "# # #   # # #",
#  "# # # # # # #",
#  "# # #   # # #",
#  "# # ##### # #",
#  "# #       # #",
#  "# ######### #",
#  "#           #",
#  "#############" )

print Target().draw(17)
# Returns: 
# ("#################",
#  "#               #",
#  "# ############# #",
#  "# #           # #",
#  "# # ######### # #",
#  "# # #       # # #",
#  "# # # ##### # # #",
#  "# # # #   # # # #",
#  "# # # # # # # # #",
#  "# # # #   # # # #",
#  "# # # ##### # # #",
#  "# # #       # # #",
#  "# # ######### # #",
#  "# #           # #",
#  "# ############# #",
#  "#               #",
#  "#################" )
