# Jawaban Tugas

# Tugas 2 PBP

## Jawaban untuk soal tugas 2

### **Nomor 1**: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

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

5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Di dalam berkas `views.py`, saya menambahkan fungsi `show_main` dan menambahkan konteks `nama`, `class`, dan `app` untuk dirender ke `main.html`.
    - Kemudian, konteks yang sebelumnya sudah ditambahkan di fungsi `show_main` akan dipanggil di `main.html` dengan `{{ name }}` untuk salah satu contohnya.

6. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
    - Menambahkan berkas `urls.py` di dalam direktori `main`.
    - Menambahkan variable `app_name = 'main'` serta `path('', show_main, name='show_main'),` pada variable list `urlpatterns` di `urls.py`.

7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Melakukan `add`, `commit`, dan `push` ke repository `tugas-2-pbp`.
    - Melakukan deeploy di `adaptable.io`.

### **Nomor 2**: Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

![Alt text](image/bagan_pbp.png)

- User merequest terhadap `urls`
- Setelah diidentifikasi path URLnya oleh django, sudah ditentukan `view` yang akan menangani request user `(routing)`.
- `View` akan menggunakan `model` untuk memproses request yang akan meneruskannya ke `template`.
- `Template` akan menghasilkan respon yang sesuai.
- HTML atau `template` diterima oleh user melewati web browser

### **Nomor 3**: Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah seperti sebuah kotak penyimpanan khusus yang digunakan untuk menyimpan berbagai perangkat dan alat yang diperlukan dalam suatu proyek tertentu. Ini membantu kita menjaga proyek-proyek yang berbeda tetap terpisah satu sama lain.

Misalnya, jika kita sedang bekerja pada beberapa proyek atau aplikasi yang menggunakan modul yang sama, tetapi memerlukan versi yang berbeda dari modul tersebut, maka virtualenv sangat berguna.

Sebagai contoh, ketika kita sedang mengembangkan sebuah aplikasi web dengan Flask versi 0.12.x, dan kemudian kita juga ingin mengembangkan aplikasi lain dengan Flask versi 1.1.x, virtualenv akan membantu kita menjaga proyek-proyek tersebut tetap terisolasi dan tidak saling mempengaruhi. Dengan cara ini, kita dapat bekerja dengan lebih efisien dan aman. Namun, Jika kita tidak menggunakan virtualenv, maka aplikasi atau proyek pertama yang menggunakan Flask 0.12.x akan secara tidak sengaja berubah menjadi Flask 1.1.x, dan semua modul yang dibutuhkan akan terus diperbarui setiap kali kita menggunakan perintah 'pip'.

### **Nomor 4**: Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model View Controller) merupakan salah satu pola arsitektur yang sangat terkenal dan banyak digunakan dalam industri perangkat lunak. Pola ini membantu dalam pemisahan peran dengan membagi aplikasi menjadi tiga komponen utama: `Model`, `View`, dan `Controller`. Dalam konteks aplikasi MVC, komunikasi antar komponen biasanya mengikuti pola pengamat. Tampilan berfungsi sebagai pengamat yang terdaftar pada pengontrol, sementara model terdaftar sebagai subjek pada pengontrol. Ketika model mengalami perubahan, model tersebut memberi tahu pengontrol, yang kemudian bertanggung jawab untuk memperbarui tampilan.

MVT (Model View Template) adalah pola desain perangkat lunak. Ini terdiri dari tiga komponen penting, yaitu Model, View, dan Template. Model digunakan untuk mengelola basis data. Ini adalah lapisan akses data yang mengelola data. Template adalah lapisan presentasi yang sepenuhnya menangani bagian Antarmuka Pengguna. View digunakan untuk menjalankan logika bisnis dan berinteraksi dengan model untuk mengambil data dan menyajikan template.

MVVM (Model-View-ViewModel) adalah sebuah kerangka kerja atau pola desain perangkat lunak yang membantu memisahkan logika bisnis dari tampilan atau kontrol antarmuka pengguna (UI) menjadi tiga bagian, yaitu model, tampilan, dan tampilan-model (viewmodel). Model didapatkan dari viewmodel setelah menerima input pengguna melalui view. View menginformasikan viewmodel apa yang dilakukan oleh pengguna. Viewmodel mendapatkan input dari view mengenai aktivitas pengguna, dan melakukan data binding 2 arah (2-way data binding).

