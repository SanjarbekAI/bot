"""
Intagramga ro'yxatdan o'tish jarayonini amalga oshirivchi sistema tuzing

Sizda quyidagi table lar bo'ladi:
users: first_name, last_name, email, username, phone_number, password
confirmation: user_email, code, status

Asosiy menyu:

1. Login
2. Register

1. Login: username yoki phone number kiritadi va password, bazadan qidirasiz agar bor bo'lsa xush kelibsiz habari
          chiqishi kerak. Agar xato kiritilsa xato deb aytiladi va qayta urinishga imkon beriladi

2. Register: 1-etapda first_name, last_name, email, phone_number so'raladi va 4 xonali son generatsiya qilib unga
                      ko'rsatiladi
             2-etapda odam usha generatsiya qilingan raqamni kiritadi, agar to'g'ri kiritsa 
                      username va parol qo'yishga imkon beriladi
                      agar notog'ri kiritsa qayta kiritish imkoni beriladi
             3-etapda username va parol kiritiladi va akaunt yaratiladi.

E'tiborga olish kerak bo'lgan joylar:
- username, email, phone_number unique bo'lishi kerak yani takrorlanmasligi kerak
- parol eng kamida 8 ta uzinlikda bo'lishi va unda ham raqam ham harf ishtirok etishi kerak
"""