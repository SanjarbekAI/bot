"""
Kartadan kartaga pub o'tkazish va har bir o'tkazma haqida malumot saqlash sistemasini tuzish kerak.
Ma'lumotlarni saqlash uchun postgresqldan foydalanish mumkin. 
Registeratsiya va login bo'lishi kerak

Registratsiya: full_name, card_number, expire_date, phone_number, password
Login: card_number, password

Undan keyin quyidagi imkoniyatlar bo'lishi kerak

Imkoniyatlari:
- kartadan kartaga pul o'tkazish faqatgina bizni bazada bor odamlar orasida
- o'zini kartasi haqida ma'lumot olish
- karta raqam bo'yicha barcha o'tkazmalarni ko'rish
- chiqish

Tekshirish kerak:
- karta raqam 16 ta bo'lishi
- expire date bugundan katta bo'lishi
- har bir transaksiyada expire_date ni tekshirish

"""