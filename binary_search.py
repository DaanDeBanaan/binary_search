#--------imports--------#
"""time is used to time our performance, numpy for arrays and random generation, numba for speed"""
from time import perf_counter
import numpy as np
from numba import njit


#--------functions--------#
def create_array(element_count, upper_bound):
    """creates a random array"""
    print("Creating array...")
    if element_count == upper_bound:
        a = np.arange(element_count)
    else:
        a = np.sort(np.random.choice(upper_bound, element_count, replace=False))
    print("Finished array!")
    return a

@njit
def binary_search(a, search):
    """performs a simple binary search, returns index and amount of runs"""
    low = 0
    high = a.size - 1
    count = 0
    while True:
        count += 1
        if low > high:
            print("Element not found in list!")
            return None, count
        mid = (low+high) // 2
        if a[mid] < search:
            low = mid + 1
        elif a[mid] > search:
            high = mid - 1
        else:
            return mid, count

#--------program--------#
if __name__ == "__main__": #just good practice
    binary_search(create_array(5, 5), 3) #compiles the functions
    while True: #simple loop to get the user input for the array length
        try:
            while True:
                element_count = int(input("How many elements (strictly positive) do you want in your list?: "))
                if element_count > 0:
                    break
                else:
                    print("Amount of elements can't be zero or negative!")
            break
        except ValueError:
            print("Input an integer!")

    while True: #same as last loop, but for the biggest possible element
        try:
            while True:
                print("What is the upper range for the element size?")
                print("Making the upper range equal to the amount of elements creates the array quicker.")
                upper_bound = int(input("Input a number >= the amount of elements: "))
                if upper_bound >= element_count:
                    break
                else:
                    print("Number was not greater than or equal to the amount of elements!")
            break
        except ValueError:
            print("Input an integer!")

    while True: #you get how it works by now
        try:
            while True:
                run_count = int(input("Input the amount of times the algorithm needs to be run: "))
                if run_count > 0:
                    break
                else:
                    print("Number was not greater than 0!")
            break
        except ValueError:
            print("Input an integer!")

    a = create_array(element_count, upper_bound) #creates the array
    rng = np.random.default_rng()
    random_element = a[rng.integers(a.size)] #it's overkill to use numpy, but it's one less import

    search_time = 0
    for i in range(run_count): #couldn't use timeit because it didn't work
        start = perf_counter()
        search_data = binary_search(a, random_element)
        end = perf_counter()
        search_time += end - start

    if search_data[0] is None:
        print(f"The element {random_element} is not in the list.")
    else:
        print(f"The element {random_element} is at index {search_data[0]}")
    print(f"It took {search_time} seconds to run the program {run_count} times ({search_time/run_count} seconds per run).")
    print(f"It took {search_data[1]} passes to find the element {random_element}.")
