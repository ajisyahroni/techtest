# Dokumentasi

## struktur folder projek 
| File / Folder         | Description                                                                                                 |
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
1. source code task visualisasi menggunakan python matplotlib terdapat pada file main.py (lama) atau fix_top_ten_movies.py (terbaru)
2. Hasil implementasi disajikan pada dokumen https://docs.google.com/document/d/1O4J8UHHgdVMsrUaKZyg7pfCytCigbMAYJgAhwboVeyQ/edit?usp=sharing
3. source code visualisasi dalam bentuk web terdapat pada folder web/src


## Catatan Installasi 
untuk menjalankan visualisasi dengan grafana cek pada [Tahapan Installasi Docker Grafana Clickhouse](installation.md)

untuk memperoleh hasil query yang sama gunakan query pada file-file *.sql
gunakan file json grafana ['File JSON Dashboard Grafana'](grafana-clickhouse-dashboard-1691955780325.json) untuk mengimport dashboard