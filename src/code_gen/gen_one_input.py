# ------------------------------------------------------------------------
# graph generator for max-flow in python3
#
# command line arguments:
#   n = number of vertices
#   p = arc probability (0 <= p <= 1)
#   r = maximum range of capacity
#   s = random seed
#   f = output file name
#
#  example: python3 10 0.4 100 1234 data.in
#
#  It generates either:
#
#   1) a feasible graph, that is, there exists a path between vertice 1 and
#   vertice n, or
#
#   2) an infeasible graph, that is, there exists no path between vertice 1 and
#   vertice n. In this case, the output file contains only "-1"
#
#  Note that 2) may arise if the probability is too small
#
# ------------------------------------------------------------------------


import random
import sys
import os


class GraphGen:

    def __init__(self):
        try:
            os.mkdir('../generated_inputs')
        except OSError as error:
            print('INFO: path already exists')

    # ---------------------------
    # graph traversal
    # ---------------------------

    def __dfs(self, L, v, n, i):
        if i == n:
            return True
        if v[i] == False:
            v[i] = True
            for j in L[i]:
                if self.__dfs(L, v, n, j) == True:
                    return True
        return False

    # ----------------------------
    # check that a path exists
    # ----------------------------

    def __check(self, L, n):
        v = [False] * (n+1)
        return self.__dfs(L, v, n, 1)

    def gen_input(self, n, p, r, s, f):
        random.seed(s)

        M = []
        L = [[] for i in range(n+1)]
        m = 0

        for i in range(1, n):
            for j in range(i+1, n+1):
                if random.random() < p:
                    m = m + 1
                    M.append([i, j])
                    L[i].append(j)

        fout = open('../generated_inputs_VERTICES/' + f, "w")
        if self.__check(L, n) == True:
            fout.write(str(n) + " " + str(m) + "\n")
            for i in M:
                fout.write(str(i[0]) + " " + str(i[1]) + " ")
                fout.write(str(random.randint(1, r)) + "\n")
        else:
            fout.write("-1")
        fout.close()


# ---------------------------
#  main function
# --------------------------


def main():

    argv = sys.argv[1:]
    n = int(argv[0])            # number of vertices
    p = float(argv[1])          # arc probability
    r = int(argv[2])            # maximum range of capacity
    s = int(argv[3])            # random seed
    f = argv[4]

    GraphGen.gen_input(n, p, r, s, f)


if __name__ == "__main__":
    main()
