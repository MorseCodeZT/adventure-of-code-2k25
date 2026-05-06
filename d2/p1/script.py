with open("input.txt", "r") as f:
    input_ = f.readlines()[0]

# input_ = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#
# test = "11-22,95-115"
# test_split = input_.split(",")
# # test_split = input_.split("-")

input_split = input_.split(",")

invalid_id = []

for range_num in input_split:
    range_num_split = range_num.split("-")

    for x in range(int(range_num_split[0]), int(range_num_split[1])+1):
        number = str(x)
        if len(number)%2 == 0:
            first_part = number[0:len(number)//2]
            second_part = number[len(number)//2:len(number)]

            print(first_part, second_part)

            if first_part == second_part:
                invalid_id.append(x)

# print(invalid_id)

sum_ = 0
for x in invalid_id:
    sum_ += int(x)

print(sum_)

