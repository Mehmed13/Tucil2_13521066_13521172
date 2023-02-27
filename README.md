# Tucil2_13521066_13521172
Tucil 2 tentang penerapan algoritma divide and conquer dalam menentukan jarak terdekat antara dua buah titik.

Algoritma Pencarian Titik Terdekat :
1. Terima banyak titik, banyak dimensi, dan masing-masing titik.
2. Urutkan tiap titik berdasarkan posisinya di salah satu sumbu. Dalam program ini kami mengurutkan titik berdasarkan posisinya pada sumbu pertama (sumbu X).
3. Bila jumlah titik hanya dua atau tiga, langsung hitung jarak antar masing-masing titik dan kembalikan jarak terkecilnya.
4. Jika jumlah titik lebih banyak, bagi titik-titik ke dalam dua daerah dan hitung jarak terkecil di masing-masing daerah. Ambil jarak yang lebih kecil (misalkan d)   sebagai batas untuk perhitungan jarak titik antar daerah.
5. Ambil titik-titik yang jaraknya dengan garis pemisah (misal ada di posisi titik tengah) lebih kecil atau sama dengan d.
6. Untuk tiap titik, hitung jaraknya dengan titik lain yang selisih posisi di tiap sumbunya <= d.
7. Jika jaraknya lebih kecil dari d, simpan sebagai nilai d yang baru.

# Requirement Program
1. Python (penulis menggunakan versi 3.9.5+)

# Cara kompilasi
Buka file main.py di dalam folder src memakai Visual Studio Code lalu tekan tombol F5 untuk melakukan kompilasi sekaligus menjalankan program.

# Cara menjalankan program
1. Buka file main.py di dalam folder src.
2. Tekan tombol F5 untuk melakukan kompilasi dan menjalankan program.
3. Masukkan jumlah titik dan dimensi yang diinginkan.
4. Apabila ingin menyimpan output ke dalam file, ketik 'Y' lalu masukkan nama file beserta extensionnya.

# Anggota
Muhammad Fadhil Amri / 13521066

Nathan Tenka / 13521172
