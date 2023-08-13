

# HOW TO SETUP CLICKHOUSE DATA SOURCE 
1. docker-compose up -d
2. install clickhouse plugin di grafana (http://localhost:3000/connections/datasources/grafana-clickhouse-datasource)
3. aktifkan sql-driven (https://stackoverflow.com/questions/64166492/how-to-setup-an-admin-account-for-clickhouse)
   1. ```docker exec -u 0 -it ums_draft_clickhouse_1 bash``` (sesuaikan nama container eg: ums_draft_clickhouse_1 )
   2. aktifkan fitur access_management clickhouse (https://clickhouse.com/docs/en/operations/access-rights)
      1. apt-get update && apt-get install nano 
      2. nano /etc/clickhouse-server/users.xml
      3. tambahkan ini ``` <access_management>1</access_management>
       <named_collection_control>1</named_collection_control>
       <show_named_collections>1</show_named_collections>
       <show_named_collections_secrets>1</show_named_collections_secrets>```


4. buka clickhouse console http://localhost:8123/play
5. aktifkan akses ke akun default ``` ALTER USER default DEFAULT ROLE ALL ```
6. buat user super admin baru ``` CREATE USER ajik_sa IDENTIFIED BY '1122'; ```
7. kasi akses ke super admin baru ``` GRANT ALL ON *.* TO ajik_sa WITH GRANT OPTION; ```
8. buat role baru ``` CREATE ROLE grafana_readonly; ```
9. kasih akses readonly ke role baru ``` GRANT SELECT ON db.* TO grafana_readonly; ```
10. buat user sekaligus kasih akses readonly ke ``` CREATE USER grafana_user@'localhost' IDENTIFIED  BY '1122' DEFAULT ROLE grafana_readonly; ```
atau 
``` CREATE USER robi IDENTIFIED  BY '1122' DEFAULT ROLE grafana_readonly; ```

11. buka grafana http://localhost:3000/, pilih datasource clickhouse (install jika bleum), buat koneksi contoh 
    - server address : host.docker.internal
    - server port : 8123
    - username  : robi 
    - password : 1122 
    - default database : techtest_db (buat jika belum ada)

12. kirim data parquet ke container  ``` docker cp ./db ums_draft_clickhouse_1:/bitnami/clickhouse/data/user_files/ ``` (pastikan terminal disini)
13. check describe table file parquet ``` DESCRIBE TABLE file('./db/movie.parquet', Parquet) ```
14. insert movies parquet data on the fly ``` CREATE TABLE movies ENGINE = MergeTree ORDER BY tuple() AS SELECT * FROM file('./db/movie.parquet', Parquet) ```
15. insert ratings parquet data on the fly ``` CREATE TABLE ratings ENGINE = MergeTree ORDER BY tuple() AS SELECT * FROM file('./db/rating.parquet', Parquet) ```
16. test kedua data yang sudah terimport ``` select * from ratings limit 3;  ```
