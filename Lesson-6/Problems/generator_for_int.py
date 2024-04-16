"""
int raqamni ichida for bilan aylanish imkonini beruvchi generator yozing
"""


def int_generator(num):
    for char in str(num):
        yield int(char)


number = 12121212

for i in int_generator(number):
    print(i)
