import auth
import queries
from typing import Callable, Any, List


def main() -> None:
    user_input = input("""
1. Register
2. Login
0. Stop code
""")
    if user_input == "1":
        return auth.register()
    elif user_input == "2":
        return auth.login()
    elif user_input == "0":
        print("Good bye")
    else:
        print("Invalid code")
        main()


def services(card_number: str, password: str) -> Callable[..., Any]:
    """provide information about all services to user"""

    user_input = input("""
1. Balance
2. Transfer
3. History
0. Logout
""")
    if user_input == "1":
        return queries.user_balance(card_number, password)
    elif user_input == "2":
        return queries.transfer(card_number, password)
    elif user_input == "3":
        return queries.history(card_number, password)
    elif user_input == "0":
        main()


if __name__ == '__main__':
    main()


