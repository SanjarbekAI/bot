"""
Bankamatda 540 ming so'm pul bor va ular 3 ta 100 4 ta 50 1 ta 20 1 ta 10 2 ta 5 minglik

Agar odam menda 150 ming so'rasa men unga 1 ta 100 va 1 ta 50 berishim kerak
yani avval eng katta valyutalarni berishim kerak. Agar u so'ragan pulni chiqarish
imkoni bo'lmasa noto'g'ri summa deyiladi agar u so'ragan miqdorda pul bankamatda yo'q
bo'lsa pul yetarli emas deyiladi
"""

from collections import defaultdict


class CalculateMoney:
    def __init__(self, money, total_money):
        self.money = money
        self.total_money = total_money
        self.max_money = 0
        self.spend_money = defaultdict(int)

    def calculate_max_money(self):
        for key, value in self.total_money.items():
            self.max_money += int(key) * value

    def minus_max_sum(self):
        for key1, value1 in self.total_money.items():
            if int(key1) * 1000 <= self.money:
                self.total_money[key1] -= 1
                self.money -= int(key1) * 1000
                return key1
        return False

    def calculate_num_of_sum(self):
        while True:
            res = self.minus_max_sum()
            if res is False:
                for num, count in self.spend_money.items():
                    print(f"{num}: {count} ta", end="\n")
                break
            else:
                bank.spend_money[res] += 1


user_input = int(input("Enter money: "))

bank_money = {
    '200': 9,
    '100': 10,
    '50': 25,
    '20': 13,
    '10': 33,
    '5': 22,
}

bank = CalculateMoney(user_input, bank_money)
bank.calculate_num_of_sum()
