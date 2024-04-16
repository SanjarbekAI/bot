nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


nums = iter(nums)
while True:
    try:
        print(next(nums))
    except StopIteration:
        break

# for num in nums:
#     print(num)


def num_generator():
    num = 1
    while True:
        yield num
        num += 2


for i in num_generator():
    print(i)
