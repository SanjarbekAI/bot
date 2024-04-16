import main
from database import Database

def register():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    card_number = input("Enter your card number: ")
    password = input("Enter your password: ")
    balance = input("Enter your balance: ")

    query = f"""INSERT INTO users (full_name, phone_number, card_number, password, balance) VALUES (
    '{full_name}', '{phone_number}', '{card_number}', '{password}', {balance}
    )"""
    print(Database.connect(query, 'insert'))
    return main.services(card_number, password)


def login():
    card_number = input("Enter your card number: ")
    password = input("Enter your password: ")

    query = f"SELECT * FROM users WHERE card_number = '{card_number}' and password = '{password}'"
    user = Database.connect(query, 'select', fetchone=True)
    if not user:
        print("Invalid password or card number")
        return main.main()
    return main.services(card_number, password)