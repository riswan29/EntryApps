1) django-admin startproject partai (bebas mau di namain apa di aku namanya kubuat partai)

2) django-admin startapp apps (ini juga bebas ini nanti tempat fitur yang bakalan kita buat nantinya)

3) masuk ke folder yang dah dibuat di nomor 1 di aku kan namanya partai, jadi masuk ke folder partai , pilih settings.py, scroll cari yang namanya installed_apps, nah di akhir tambahin (nama folder yang kalian buat di nomor 2 di aku kan namanya apps jadi aku buat apps) => 'apps',

4) kemudian di badian Templates masih di settings tinggal scroll aja ntar ada root nya template, nah di bagian 'DIRS': [] itu kan kosong tuh di dalamnya, tinggal tambahin  [BASE_DIR, 'templates'], atau kalian bisa aja buat cuman  ['templates'], gitu aja juga bisa, tapi saran ikutin yang pertama ,

5) nah lanjut ke buat db nya , habis lakuin semua yang di atas kita lanjut buat db , di situ kan belum ada tuh db nya kan kalau kalian liat samua flenya,untuk buatnya kalian jalanin perintah **python manage.py migrate** nah ini nanti bakalan buatin kalian db nya nanti itu semua auth , koneksi semuanya yang berhubungan dengan root nya akan di buatin, udah itu nanti kalian bakalan liat bakalan nambah 1 file namnaya db.sqlite3

6) kalau itu dah ada nih, lanjut ke **models.py** nah disini kita bakalan buat db kita , untuk setiap operator nya nanti

7) aku kan udah buat nih yang aku ntar coba ikutin kaya punyaku juga versi opertor yang kalian pake
```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('entry', 'Entry'),
        ('perbaikan', 'Perbaikan'),
        ('keuangan', 'Keuangan'),
        ('dapal', 'Dapal'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
```
itu tuh model untuk registrasi yang aku buat,nah nanti kalian lanjutin lah dengan role yang kalian buat dulu

8) selesai kalian buat modelnya jagan lupa migrate

```python
python manage.py makemigrations
python manage.py migrate
```

9) nah udah itu nanti bakalan selesai tuh db nya di buat kalau berhasil di jalanin semuanya,

10) lanjut buatin views, formsm, urls sama tempaltenya juga ,

11) nanti kalau ada yang mau ditanyain lagi tanya aja di grup oke ges hehe...