MVT adalah konsep yang khusus untuk kerangka kerja Django dan mirip dengan MVC, dengan perbedaan utama berupa penggunaan template untuk menghasilkan tampilan. Sedangkan Tampilan dalam MVC lebih umumnya merujuk pada tampilan yang ditampilkan kepada pengguna. Untuk MVVM, berbeda dengan MVC dan MVT, karena MVVM sendiri mengimplementasikan data binding yang tidak dimiliki oleh MVC dan MVT.

### **BONUS TUGAS 2**
Untuk unit tester django, saya mengetest-kan model-model yang sudah saya implementasikan apakah sudah berjalan dengan baik.

# Tugas 3 PBP

## Jawaban untuk soal tugas 3

### **Nomor 1**: Apa perbedaan antara form POST dan form GET dalam Django?

GET lebih tepat digunakan saat kita hanya ingin mengambil data yang sederhana dan ringan, seperti saat mengakses halaman pencarian di sebuah situs web. Di sisi lain, POST lebih sesuai ketika kita perlu mengirimkan data yang bersifat rahasia atau data yang lebih kompleks, seperti saat melakukan proses login, mengirim email, atau mengisi formulir dengan banyak informasi.

### **Nomor 2**: Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML adalah fondasi yang penting untuk membuat halaman web yang fungsional dan estetis. Bahasa ini berfungsi untuk membuat struktur website hingga menyusun format teks dan gambar pada halaman web. Untuk XML dan JSON, keduanya merupakan format yang digunakan untuk menukar data dengan server. Perbedaan paling terlihat dari keduanya adalah cara menyimpannya, XML menyimpan data dengan cara yang terstruktur dan dengan mudah dibaca oleh mesin maupun manusia, akan tetapi kurang efisien. Sedangkan, JSON  menyimpan data dengan cara menyimpannya yang akan lebih efisien karena menggunakan struktur data map yang mudah diakses. Sementara itu, XML menggunakan struktur data yang lebih terstruktur dan luas karena menggunakan struktur tree.

### **Nomor 3**: Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON adalah salah satu format data yang sangat populer di internet karena kesederhanaan dan ringkasannya. Kelebihan ini membuat pemrosesan data menjadi lebih cepat, meningkatkan pengalaman pengguna, terutama ketika menyimpan preferensi dan pengaturan dari pengguna. JSON juga sering digunakan sebagai format pertukaran data dalam API untuk berbagai jenis aplikasi, pada umumnya pada web modern yaitu payment gateway untuk transaksi online.

