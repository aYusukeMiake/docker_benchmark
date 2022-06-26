# check_speed_test.py
import numpy  # pip install numpyで入れてください
import os
import tqdm  # pip install tqdmで入れてください
import time

start_time = time.time()

print("\n")
for i in tqdm.tqdm(range(2000)):
    with open('./test.bin', "wb") as file:
        file.write(numpy.random.bytes(5000))
    os.remove('./test.bin')

print("time: {0}\n".format(time.time() - start_time))
