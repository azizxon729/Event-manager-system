# 📅 Event Manager System API

Ushbu loyiha tadbirlarni boshqarish, ularni ko'rish va foydalanuvchilarni tadbirlarga ro'yxatdan o'tkazish uchun mo'ljallangan **Django REST Framework (DRF)** asosida yaratilgan kuchli backend API tizimidir. Loyihada foydalanuvchilar xavfsizligi va validatsiya tizimiga alohida e'tibor qaratilgan.

---

## ✨ Imkoniyatlar va Funksiyalar

*   **Tadbirlar boshqaruvi (Events):** Yangi tadbirlar yaratish (`POST`) va barcha faol tadbirlar ro'yxatini ko'rish (`GET`).
*   **Xavfsizlik (Authentication):** API so'rovlari **Basic Authentication** yordamida himoyalangan. Tizimga kirmagan foydalanuvchilar tadbir yarata olmaydi yoki ro'yxatdan o'ta olmaydi.
*   **Avtomatik bog'liqlik:** Tadbir yaratilganda yoki ro'yxatdan o'tilganda, foydalanuvchi (`user`) ma'lumotlari so'rov yuborayotgan profildan avtomatik aniqlanadi va bazaga yoziladi.
*   **Tadbir sig'imi validatsiyasi (Capacity Check):** Agar tadbirlarda joy qolmagan bo'lsa (ya'ni ro'yxatdan o'tganlar soni `capacity` limitiga yetsa), tizim yangi foydalanuvchini ro'yxatdan o'tkazmaydi va xatolik qaytaradi.
*   **Mening tadbirlarim:** Har bir foydalanuvchi faqat o'zi ro'yxatdan o'tgan tadbirlar ro'yxatini alohida ko'ra oladi.
*   **Ro'yxatdan o'tishni bekor qilish:** Foydalanuvchilar o'zlari yozilgan tadbir ro'yxatidan o'chib ketish imkoniyatiga ega (`DELETE`).

---

## 🛠 Ishlatilgan Texnologiyalar

*   **Backend:** Python 3.x, Django 5.x
*   **API Framework:** Django REST Framework (DRF)
*   **Ma'lumotlar bazasi:** SQLite (Loyiha ichiga o'rnatilgan)
*   **API Testlash:** Postman

---

## 🚀 Loyihani Kompyuterda Ishga Tushirish

Loyihani o'zingizning kompyuteringizda sinab ko'rish uchun quyidagi buyruqlarni ketma-ket bajaring:

1. **Loyihani yuklab olish (Clone):**
```bash
   git clone [https://github.com/SizningGithubProfilingiz/repo-nomi.git](https://github.com/SizningGithubProfilingiz/repo-nomi.git)
   cd repo-nomi
2. **Virtual muhitni yaratish va faollashtirish:**
python -m venv venv
   # Windows uchun:
   venv\Scripts\activate
   # Linux/Mac uchun:
   source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

---

### 💡 Maslahat:
Faylni chiroyli ko'rsatish uchun yuqoridagi `[http://azizxon.pythonanywhere.com/](http://azizxon.pythonanywhere.com/)` qismiga o'zingizning PythonAnywhere saytidagi haqiqiy havolangizni va `git clone` yozilgan joyga esa o'zingizning GitHub silkangizni qo'yib qo'ysangiz yanada zo'r bo'ladi!
