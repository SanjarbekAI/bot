"""
Har bir guruh bir mavzuga tayyorgarlik ko'rib 10 daqiqa ichida bir mavzuni tushuntirib berishi kerak bo'ladi
Kodlar orqali misollar keltirishi kerak

Ushbu muhim mavzularga doir masalalarni hamma bajarishi kerak:

GIT
Generator
Iterator
Threads
context manager

Har bir amalni bajargandan keyin alohida commit qiling

1. Kompyuteringizda bitta papka ochasiz uni ichiga quyidagi fayllarni yaratasiz
.gitignore
generator.py
iterator.py
threads.py
context_manager.py

1. Ushbu list ichidagi toq sonlar qaytarib beradigan generator yozing. Va undan qaytgan natijani ichida for
   orqali aylanib o'rta arifmetigini toping.
   nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]

2. Ushbu list ichida for ishlatmasdan iterator va while orqali aylanib juft sonlarni yig'indisni toping
3. Ushbu funksiyani 5 ta thread da run qiling

def calculate_square(number):
    result = number * number
    print(f"Square of {number} is {result}")


def run_function_in_threads():
    numbers = [2, 4, 55, 6, 6]
    threads = []

4. with context manageri orqali test.txt fayl oching va uni ichiga 1 dan 100 gacha bo'lgan sonlarni yozing.

"""

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]


def find_odd(numbers: list):
    for number in numbers:
        if number % 2 != 0:
            yield number


total = 0
counter = 0

for i in find_odd(nums):
    total += i
    counter += 1
print(total / counter)
