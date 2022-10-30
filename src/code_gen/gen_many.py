from gen_one_input import GraphGen
import sys
import numpy as np

SEED: int = 209184012

MAX_VERTICES: int = 2000
MIN_VERTICES: int = 100

MAX_PROB_EDGES: float = 0.9
MIN_PROB_EDGES: float = 0.1

MAX_WEIGHT_EDGES: int = 100
MIN_WEIGHT_EDGES: int = 10

NUM_FILES_PER_EXP: int = 5

def main():

    sys.setrecursionlimit(MAX_VERTICES)

    vertices: tuple(int) = np.arange(MIN_VERTICES, MAX_VERTICES,
                                     (MAX_VERTICES - MIN_VERTICES) / NUM_FILES_PER_EXP, dtype=int)
    edges: tuple(float) = np.arange(MIN_PROB_EDGES, MAX_PROB_EDGES,
                                     (MAX_PROB_EDGES - MIN_PROB_EDGES) / NUM_FILES_PER_EXP, dtype=float)
    weights: tuple(int) = np.arange(MIN_WEIGHT_EDGES, MAX_WEIGHT_EDGES,
                                     (MAX_WEIGHT_EDGES - MIN_WEIGHT_EDGES) / NUM_FILES_PER_EXP, dtype=int)

    print(vertices.size,vertices, edges, weights)

    generator = GraphGen()
    file_num: int = 0
    for vertice in vertices:
        for edge in edges:
            for weight in weights:

                print(vertice, edge, weight)
                generator.gen_input(vertice, edge, weight, SEED, f'input{file_num}.txt')
                file_num += 1


if __name__ == "__main__":
    main()