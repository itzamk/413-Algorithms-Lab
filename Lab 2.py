'''
Andrew Kozempel
CMPSC 413
Lab 2
Fall 2023
'''

import time

# function to measure time of functions
# *args used to pass variable number of arguments
def measure_time(function, *args):

    start = time.time_ns() # start time
    function(*args) # perform specified function
    
    return (time.time_ns() - start) # return total time

# Best: O(1)
# Worst: O(n)
def linear_search(lst, target):

    # iterate through list
    for i in range(len(lst)):

        # if element is target, return index
        if lst[i] == target:
            return i
        
# Best: O(1)
# Worst: O(logn)
def binary_search(lst, target):

    # assign left and right indices
    left = 0
    right = len(lst) - 1
    
    # while loop until target is found
    while left <= right:

        # calculate mid index
        mid = (left + right) // 2

        # if mid index is target, return index
        if lst[mid] == target:
            return mid
        
        # search right half
        elif lst[mid] < target:
            left = mid + 1

        # search left half
        else:
            right = mid - 1

# Best: O(n)
# Worst: O(n^2)
def insertion_sort(lst):

    # loop through list starting at second
    for i in range(1, len(lst)):

        curr = lst[i] # store current element
        j = i - 1 # element before curr

        # while there are elements to the left of curr
        # and curr is less than previous element
        while j >= 0 and curr < lst[j]:

            lst[j + 1] = lst[j] # move element to the right (copy?)
            j -= 1 # move to previous element

        # insert current element in correct spot
        lst[j + 1] = curr

# Best: O(n^2)
# Worst: O(n^2)
def selection_sort(lst):

    # iterate through list
    for i in range(len(lst)):

        # initalize min index
        min_idx = i

        # iterate through unsorted elements
        for j in range(i+1, len(lst)):

            # update min index if smaller elements is found
            if lst[j] < lst[min_idx]:
                min_idx = j

        # swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

# Best: O(n)
# Worst: O(n^2)
def bubble_sort(lst):

    # length of list
    n = len(lst)

    # iterate through list
    for i in range(n):

        # iterate through unsorted (ignore the last i elements)
        for j in range(0, n-i-1):

            # swap if out of order
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def read_student_data(filename):
    # store student data
    students = []

    # open the file in read mode
    with open(filename, 'r') as file:
        # read first line to get the headers/column names
        headers = file.readline().strip().split(',')
        
        # loop through each line in the file
        for line in file:
            # split the line into individual data items
            data = line.strip().split(',')
            
            # create a dictionary for each student using a dictionary comprehension
            student = {}
            
            # iterate through items in line
            for i in range(len(headers)):
                student[headers[i]] = data[i]
            
            # append the student dictionary to the students list
            students.append(student)
    
    # return the list of student dictionaries
    return students

############################################################
#  PART 2 - STUDENT SORTING
############################################################

students_data = read_student_data('students.txt')


search_key = 'Student ID'
search_value = 1002

# Linear Search
print(f'Linear search time: {measure_time(linear_search, students_data, search_value): .6f} nanoseconds')

# Binary Search
print(f'Binary search time: {measure_time(binary_search, students_data, search_value): .6f} nanoseconds')

# Selection Sort
print(f'Selection sort time: {measure_time(selection_sort, students_data.copy(), "Student ID"):.6f} seconds')

# Insertion Sort
print(f'Insertion sort time: {measure_time(insertion_sort, students_data.copy(), "Student ID"):.6f} seconds')

# Bubble Sort
print(f'Bubble sort time: {measure_time(bubble_sort, students_data.copy(), "Student ID"):.6f} seconds')
