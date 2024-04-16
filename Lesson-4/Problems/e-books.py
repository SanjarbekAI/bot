"""
    Kutubxona sistemasini yasash kerak, foydalanuvchi terminaldan foydalangan holda kutubxonadan 
    foydalana olsin. Kitob haqida malumotlar namedtuple ko'rinishida saqlanishi kerak
    title, author, pub_date, pages, language

    Foydalanuvchida quyidagi imkoniyatlar bo'lishi kerak:
    - yangi kitob qo'sish
    - hamma kitoblarni chiroyli ko'rinishda terminalda ko'rish
    - eng varoqi ko'p, eng yoshi katta olish
    - uz tilidagi hamma kitoblarni olish
    - biror author ni ismi kiritilsa usha ismga o'xshash hamma kitoblarni olish

    tepada keltirilgan imkoniyatlari har biri alohida funksiya bo'lishi kerak
    
    Tekshirish kerak:
    - kitob pub_date malumoti bugungi kundan ortda bo'lishi shart
    - language faqatgina [uz, ru, en] bo'lishi mumkin holos
    - pub_date quyidagi formatda bo'lishi kerak: kun-oy-yil

"""
from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'year', 'pages', 'lang'])
books = list()

def add_book():
    title = input('title: ')
    author = input('author: ')
    year = input('year: ')
    pages = input('pages: ')
    lang = input('lang: ')

    book = Book(title=title, author=author, year=year, pages=pages, lang=lang)
    books.append(book)

    return book


def get_all_books():
    text = ""
    counter = 1
    if books:
        for book in books:
            text += f"{counter}) {book.title}\t{book.author}\t{book.year}\n"
    else:
        text = "Hali kitob mavjud emas"
    return text


def find_old():
    min_year_book = books[0]

    for book in books:
        if int(book.year) < int(min_year_book.year):
            min_year_book = book

    text = f"{min_year_book.year}"
    return text
    

while True:
    user_input = input("""
1. Kitob qo'sish
2. Hamma kitoblar
3. Eng qari kitob
4. Til bo'yicha olish
0. Chiqish

""")
    
    if user_input == "1":
        new_book = add_book()
        if new_book:
            print("yangi kitob qo'shildi")
            continue

    elif user_input == "2":
        text = get_all_books()
        print(text)
    elif user_input == "3":
        text = find_old()
        print(text)
    elif user_input == "4":
        break


    






