import os
import subprocess
from os.path import isfile


def checkDirectory(path):
    resultDirectoryExists = os.path.exists(path)

    if not resultDirectoryExists:
        os.makedirs(path)





def generateData(executableName, input_path):
    print("..\\algorithms\\" + executableName + ".exe")

    k = subprocess.run(
        [r"..\\algorithms\\" + executableName + ".exe", "100",  input_path],
        capture_output=True, text=True).stdout.split()


    print(k)

    results = [executableName, k[0], k[1]]
    storeResults(results, input_path)


def storeResults(results, input_path):
    f_in = open(input_path, "r")
    f_out = open("../results/results.csv", "a")

    vertices_edges = f_in.readline().strip().split(" ")

    # print(results)
    for item in results:
        f_out.write(f"{item};")
        # print(item)

    f_out.write(f"{vertices_edges[0]};{vertices_edges[1]}\n")

    f_in.close()
    f_out.close()


def main():
    checkDirectory('../results')

    dir = "../generated_inputs\\"
    all_files = os.listdir(dir)
    print(all_files)

    # print(all_files)
    for file in all_files:
        print(dir + file)
        generateData("EK", dir + file)
        generateData("Dinic", dir + file)
        generateData("MPM", dir + file)


if __name__ == "__main__":
    main()
