"""
for loop vazifani bajarib beradigan while yozing iterator orqali

1. ushbu sonlar ichida 5 ga bo'linadigan eng kattasi ni topong
2. ushbu ismlar ichida unli harflar eng ko'pini toping
"""

# nums = [12, 23, 40, 100, 55, 66, 75]
# max_num = 0
#
# nums = iter(nums)
#
# while True:
#     try:
#         num = next(nums)
#         if num % 5 == 0 and num > max_num:
#             max_num = num
#     except StopIteration:
#         break
# print(max_num)


names = ['alice', 'bob', 'charlie', 'david', 'eve', 'fred', 'sasasasasa']

max_vowel_name = names[0]

names = iter(names)


def find_vowels_count(text):
    counter = 0
    for char in text:
        if char in 'aeiouAEIOU':
            counter += 1
    return counter


while True:
    try:
        name = next(names)
        max_vowels_count = find_vowels_count(max_vowel_name)
        vowels_count = find_vowels_count(name)
        if vowels_count >= max_vowels_count:
            max_vowel_name = name
    except StopIteration:
        break
print(max_vowel_name)