### **Nomor 4**: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat input `form` untuk menambahkan objek `model` pada app sebelumnya.
    - Membuat berkas `forms.py` pada direktori `main` untuk struktur form yang menerima data item baru.
    - Mengimport yang dibutuhkan dengan kode ini:
    ```
    from django.forms import ModelForm
    from main.models import Item
    ```
    - Membuat class `ItemForm` yang menerima parameter `ModelForm`, didalamnya tambahkan class baru `Meta` yang kemudian diisikan dengan kode ini:
    ```
    model = Item
    fields = ["name", "amount", "description", "power", "mana", "categories"]
    ```
    Tujuan dari kode diatas adalah untuk menunjukkan field dari model yang sudah dibuat sebelumnya yang digunakan untuk form.
    - Pada berkas `views.py` di `main` menambahkan import yang dibutuhkan dengan kode ini:
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    ```
    - Membuat fungsi baru `create_item` yang menerima parameter `request`, yang kemudian diisikan dengan `form = ItemForm(request.POST or None)` untuk membuat `ItemForm` baru yang kemudian divalidasi dengan `form.is_valid()`, dan disimpan dengan `form.save()`, pada akhiran fungsi tambahkan `return HttpResponseRedirect(reverse('main:show_main'))` untuk me-redirect ke main.
    - Mengubah fungsi `show_main` pada berkas `views.py`  menambahkan `items = Item.objects.all()` untuk mengambil seluruh object item yang disimpan di database.
    - Menambahkan `path('create-item', create_item, name='create_item'),` pada berkas `urls.py` di `main`.
    - Membuat berkas `create_product.html` pada direktori `main/templates` yang kemudian diisi table untuk form dengan `{{ form.as_table }}`, token `{% csrf_token %}` untuk security, menandakan block untuk form POST dengan kode `<form method="POST">`, dan tombol submit `<input type="submit" value="Add Product"/>` untuk mengirimkan request ke view.

2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID, serta membuat routing URL untuk masing-masing views yang telah ditambahkan sebelumnya.
    - Menambahkan fungsi `show_xml` pada `views.py` di `main` dengan kode ini:
    ```
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    Kemudian menambahkan path routing `path('show_xml/', show_xml, name='show_xml'),` di `urls.py` pada `main`.
    - Menambahkan fungsi `show_json` pada `views.py` di `main` dengan kode ini:
    ```
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Kemudian menambahkan path routing `path('json/', show_json, name='show_json'),` di `urls.py` pada `main`.
    - Menambahkan fungsi `show_xml_by_id` pada `views.py` di `main` dengan kode ini:
    ```
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    Kemudian menambahkan path routing `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),` di `urls.py` pada `main`.
    - Menambahkan fungsi `show_json_by_id` pada `views.py` di `main` dengan kode ini:
    ```
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Kemudian menambahkan path routing `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),` di `urls.py` pada `main`.

### **BONUS TUGAS 3**
Untuk menunjukkan banyak jumlah item yang sudah ditambahkan pada aplikasi adalah dengan cara menambahkan `items_total = items.count()` di fungsi `show_main` di `views.py` pada `main` yang kemudian ditambahkan di variable `context`. Lalu, tambahkan templatenya pada `main.html`.

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
<img src="/image/html_postman.png">
<img src="/image/xml_postman.png">
<img src="/image/json_postman.png">
<img src="/image/xmlbyid_postman.png">
<img src="/image/jsonbyid_postman.png">

# Tugas 4 PBP

## Jawaban untuk soal nomor 4

### **Nomor 1**: Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web dengan tiga field, diantaranya username, password1, dan password2 yang merupakan konfirmasi password. Kelebihan yang signifikan dari Django UserCreationForm adalah mudah diimplementasikan dan digunakan. Sedangkan, kekurangan yang dapat ditemui pada Django UserCreationForm adalah kurang fleksibel jika ingin memiliki formulir pendaftaran yang kompleks, karena memiliki field yang terbatas.

### **Nomor 2**: Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses untuk memverifikasi siapa usernya. Sedangkan otorisasi adalah proses untuk memverifikasi bahwa user memiliki akses ke sesuatu hal. Autentikasi dan otorisasi adalah dua proses keamanan informasi penting yang digunakan oleh administrator untuk melindungi sistem dan data. Autentikasi mengkonfirmasi identitas pengguna atau layanan, sedangkan otorisasi menetapkan izin akses mereka.

### **Nomor 3**: Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah file teks yang berisi sejumlah kecil data yang digunakan untuk mengidentifikasi mesin ketika terhubung ke jaringan. Django mengidentifikasi setiap browser dan sesi yang terkait dengan situs dengan menggunakan cookie yang membawa ID sesi yang unik. Secara default, data sesi yang sebenarnya disimpan di database situs.

### **Nomor 4**: Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Cookie tidak terlalu aman, keamanan mereka tergantung pada bagaimana mereka digunakan dan diatur. Cookie adalah potongan-potongan kecil data yang situs web menyimpan pada perangkat pengguna untuk melacak informasi atau menyimpan data sesi. Jika cookie tidak dilindungi, penjahat cyber dapat mencuri informasi pribadi.

### **Nomor 5**: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    - Pada `views.py`di folder `main`, import `redirect`, `UserCreationForm`, dan `messages`, lalu membuat fungsi dengan nama `register` dengan kode berikut:
    ```
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
    Setelah membuat fungsi register, buat file `register.html` pada template di main untuk mendapatkan data register di web. Kemudian lakukan routing di `urls.py` dengan `path('register/', register, name='register'),`.
    - Pada `views.py` di folder `main`, import `authenticate` dan `login`, lalu membuat fungsi dengan nama `login_user` dengan kode berikut:
    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```
    Setelah membuat fungsi login_user, buat file `login.html` pada template di main untuk mendapatkan data login di web. Kemudian lakukan routing di `urls.py` dengan `path('login/', login_user, name='login'),`.
    - Pada `views.py` di folder `main`, import `logout`, lalu membuat fungsi dengan nama `logout_user` dengan kode berikut:
    ```
    def logout_user(request):
    logout(request)
    return redirect('main:login')
    ```
    Setelah membuat fungsi logout_user, Tambahkan potongan kode di bawah ini pada `main.html` di template main untuk menambahkan button di web. 
    ```
    <a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
    </a>
    ```
    Kemudian lakukan routing di `urls.py` dengan `path('logout/', logout_user, name='logout'),`.
    - Menambahkan kode dibawah ini di atas fungsi `show_main` agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
    ```
    @login_required(login_url='/login')
    def show_main(request):
    ```
2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
<img src="/image/akun_1.png">
<img src="/image/akun_2.png">

3. Menghubungkan model Item dengan User.
    - Dalam `models.py` import user, kemudian tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` di dalam model Item yang ada. Modifikasi `create-item` untuk menetapkan bidang pengguna ke User object yang terkait dengan pengguna yang saat ini masuk, menunjukkan bahwa item itu milik pengguna tersebut dengan kode berikut:
    ```
    def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
    ```
    Pada fungsi `show_main` tambahkan `'name': request.user.username` untuk mendapatkan username user. Kemudian lakukan migration untuk modelnya.

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
<img src="/image/last_login_1.png">
<img src="/image/last_login_2.png">

