# Tugas Eliminasi Gaussan

## 1. SPL (Sistem Persamaan Linear)

$$
\begin{cases}
2x_1 + 0x_2 + 0x_3 + 0x_4 + 0x_5 = 2 \\
3x_1 + 2x_2 + 0x_3 + 0x_4 + 0x_5 = 7 \\
0x_1 + 4x_2 + 2x_3 + 0x_4 + 0x_5 = 14 \\
0x_1 + 0x_2 + 5x_3 + 2x_4 + 0x_5 = 23 \\
0x_1 + 0x_2 + 0x_3 + 6x_4 + 2x_5 = 34
\end{cases}
$$

## Matriks Augmented

$$
\left[\begin{array}{ccccc|c}
2 & 0 & 0 & 0 & 0 & 2 \\
3 & 2 & 0 & 0 & 0 & 7 \\
0 & 4 & 2 & 0 & 0 & 14 \\
0 & 0 & 5 & 2 & 0 & 23 \\
0 & 0 & 0 & 6 & 2 & 34
\end{array}\right]
$$

## 3. Eliminasi Gauss (OBE)

**Matriks Augmented Awal:**
$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & | & 1 \\
3 & 1 & 0 & 0 & 0 & | & 5 \\
0 & 2 & 1 & 0 & 0 & | & 7 \\
0 & 0 & 3 & 1 & 0 & | & 13 \\
0 & 0 & 0 & 4 & 1 & | & 21
\end{bmatrix}
$$

<br>

#### Langkah 1: nolkan elemen di bawah pivot kolom 1
Operasi baris: $R_2 \leftarrow R_2 - 3R_1$

Penjelasan:
1. Pivot pertama ada di kolom 1 baris 1 (angka 1).
2. Di bawahnya (baris 2 kolom 1) ada angka 3.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan 3 kali baris 1 dari baris 2.

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & | & 1 \\
0 & 1 & 0 & 0 & 0 & | & 2 \\
0 & 2 & 1 & 0 & 0 & | & 7 \\
0 & 0 & 3 & 1 & 0 & | & 13 \\
0 & 0 & 0 & 4 & 1 & | & 21
\end{bmatrix}
$$

<br>

#### Langkah 2: nolkan elemen di bawah pivot kolom 2
Operasi baris: $R_3 \leftarrow R_3 - 2R_2$

Penjelasan:
1. Pivot kedua ada di kolom 2 baris 2 (angka 1).
2. Di bawahnya (baris 3 kolom 2) ada angka 2.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan 2 kali baris 2 dari baris 3.

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & | & 1 \\
0 & 1 & 0 & 0 & 0 & | & 2 \\
0 & 0 & 1 & 0 & 0 & | & 3 \\
0 & 0 & 3 & 1 & 0 & | & 13 \\
0 & 0 & 0 & 4 & 1 & | & 21
\end{bmatrix}
$$

<br>

#### Langkah 3: nolkan elemen di bawah pivot kolom 3
Operasi baris: $R_4 \leftarrow R_4 - 3R_3$

Penjelasan:
1. Pivot ketiga ada di kolom 3 baris 3 (angka 1).
2. Di bawahnya (baris 4 kolom 3) ada angka 3.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan 3 kali baris 3 dari baris 4.

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & | & 1 \\
0 & 1 & 0 & 0 & 0 & | & 2 \\
0 & 0 & 1 & 0 & 0 & | & 3 \\
0 & 0 & 0 & 1 & 0 & | & 4 \\
0 & 0 & 0 & 4 & 1 & | & 21
\end{bmatrix}
$$

<br>

#### Langkah 4: nolkan elemen di bawah pivot kolom 4
Operasi baris: $R_5 \leftarrow R_5 - 4R_4$

Penjelasan:
1. Pivot keempat ada di kolom 4 baris 4 (angka 1).
2. Di bawahnya (baris 5 kolom 4) ada angka 4.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan 4 kali baris 4 dari baris 5.

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & | & 1 \\
0 & 1 & 0 & 0 & 0 & | & 2 \\
0 & 0 & 1 & 0 & 0 & | & 3 \\
0 & 0 & 0 & 1 & 0 & | & 4 \\
0 & 0 & 0 & 0 & 1 & | & 5
\end{bmatrix}
$$

<br>

#### Hasil Akhir (Matriks Eselon Baris)
Karena matriks sudah membentuk matriks identitas (karena sistem ini bentuknya sangat sederhana), kita bisa langsung membaca solusinya dari kolom terakhir:
* $x_1 = 1$
* $x_2 = 2$
* $x_3 = 3$
* $x_4 = 4$
* $x_5 = 5$

![original image](https://cdn.mathpix.com/snip/images/QMGNgt072A_at8meIP895LnjyNsLn3PjmWo0dGz8-t0.original.fullsize.png)