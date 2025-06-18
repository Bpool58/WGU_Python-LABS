user_input = input('Enter numbers: ')
tokens = user_input.split()
nums = []
for token in tokens:
    nums.append(int(token))
print()

for pos, val in enumerate(nums):
    print(f'{pos}: {val}')


for pos in range(len(nums)):
    if nums[pos] < 0:
        nums[pos] = 0
print(nums)

for num in nums:
    print(num, end = ' ')

# user_input = input('Enter numbers: ')
#
# tokens = user_input.split()
#
# # Convert strings to integers
# nums = []
# for token in tokens:
#     nums.append(int(token))
#
# # Print each position and number
# print()
# for pos, val in enumerate(nums):
#     print(f'{pos}: {val}')
#
# # Change negative values to 0
# for pos in range(len(nums)):
#     if nums[pos] < 0:
#         nums[pos] = 0
#
# # Print new numbers
# print('New numbers: ')
# for num in nums:
#     print(num, end=' ')