### **BONUS TUGAS 4**
Untuk bonus, tambahkan kode berikut dibawah ini pada `views.py`:
```
if request.method == 'POST':
    if 'increment' in request.POST:
        item_id = request.POST.get('increment')
        item = items.get(id=item_id)
        item.amount += 1
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    elif 'decrement' in request.POST:
        item_id = request.POST.get('decrement')
        item = items.get(id=item_id)
        if item.amount == 1:
                item.amount -= 1
                item.delete()
        else:
            item.amount -= 1
            item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    elif 'delete' in request.POST:
        item_id = request.POST.get('delete')
        item = items.get(id=item_id)
        item.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
```
Kemudian, menambahkan button untuk masing-masing kegunaan pada `main.html`

# Tugas 5 PBP

## Jawaban untuk soal nomor 5

### **Nomor 1**: Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
1. Element Sector bermanfaat untuk memilih elemen HTML berdasarkan nama tag. Contohnya, untuk memilih semua elemen `<p>` pada halaman web, kita dapat menggunakan kode berikut:
```$("p")```. Element Selector dapat digunakan ketika kita ingin memilih elemen HTML berdasarkan nama tag.
2. ID Selector bermanfaat untuk memilih elemen HTML berdasarkan ID. Contohnya, untuk memilih elemen dengan ID `#intro` pada halaman web, kita dapat menggunakan kode berikut:
```$("#intro")```. ID Selector dapat digunakan ketika kita ingin memilih elemen HTML berdasarkan ID.
3. Class Selector bermanfaat untuk memilih elemen HTML berdasarkan class. Contohnya, untuk memilih elemen dengan class `.intro` pada halaman web, kita dapat menggunakan kode berikut:
```$(".intro")```. Class Selector dapat digunakan ketika kita ingin memilih elemen HTML berdasarkan class.
4. Universal Selector bermanfaat untuk memilih semua elemen HTML pada halaman web. Contohnya, untuk memilih semua elemen pada halaman web, kita dapat menggunakan kode berikut:
```$("*")```. Universal Selector dapat digunakan ketika kita ingin memilih semua elemen HTML pada halaman web.
5. Group Selector bermanfaat untuk memilih beberapa elemen HTML. Contohnya, untuk memilih semua elemen `<p>` dan semua elemen dengan class `.intro` pada halaman web, kita dapat menggunakan kode berikut:
```$("p, .intro")```. Group Selector dapat digunakan ketika kita ingin memilih beberapa elemen HTML.

### **Nomor 2**: Jelaskan HTML5 Tag yang kamu ketahui.
1. `<header>` Tag untuk mendefinisikan header untuk dokumen atau bagian.
2. `<nav>` Tag untuk mendefinisikan bagian navigasi.
3. `<section>` Tag untuk mendefinisikan bagian dalam dokumen.
4. `<article>` Tag untuk mendefinisikan konten independen.
5. `<aside>` Tag untuk mendefinisikan konten yang berdiri sendiri.

### **Nomor 3**: Jelaskan perbedaan antara margin dan padding.
Margin adalah ruang di luar elemen, sedangkan padding adalah ruang di dalam elemen. Margin dan padding dapat digunakan untuk mengatur jarak antara elemen HTML.

### **Nomor 4**: Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS adalah framework CSS yang dirancang untuk membangun antarmuka kustom dengan cepat. Tailwind CSS tidak hadir dengan komponen UI yang siap pakai, tetapi menyediakan kelas utilitas yang dapat digunakan untuk membangun antarmuka kustom. Tailwind CSS dapat digunakan ketika kita ingin membangun antarmuka kustom dengan cepat. Sedangkan, Bootstrap adalah framework CSS yang dirancang untuk membangun antarmuka responsif. Bootstrap dengan komponen UI yang siap pakai yang dapat digunakan untuk membangun antarmuka responsif. Bootstrap dapat digunakan ketika kita ingin membangun antarmuka responsif dengan cepat.