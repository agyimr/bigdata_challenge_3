import time
import os
import multiprocessing
import kmeans

from multiprocessing import Manager

import image


def calculate_hashes(sublist, result_list):
    for filename in sublist:
        result_list.append((filename, image.process_image('./videos/' + filename)))


if __name__ == "__main__":
    start = time.time()
    manager = Manager()
    shared_list = manager.list()

    filename_list = os.listdir(os.getcwd() + '/videos')

    number_of_processes = 4
    processes = []
    input_array_step = len(filename_list) // number_of_processes

    for i in range(number_of_processes):
        sub_array = filename_list[i * input_array_step:(i + 1) * input_array_step]
        processes.append(multiprocessing.Process(target=calculate_hashes, args=(sub_array, shared_list)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
    
    print("Ready with hashing!")
    output = open("res.txt", "w")
    for item in kmeans.calculate_kmeans(shared_list):
        output.write(item[0] + " " + str(item[1]) + "\n")
    output.close()
    print("Ready with k-means!")
    print(time.time() - start)
