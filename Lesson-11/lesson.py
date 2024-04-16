"""
Bir nechta threadda bitta funksiyani ishga tushurish
Eng muhim git komandalari
bot orqali rasm jo'natish
main linux commands, deploying
Imtihondan keyin nimalarni o'rganamiz
IMtihonda 90 dan baland olgan 5 kishi uchun 1 yillik jetbrains professional

"""

import threading
import random


def say_hello(name):
    print(f"Hello {name}")


def run_threads():
    names = ['alice', 'bob', 'charlie']
    threads = []

    for _ in range(5):
        th = threading.Thread(target=say_hello, args=(random.choice(names),))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

