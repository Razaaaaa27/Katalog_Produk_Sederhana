#  Katalog Produk Sederhana

Website katalog produk sederhana berbasis Django.  
Menampilkan homepage, daftar produk, detail produk, kontak, dan about page.

---

##  Teknologi yang Digunakan
- Python 3.13
- Django 5.2
- HTML + CSS via HttpResponse langsung 
- SQLite3 

---

##  Fitur Utama
-  Homepage (`/`)
-  Daftar Produk (`/produk/`)
-  Detail Produk (`/produk/<id>/`)
-  Halaman Kontak (`/kontak/`)
-  Halaman About (`/about/`)

---

##  Struktur Folder

```plaintext
katalog_produk/
├── db.sqlite3
├── manage.py
├── katalog_produk/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── produk/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── migrations/
        └── __init__.py
```

---

## ⚙️ Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/Razaaaaa27/Katalog_Produk_Sederhana.git
   ```

2. **Buat Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate      # (Linux/Mac)
   env\Scripts\activate         # (Windows)
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Migrasi Database**
   ```bash
   python manage.py migrate
   ```

5. **Jalankan Server**
   ```bash
   python manage.py runserver
   ```

6. **Buka Website di Browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📄 Penjelasan Views

| URL | View Function | Keterangan |
|:---|:---|:---|
| `/` | `home()` | Menampilkan homepage sederhana |
| `/produk/` | `daftar_produk()` | Menampilkan daftar produk |
| `/produk/<id>/` | `detail_produk(id)` | Menampilkan detail produk berdasarkan ID |
| `/kontak/` | `kontak()` | Menampilkan informasi kontak |
| `/about/` | `about()` | Menampilkan informasi tentang perusahaan |

---




