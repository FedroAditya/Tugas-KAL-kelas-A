# Tugas Eliminasi Gaussian

## 1. SPL (Sistem Persamaan Linear)

Sistem persamaan linear dengan lima variabel.

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 + x_5 = 15 \\
x_2 + x_3 + x_4 + x_5 = 14 \\
x_3 + x_4 + x_5 = 12 \\
x_4 + x_5 = 9 \\
x_5 = 5
\end{cases}
$$

---

## 2. Matriks Augmented

SPL diubah menjadi matriks augmented agar lebih mudah dilakukan operasi baris elementer.

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 1 & 1 & 1 & 14 \\
0 & 0 & 1 & 1 & 1 & 12 \\
0 & 0 & 0 & 1 & 1 & 9 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

---

# 3. Eliminasi Gauss

Tujuan eliminasi Gauss adalah mengubah matriks menjadi bentuk identitas menggunakan operasi baris elementer.

---

## Langkah 1

Pivot pertama berada pada **baris 1 kolom 1** dengan nilai **1**.

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 1 & 1 & 1 & 14 \\
0 & 0 & 1 & 1 & 1 & 12 \\
0 & 0 & 0 & 1 & 1 & 9 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

### Penjelasan

1. Pivot pertama ada di kolom 1 baris 1 (angka 1).  
2. Elemen di bawahnya pada kolom pertama sudah bernilai 0.  
3. Karena semua elemen di bawah pivot sudah 0 maka tidak perlu operasi baris.  
4. Matriks tetap sama dan kita lanjut ke pivot berikutnya.  

---

## Langkah 2

Pivot berikutnya berada pada **kolom ke-5 baris ke-5**.

Kita ingin membuat semua elemen **di atas pivot menjadi 0**.

Operasi baris:

$$
R_4 \leftarrow R_4 - R_5
$$

$$
R_3 \leftarrow R_3 - R_5
$$

$$
R_2 \leftarrow R_2 - R_5
$$

$$
R_1 \leftarrow R_1 - R_5
$$

Hasil matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 0 & 10 \\
0 & 1 & 1 & 1 & 0 & 9 \\
0 & 0 & 1 & 1 & 0 & 7 \\
0 & 0 & 0 & 1 & 0 & 4 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

### Penjelasan

1. Pivot berada pada kolom 5 baris 5 (angka 1).  
2. Di atas pivot terdapat beberapa angka 1.  
3. Agar menjadi 0, setiap baris dikurangi dengan baris ke-5.  
4. Hasilnya kolom ke-5 hanya memiliki satu angka 1 pada pivot.  

---

## Langkah 3

Pivot berikutnya berada pada **kolom ke-4 baris ke-4**.

Operasi baris:

$$
R_3 \leftarrow R_3 - R_4
$$

$$
R_2 \leftarrow R_2 - R_4
$$

$$
R_1 \leftarrow R_1 - R_4
$$

Hasil matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 0 & 0 & 6 \\
0 & 1 & 1 & 0 & 0 & 5 \\
0 & 0 & 1 & 0 & 0 & 3 \\
0 & 0 & 0 & 1 & 0 & 4 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

### Penjelasan

1. Pivot berada pada kolom 4 baris 4.  
2. Elemen di atas pivot masih ada angka 1.  
3. Setiap baris di atasnya dikurangi dengan baris ke-4.  
4. Tujuannya agar kolom ke-4 hanya memiliki satu pivot.  

---

## Langkah 4

Pivot berikutnya pada **kolom ke-3**.

Operasi baris:

$$
R_2 \leftarrow R_2 - R_3
$$

$$
R_1 \leftarrow R_1 - R_3
$$

Hasil matriks:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 0 & 0 & 0 & 3 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 0 & 0 & 3 \\
0 & 0 & 0 & 1 & 0 & 4 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

### Penjelasan

1. Pivot berada pada kolom 3 baris 3.  
2. Di atasnya terdapat angka 1 pada baris 1 dan 2.  
3. Baris tersebut dikurangi dengan baris ke-3.  
4. Kolom ke-3 sekarang hanya memiliki satu pivot.  

---

## Langkah 5

Pivot pada **kolom ke-2 baris ke-2**.

Operasi baris:

$$
R_1 \leftarrow R_1 - R_2
$$

Hasil matriks akhir:

$$
\left[
\begin{array}{ccccc|c}
1 & 0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 0 & 0 & 3 \\
0 & 0 & 0 & 1 & 0 & 4 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]
$$

### Penjelasan

1. Pivot berada pada kolom 2 baris 2.  
2. Di atas pivot terdapat angka 1 pada baris pertama.  
3. Baris pertama dikurangi dengan baris kedua.  
4. Matriks akhirnya menjadi matriks identitas.  

---

# 4. Hasil Akhir

Dari matriks identitas tersebut diperoleh solusi:

$$
x_1 = 1,\quad x_2 = 2,\quad x_3 = 3,\quad x_4 = 4,\quad x_5 = 5
$$