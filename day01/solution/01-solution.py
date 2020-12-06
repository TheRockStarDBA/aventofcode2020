#! /usr/local/bin/python3.9
"""find the two entries that sum to 2020 and then multiply those two numbers together
"""
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def two_sum(arr, target):
    """We are going to solve the adding of 2 numbers to get 2020 using
        a 2 pointer method over a sorted array
    arr = sorted array
    target = the target sum that you want .. for us it is 2020
    """
    left = 0
    right = len(arr) - 1
    if arr is None:
        return "array length is 0"
    while left < right:
        curr = arr[left] + arr[right]
        if curr < target:
            left += 1
        elif curr > target:
            right -= 1
        else:
            return [arr[left], arr[right]]
    return [-1, -1]


def read_file_to_sorted_array(input_file):
    file_number_array = []
    try:
        with open(input_file, "r") as reader:
            for line in reader:
                number = int(line)
                file_number_array.append(number)
        return sorted(file_number_array)
    except FileNotFoundError:
        print("file {} does not exist".format(input_file))


def main():
    file_number_array_sorted = read_file_to_sorted_array(filename)
    results = two_sum(file_number_array_sorted, target=3021)
    print(results)
    print(sum(results))
    print(results[0] * results[1])


if __name__ == "__main__":
    main()