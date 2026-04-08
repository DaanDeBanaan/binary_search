#--------imports--------#
"""time is used to time our performance, numpy for arrays and random generation"""
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
    """performs a simple binary search, returns index"""
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
    binary_search(create_array(10, 10), 5) #compiles the functions
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

    start = perf_counter()
    a = create_array(element_count, upper_bound) #returns the array and its creation time
    end = perf_counter()
    array_time = end - start

    print(f"Creating array took {array_time} seconds")
    rng = np.random.default_rng()
    random_element = a[rng.integers(a.size)] #it's overkill to use numpy, but it's one less import
    start = perf_counter()
    search_data = binary_search(a, random_element)
    end = perf_counter()
    search_time = end - start
    if search_data[0] is None:
        print(f"The element {random_element} is not in the list.")
    else:
        print(f"The element {random_element} is at index {search_data[0]}")
    print(f"It took {search_time} seconds and {search_data[1]} passes.")
    print(f"Searching was {int(array_time // search_time)} times faster than creating the array.")
