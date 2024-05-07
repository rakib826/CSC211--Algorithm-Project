# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A5xEpe3lqGPoxxkogfeR7u7D0D02JMFp
"""

import random

def counting_sort(arr):
    """
    Perform counting sort algorithm to sort student data based on marks.

    Args:
        arr (list of tuples): List containing tuples of student name and their corresponding marks.

    Returns:
        list of tuples: Sorted student data based on marks.
    """
    # Initialize count array to store the count of each grade
    count = [0] * 101  # Assuming marks range from 0 to 100

    # Count the occurrences of each grade
    for _, grade in arr:
        count[grade] += 1

    # Modify count array to store the position of each grade in the sorted array
    for i in range(1, 101):
        count[i] += count[i - 1]

    # Create a new array to store the sorted result
    sorted_arr = [None] * len(arr)

    # Build the sorted array
    for name, grade in reversed(arr):
        sorted_arr[count[grade] - 1] = (name, grade)
        count[grade] -= 1

    return sorted_arr

def generate_test_case(num_students, marks_range):
    """
    Generate a test case for the counting sort program.

    Args:
        num_students (int): Number of students in the test case.
        marks_range (tuple): Range of marks, e.g., (0, 100) for marks between 0 and 100 (inclusive).

    Returns:
        list of tuples: Test case containing student names and their corresponding marks.
    """
    min_mark, max_mark = marks_range
    test_case = []

    # Generate student names and marks randomly
    for i in range(num_students):
        name = f"Student_{i + 1}"
        # Generate random marks until it's different from student number
        marks = random.randint(min_mark, max_mark)
        while marks == i + 1:
            marks = random.randint(min_mark, max_mark)
        test_case.append((name, marks))

    return test_case

def main():
    # Test Case 1 (Small dataset)
    test_case_1 = generate_test_case(5
                                     , (0, 100))
    print("\nTest Case 1 (Small dataset):")
    sorted_student_data = counting_sort(test_case_1)
    for name, grade in sorted(sorted_student_data, key=lambda x: x[1]):
        print(f"Name: {name}, Marks: {grade}")

    # Test Case 2 (Large dataset)
    test_case_2 = generate_test_case(1000, (0, 100))
    print("\nTest Case 2 (Large dataset):")
    sorted_student_data = counting_sort(test_case_2)
    # Print only the first 50 elements to avoid printing a large amount of data
    for name, grade in sorted(sorted_student_data, key=lambda x: x[1])[:10]:
        print(f"Name: {name}, Marks: {grade}")
    print("... (remaining data omitted)")

    # Test Case 3 (All students have same mark)
    test_case_3 = [("Student_" + str(i), 85) for i in range(1, 5)]
    print("\nTest Case 3 (All students have same mark):")
    sorted_student_data = counting_sort(test_case_3)
    for name, grade in sorted(sorted_student_data, key=lambda x: (x[1], test_case_3.index((x[0], x[1])))):
        print(f"Name: {name}, Marks: {grade}")

    # Test Case 4 (Marks are already sorted)
    test_case_4 = [("Student_" + str(i), i) for i in range(10)]
    print("\nTest Case 4 (Marks are already sorted):")
    sorted_student_data = counting_sort(test_case_4)
    for name, grade in sorted(sorted_student_data, key=lambda x: x[1]):
        print(f"Name: {name}, Marks: {grade}")

if __name__ == "__main__":
    main()