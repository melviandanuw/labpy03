# <p align="center"> TUGAS PEMROGRAMAN - Latihan1.py, Latihan2.py, & Program1.py
[![melvian](./images/melvian.png)](https://www.linkedin.com/in/melvian-wijaya-760b371b1/)


<br>


# [Latihan1.py](https://github.com/melviandanuw/TugasKelilingLuasLingkaran/blob/main/tugas.py)

<p align="justify">Tampilkan <b>N</b> bilangan acak kurang dari 0,5.

- Import Random.
```sh
import random;
```
- Masukan nilai N.
```sh
N = int(input('Masukkan nilai N: '));
```
- Looping nilai N menggunakan For.
```sh
for i in range(N)
```
- Random dengan random.uniform dengan range 0.0 - 0.5.
```sh
random2 = random.uniform(0.0, 0.5);
```
- Print hasil random.
```sh
print(random2);
```
----
# Hasil Output Latihan1.py
![Output](./images/output-l1.png)

----

<br>

<br>

<br>

# [Latihan2.py](https://github.com/melviandanuw/TugasKelilingLuasLingkaran/blob/main/tugas.py)

<p align="justify">Program untuk menampilkan bilangan terbesar dari N buah data yang diinputkan.
Masukkan angka 0 untuk berhenti.

- Buat variabel Array.
```sh
number = [];
```
- Looping menggunakan While dengan kondisi True.
```sh
while True
```
- Input nomor untuk dimasukan ke dalam Array.
```sh
numberInput = int(input('Masukkan Bilangan: '));
number.append(numberInput);
```
- Menggunakan logif If saat input == 0.
```sh
if numberInput == 0:
```
- Membuat Perulangan dengan For untuk menentukan angka terbesar dalam Array.
```sh
    max2 = number[0];
    for b in range(0, len(number)):        
        if(number[b] > max2):    
            max2 = number[b];    
```
- Menampilkan Angka Terbesar.
```sh
print('Bilangan Terbesar adalah', max2);
```
- Menghentikan While dengan Breaks saat input == 0.
```sh
if numberInput == 0:
        max2 = number[0];
        for b in range(0, len(number)):        
            if(number[b] > max2):    
                max2 = number[b];    
        print('Bilangan Terbesar adalah', max2);
        break;
```
----
# Hasil Output Latihan2.py
![Output](./images/output-l2.png)

----
<br>

<br>

<br>

# [Program1.py](https://github.com/melviandanuw/TugasKelilingLuasLingkaran/blob/main/tugas.py)

<p align="justify">Program sederhana dengan perulangan.
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.

- Buat variabel Modal, dan laba.
```sh
modal = 100000000;
laba = 0;
```
- Looping menggunakan For Range dengan kondisi 9x loops.
```sh
for i in range (9):
```
- Menggunakan Pengkondisian ketika perulangan.
```sh
if i == 1 or i == 2:
...
elif i > 2 and i < 5:
...
elif i > 4 and i < 8:
...
elif i == 8:
...
```
- Mencetak besaran laba tiap loop.
```sh
print("laba bulan ke-",i, "sebesar: ", 0);
```
- Membuat perhitungan laba dan menyimpannya pada variabel laba.
```sh
temp = modal * 1 / 100;
laba += temp;  
```
- Menampilkan Total Hasil Laba.
```sh
print('Total Laba adalah', laba);
```
----
# Hasil Output Program1.py
![Output](./images/output-p1.png)

----