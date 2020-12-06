import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def three_sum(arr, target):
    """We are going to solve the adding 3 numbers to get 2020 using
        an outer for loop and a 2 pointer method over a sorted array
    arr = sorted array
    target = the target sum that you want .. for us it is 2020
    """
    # get the length of input list: arr
    length = len(arr)

    # sort input numbers, to keep the increasing order
    arr.sort()

    # container for 3 sum answer storage
    triplet_answer = []

    # length - 2 is for the valid index i, left ,right within boundary
    # i = index for the first element such that 3 sum = arr[i] + arr[left] + arr[right] = target
    for i in range(0, length - 2):

        # skip the repetition of the same element (the limitation of problem description)
        if i > 0 and (arr[i - 1] == arr[i]):
            pass
            continue

        # left :   index for the second element such that 3 sum = arr[i] + arr[left] + arr[right] = target
        #       start from smallest value after index i

        # right : index for the third  element such that 3 sum = arr[i] + arr[left] + arr[right] = target
        #       start from largest value after index i
        left, right = i + 1, length - 1

        # inner loop to iterate index left, right
        while left < right:

            three_sum = arr[i] + arr[left] + arr[right]

            # check index i, left , right meets the sum value = target or not
            if three_sum == target:

                # get one triplet that satisfy the requirement, append to triplet_answer
                triplet_answer.append([arr[i], arr[left], arr[right]])

                # update index left, right for next iteration
                left += 1
                right -= 1

                # skip the repetition of the same element
                while left < right and (arr[left] == arr[left - 1]):
                    left += 1

                # skip the repetition of the same element
                while left < right and (arr[right] == arr[right + 1]):
                    right -= 1

            elif three_sum < target:
                # sum value is too small, make the second element larger on next iteration
                # update index left
                left += 1

            else:
                # sum value is too big, make the third element smaller on next iteration
                # update index right
                right -= 1

    # return the container for 3 sum triplet
    return triplet_answer


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
    results = three_sum(file_number_array_sorted, target=2020)
    print(results)
    print(sum(results[0]))
    result = 1
    for x in results[0]:
        result = result * x
    print(result)


if __name__ == "__main__":
    main()