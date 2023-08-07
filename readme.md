# Dokumentasi

## struktur folder projek 
| File                  | Description                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| result                | berisi screenshot dari hasil program                                                                        |
| main.py               | berisi kode untuk menjalankan proses kalkulasi top 10 movie dan genres marketshare                          |
| docker-compose        | helper buat setup grafana dan data source                                                                   |
| web                   | Vue JS Project yang berisi visualisasi Grafik                                                               |


## prerequisite
1. ```python```
2. ```node >= 18```


## how to run 
1. buat folder ```db```, download file parquet https://drive.google.com/drive/folders/1jmBMkgX83ylr5POevb0HJHUd8NuPFlNL?usp=drive_link lalu masukkan ke folder db 
2. ```python -m venv venv &&```
3. ```source venv/bin/activate```
4. ```pip -r requirements.txt```
5. ```python main.py```
6. ```cd web```
7. ```npm install```
8. ```npm run dev```


## Catatan 
1. source code task visualisasi menggunakan python matplotlib terdapat pada file main.py
2. visualisasi dengan Grafana terkendala secara teknis (penyimpanan storage penuh), sehingga mohon maaf dengan besar hati task ini tidak dapat terselesaikan. terdapat 3 pendekatan yang sudah dilakukan untuk menyelesaikan task ini yaitu :
   - MySQL sebagai data source, hasilnya Database MySQL kurang cocok untuk menyelesaikan kasus ini dikarenakan data yang digunakan memiliki kapasitas yang cukup besar
   - Endpoint API sebagai data source, pendekatan ini menggunakan API sebagai data source, akan tetapi proses query dilakukan  disisi backend sehingga hasil kurang kredibel
   - JSON / CSV sebagai data source, data parquet dirubah kedalam JSON / CSV kendala pada tahapan ini adalah pada sisi query data
  
  solusi lain yang perlu dicoba adalah dengan menggunakan Clickhouse database sebagai data source.

3. source code visualisasi dalam bentuk web terdapat pada folder web/src