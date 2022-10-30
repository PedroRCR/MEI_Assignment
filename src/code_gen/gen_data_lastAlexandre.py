# import os
# import subprocess
# from os.path import isfile
# from multiprocessing import Process
# from statistics import mean
#
# NUM_SAMPLES = 3
#
#
# def checkDirectory(path):
#     resultDirectoryExists = os.path.exists(path)
#
#     if not resultDirectoryExists:
#         os.makedirs(path)
#
#
# def generateData(executableName, input_path, f_out):
#
#
#     k = subprocess.run([r".\..\algorithms\\" + executableName, "100",
#                         input_path], capture_output=True, text=True).stdout.split()
#     print(k)
#     results = [executableName, k[0],  k[1]]
#
#     times = []
#
#
#     for i in range(NUM_SAMPLES):
#         k = subprocess.run([r".\..\algorithms\\" + executableName, "1000",
#                             input_path], capture_output=True, text=True).stdout.split()
#         # print(k)
#         times.append(float(k[1]))
#
# #    print(k)
#     results = [executableName, k[0],  mean(times)]
#
#     storeResults(results, input_path, f_out)
#
#
# def storeResults(results, input_path):
#     print(input_path)
#     f_in = open(input_path, "r")
#     f_out = open("..\\results\\results.csv", "a")
#
#
# def storeResults(results, input_path, f_out):
#
#     f_in = open(input_path, "r")
#
#
#     vertices_edges = f_in.readline().strip().split(" ")
#
#     # print(results)
#     for item in results:
#         f_out.write(f"{item};")
#         # print(item)
#
#     f_out.write(f"{vertices_edges[0]};{vertices_edges[1]}\n")
#
#     f_in.close()
#
#
#
# def main():
#     checkDirectory('..\\results')
#
#
#     dir = "..\generated_inputs\\"
#
#     f_out = open("..\\results\\results.csv", "a")
#
#     dir = "..\generated_inputs\\"
#
#     all_files = os.listdir(dir)
#
#
#     # print(all_files)
#     procs = []
#     for file in all_files:
#
#         proc1 = Process(target=generateData, args=("EK", dir + file, f_out))
#         proc2 = Process(target=generateData, args=("Dinic", dir + file, f_out))
#         proc3 = Process(target=generateData, args=("MPM", dir + file, f_out))
#
#         procs.extend((proc1, proc2, proc3))
#
#     for proc in procs:
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
#     f_out.close()
#
#
# if __name__ == "__main__":
#     main()
