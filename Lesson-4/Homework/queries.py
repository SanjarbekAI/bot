from database import Database
import main


def user_balance(card_number, password):
    query = f"SELECT * FROM users WHERE card_number = '{card_number}' and password = '{password}'"
    user = Database.connect(query, 'select', fetchone=True)
    if not user:
        print("Invalid password or card number")
        return main.services(card_number, password)
    print(f"Your balance: {user[5]}")
    return main.services(card_number, password)


def transfer(card_number, password):
    query = f"SELECT * FROM users WHERE card_number = '{card_number}' and password = '{password}'"
    user = Database.connect(query, 'select', fetchone=True)

    to_user_card_number = input("Enter user card number: ")
    query = f"SELECT * FROM users WHERE card_number = '{to_user_card_number}'"
    to_user = Database.connect(query, 'select', fetchone=True)
    if not to_user:
        print("User not found")
        return main.services(card_number, password)
    money = float(input("Enter money: "))
    while money > user[5]:
        print("You dont have enough money")
        money = float(input("Enter money: "))
    user_money = float(user[5]) - money
    to_user_money = float(to_user[5]) + money

    update_user_money = f"UPDATE users SET balance={user_money} WHERE card_number = '{card_number}'"
    Database.connect(update_user_money, 'update')
    update_to_user_money = f"UPDATE users SET balance={to_user_money} WHERE card_number = '{to_user_card_number}'"
    Database.connect(update_to_user_money, 'update')

    query = f"""INSERT INTO transactions(from_user_id, to_user_id, money, status) VALUES(
    {user[0]}, {to_user[0]}, {money}, True
    )"""
    Database.connect(query, 'insert')
    print("Money is sent")
    return main.services(card_number, password)


def history(card_number, password):
    query = f"SELECT * FROM users WHERE card_number = '{card_number}'"
    user = Database.connect(query, 'select', fetchone=True)

    query = f"SELECT * FROM transactions WHERE from_user_id = {user[0]}"
    user_transactions = Database.connect(query, 'select', fetchall=True)

    if not user_transactions:
        print("There is no transactions yet")
        return main.services(card_number, password)
    for transaction in user_transactions:
        query = f"SELECT * FROM users WHERE id = {transaction[2]}"
        to_user = Database.connect(query, 'select', fetchone=True)
        print(f"""
To: {to_user[1]}
Money: {transaction[3]}
Date: {transaction[5]}
""")
    return main.services(card_number, password)
