import os
from collections import Counter

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")

file_input = []
with open(filename, "r") as reader:
    for line in reader:
        file_input.append([str(n) for n in line.strip().split(" ")])

part1 = 0
part2 = 0

for pair in file_input:
    try:
        x, y, z = pair[0], pair[1], pair[2]
        min_max = x.strip().split("-")
        min_left = int(min_max[0])
        min_right = int(min_max[1])
        # here we just count the occurrences of a given letter in the password
        count = Counter(z)
        # print(min_left, min_right, "count of "+y.strip(':')+" "+str(count[y.strip(':')]))

        if min_left <= count[y.strip(":")] <= min_right:
            part1 += 1

        # print(min_left, min_right, y, z)
        # here we use XOR to see if we can satisfy the criteria for part 2
        """Each policy actually describes two positions in the password, where 1 means the first character, 
            2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
            Exactly one of these positions must contain the given letter. 
            Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
        '"""
        if (z[min_left - 1] == y.strip(":")) ^ (z[min_right - 1] == y.strip(":")):
            part2 += 1

    except IndexError:
        print("Line in the file does not have good entry")

print(
    "There are " + str(part1) + " passwords that are valid according to their policies"
)
print(part2)
