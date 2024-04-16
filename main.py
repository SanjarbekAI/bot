# nums = [12,34,5,3,2,423,2,23,44]
#
# nums = iter(nums)
# odd_numbers = []
# try:
#     while True:
#         this_num = next(nums)
#         if this_num%2==1:
#             odd_numbers.append(this_num)
# except:
#     pass
#
# mean = 0
# for i in odd_numbers:
#     mean = (mean+i)/2
# print(mean)


# nums = [12,34,5,3,2,423,2,23,44]
#
# def odd_numbers():
#     for i in nums:
#         if i%2==1:
#             yield i
#
#
# total = 0
# k = 0
# for i in odd_numbers():
#     total += i
#     k += 1
# print(total/k)


import threading
import random

def calculate_square(number):
    result = number * number
    print(f"Square of {number} is {result}")

def run_function_in_threads():
    numbers = [2, 4, 55, 6, 6]
    threads = []

    for _ in range (5):
        th = threading.Thread(target=calculate_square, args=(random.choice(numbers),))
        th.start()
        threads.append(th)

    for i in threads:
        i.join()

run_function_in_threads()
























