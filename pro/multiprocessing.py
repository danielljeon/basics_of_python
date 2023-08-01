from multiprocessing import Lock, Process, Value, Array, Pool, Manager
import os


# ---------- Single Inner Process Functions ----------


def __add_1_shared_array_and_lock(shared_array, lock):
    # lock.acquire()  # Lock to prevent a race condition (Or you can use with lock)
    # MANIPULATE SHARED VARIABLE HERE
    # lock.release()  # Lock release

    with lock:
        for index in range(len(shared_array)):
            shared_array[index] += 1


"""
def __add_1_shared_value_and_lock(shared_value, lock):
    with lock:
        shared_value.value += 1
"""


def __add_1_single_int(passed_int):
    passed_int += 1

    return passed_int


# ---------- Multiprocess Logic Functions ----------

def multiprocessing_with_shared_and_lock():
    lock = Lock()  # Create a lock

    process_list = []

    shared_number = Value("i", 0)  # 'd' = a double precision float | 'i' = a signed integer

    shared_array = Array("d", [0.0, 100.0, 200.0])  # 'd' = a double precision float | 'i' = a signed integer
    print(f"Shared Array at start: {shared_array[:]}")

    # pass the lock to the target function
    process_list.append(Process(target=__add_1_shared_array_and_lock, args=(shared_array, lock)))

    for process in process_list:
        process.start()  # Start all processes

    for process in process_list:
        process.join()  # Wait for all processes to finish

    print(f"Shared Array at end: {shared_array[:]}")


def multiprocessing_with_manager_with_manager_list_and_lock():
    # Why use Manager().list()? -> https://stackoverflow.com/questions/9436757/how-to-use-a-multiprocessing-manager

    lock = Lock()  # Create a lock

    process_list = []

    with Manager() as manager:
        manager_list = manager.list([0.0, 100.0, 200.0])

        print(f"Shared Manager().list() at start: {manager_list}")

        # pass the lock to the target function
        process_list.append(Process(target=__add_1_shared_array_and_lock, args=(manager_list, lock)))

        for process in process_list:
            process.start()  # Start all processes

        for process in process_list:
            process.join()  # Wait for all processes to finish

        print(f"Shared Manager().list() at end: {manager_list}")


def multiprocessing_with_pool():
    pool_size = os.cpu_count()

    passed_list = [0.0, 100.0, 200.0]

    print(f"Integer at start: {passed_list}")

    with Pool(processes=pool_size) as pool:
        # by default Pool allocates the maximum number of processors available
        # processors for this task --> os.cpu_count()

        results = list(pool.imap_unordered(__add_1_single_int, passed_list))
        # passed_list = pool.map(__add_1_single_int, passed_list)

    print(f"Integer at end: {results}")


if __name__ == "__main__":
    # multiprocessing_with_shared_and_lock()
    # multiprocessing_with_manager_with_manager_list_and_lock()
    # multiprocessing_with_pool()

    pass
