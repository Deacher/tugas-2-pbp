# Tugas 2 PBP

[Link untuk app saya](https://deacher-inventory.adaptable.app/main/)

## Jawaban untuk soal tugas 2

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat sebuah proyek Django baru.
    - Untuk membuat proyek Django baru, pertama-tama membuat virtual environment pada direktori proyek terlebih dulu.
    ```
    python -m venv env
    ```
    - Setelah itu, nyalakan virutal environment-nya.
    ```
    env\Scripts\activate.bat
    ```
    - Membuat `requirements.txt` di repositori yang sama yang kemudian menambahkan dependencies yang dibutuhkan.
    - Menjalankan perintah `pip install -r requirements.txt` untuk meng-install depedencies.
    - Membuat folder proyek dengan menjalankan command `django-admin startproject item_inventroy .`.
    - Untuk mengizinkan semua host, menambahkan `"*"` di `ALLOWED_HOSTS` pada `settings.py`.
    - Menambahkan konfigurasi `.gitignore` untuk menetukan direktori yang diabaikan oleh git.

2. Membuat aplikasi dengan nama `main` pada proyek tersebut.
    - Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru bernama `main`.
    - Menambahkan `'main'` kedalam variable `INSTALLED_APPS` pada `settings.py` di dalam direktori `item_inventory`.
    - Membuat direktori `templates` dan menambahkan `main.html`.

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
    - Menambahkan `'path('main/', include('main.urls'))'` kedalam variable `urlpatterns` di berkas `urls.py` pada direktori `item_inventory`.

4. Membuat model pada aplikasi `main` dengan nama Item dan memiliki atribut wajib.
    - Di dalam berkas `models.py`, saya menambahkan beberapa attribut pada class `Product`
        - `name`
        - `date_added`
        - `amount`
        - `description`
        - `power`
        - `mana`
        - `categories`

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Di dalam berkas `views.py`, saya menambahkan fungsi `show_main` dan menambahkan konteks `nama`, `class`, dan `app` untuk dirender ke `main.html`.
    - Kemudian, konteks yang sebelumnya sudah ditambahkan di fungsi `show_main` akan dipanggil di `main.html` dengan `{{ name }}` untuk salah satu contohnya.

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    - Menambahkan berkas `urls.py` di dalam direktori `main`.
    - Menambahkan variable `app_name = 'main'` serta `path('', show_main, name='show_main'),` pada variable list `urlpatterns` di `urls.py`.
7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Melakukan `add`, `commit`, dan `push` ke repository `tugas-2-pbp`
    - Melakukan deeploy di `adaptable.io`