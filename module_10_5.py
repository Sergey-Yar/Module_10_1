import time
import multiprocessing

start = time.time()
def  read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
for name in filenames:
    read_info(name)

# Многопроцессный вызов
# if __name__ == '__main__':
#     with multiprocessing.Pool(4) as pool:
#         pool.map(read_info, filenames)

fin = time.time()
print(fin-start)