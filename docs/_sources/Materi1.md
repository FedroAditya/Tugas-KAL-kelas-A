# materi 1

# Rangkuman Materi: Sistem Persamaan Linear

Berdasarkan materi yang dipelajari, berikut adalah poin-poin utama mengenai Sistem Persamaan Linear:

---

## 1. Definisi Persamaan Linear
Sebuah **persamaan linear** dalam $n$ variabel ($x_1, x_2, \dots, x_n$) adalah persamaan yang dapat disederhanakan menjadi bentuk baku:

$$a_1x_1 + a_2x_2 + \dots + a_nx_n = b$$

* **Variabel:** $x_1, x_2, \dots, x_n$ adalah peubah yang tidak diketahui.
* **Koefisien:** $a_1, a_2, \dots, a_n$ adalah bilangan real tetap.
* **Konstanta:** $b$ adalah bilangan real di ruas kanan.

### Klasifikasi Persamaan:
1.  **Homogen:** Jika $b = 0$.
2.  **Nonhomogen:** Jika $b \neq 0$.
3.  **Nonlinear:** Jika variabel memiliki pangkat selain satu (misal: $x^2$), terdapat perkalian antar variabel (misal: $xy$), atau variabel berada di dalam fungsi non-polinomial (misal: $\sin(x)$).

---

## 2. Sistem Persamaan Linear
SPL adalah himpunan atau kumpulan dari beberapa persamaan linear. Sebuah sistem disebut **homogen** jika seluruh persamaan di dalamnya adalah homogen.

### Karakteristik Solusi SPL:
Setiap SPL memiliki salah satu dari tiga kemungkinan solusi berikut:
1.  **Tidak Konsisten:** Tidak memiliki solusi (himpunan kosong).
2.  **Konsisten (Solusi Tunggal):** Memiliki tepat satu pasang nilai variabel yang memenuhi.
3.  **Konsisten (Solusi Tak Hingga):** Memiliki banyak sekali penyelesaian.



---

## 3. Representasi Matriks
Untuk mempermudah komputasi, SPL sering direpresentasikan dalam bentuk matriks.

* **Matriks Koefisien ($A$):** Matriks yang elemennya terdiri dari koefisien-koefisien variabel.
* **Vektor Konstanta ($\mathbf{b}$):** Vektor kolom yang berisi nilai-nilai $b$ dari tiap persamaan.
* **Matriks Augmentasi ($[A | \mathbf{b}]$):** Matriks yang menggabungkan matriks koefisien dan vektor konstanta dalam satu tampilan untuk mempermudah operasi baris.

---

## 4. Implementasi Komputasi (SageMath)
Materi ini juga memperkenalkan penggunaan **Sage** untuk memproses matriks secara otomatis:

* **Membuat Matriks:** `A = matrix(QQ, baris, kolom, [[elemen]])`
* **Augmentasi:** `M = A.augment(b)` digunakan untuk menempelkan vektor konstanta ke matriks koefisien.
* **Subdivisi:** `M.subdivide([baris],[kolom])` digunakan untuk memberikan garis pemisah visual agar matriks lebih mudah dibaca.