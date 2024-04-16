from database import Database

def create_tables():
    users = """
    create table if not exists users(
    id serial primary key,
    full_name varchar(32),
    card_number varchar(16),
    phone_number varchar(9),
    password varchar(4),
    balance numeric,
    created_at timestamp default now()
    )
"""

    transactions = """
    create table if not exists transactions(
    id serial primary key,
    from_user_id int references users(id),
    to_user_id int references users(id),
    money numeric,
    status boolean,
    created_at timestamp default now()
    )
"""

    print(Database.connect(users, 'create'))
    print(Database.connect(transactions, 'create'))


if __name__ == '__main__':
    create_tables()