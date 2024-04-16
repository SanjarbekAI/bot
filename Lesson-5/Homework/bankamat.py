"""
Bankamatlarga o'xshab ishlaydigan sistema tuzish kerak
Postgresql baza sifatida ishlatilsin.

Asosiy menyuda:
- Register
- Login
- Stop code
- Enter money to system

Register -> foydalanuvchi bank sistemasi uchun ro'yxatdan o'tadi [full_name, card_number, expire_date, balance, password
            phone_number -> bu joyda kiritmaydi lekin tableda bo'lishi kerak]
Login -> foydalanuvchi bankamatdan foydalanish uchun card_number va passwordni kiritadi
Stop code -> dasturni tugatish

Imkoniyatlar:
- SMS habarnoma ulash
- Balance ni ko'rish
- Naqd pul olish

SMS habarnoma ulash -> telefon nomer so'raladi va bazadan shu karta raqam egasini telefon raqami bazada bormi yo'qmi
                       tekshirikadi agar yo'q bo'lsa qo'shiladi va sms habarnoma yoqildi deyiladi, bor bo'lsa ulangan
                       degan habar chiqariladi
- Balance ni ko'rish -> qancha puli borli ko'rsatiladi
- Naqd pul olish -> pul miqdori so'raladi va bankamotdagi pul va foydalanuvchi hisobidagi pul tekshiriladi agar
                    bankamatda yetarlicha mablag' bor bo'lsa va foydalanuvchida ham yetarlicha mablag' bor bo'lsa
                    bankamatdan shuncha summa ayiriladi, va foydalanuvchi kartasidan ham ayiriladi 1 foiz xizmat haqi
                    olinadi va u 1 foiz bankamat summasiga qo'shiladi

- Enter money to system -> bu imkoniyatdan foydalanish uchun foydalanuvchi maxsus marolni bilishi kerak bo'ladi
                           maxsus parolni o'zingiz o'ylab topasiz va bir o'zgaruvchiga saqlab qo'yasiz

                           maxsus parol so'raladi agar to'g'ri kirtilsa qancha miqdorda pul bankamatga qo'shoqchiligi
                           so'raladi va bankamatgagi pul miqdori shunchaga oshiriladi

                           maxsus parol xato bo'lsa yana qayta parol so'raladi

Tekshirish kerak:
- karta ramqa 16 ta bo'lishi
- parol 4 ta bo'lishi
- expire date bugundan o'tib ketgan bo'lmasligi

Qo'shimcha imkoniyatlar(bularni qo'shish majburiy emas):
- maxsus parolni 3 marttadan ko'proq xato tergandan keyin dasturni tugatish
- qaysi foydalanuvchiga qancha miqdorda pul berilganini bazada saqlab ketish
"""