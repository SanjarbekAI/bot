from collections import defaultdict

user_input = int(input("Enter money: "))


bank_money = {
    '200': 9,
    '100': 10,
    '50': 25,
    '20': 13,
    '10': 33,
    '5': 22,
}

spend_money = defaultdict(int)

max_money = 0

for key, value in bank_money.items():
    max_money += int(key) * 1000 * value


if str(user_input)[-1:-4:-1][::-1] != "000":
    print("Invalid")


def get_max_num(user_money, bank_money):
    for num, count in bank_money.items():
        if user_money >= int(num) * 1000 and count != 0:
            return num
    return False


while True:
    res = get_max_num(user_input, bank_money=bank_money)
    if res is False:
        print(spend_money)
        print(bank_money)
        break
    else:
        spend_money[res] += 1
        bank_money[res] -= 1
        user_input -= int(res) * 1000


