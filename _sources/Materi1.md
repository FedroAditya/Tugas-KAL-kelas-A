## 1. SPL (Sistem Persamaan Linear)

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 + x_5 = 15 \\
x_1 + 2x_2 + 2x_3 + 2x_4 + 2x_5 = 29 \\
x_1 + 2x_2 + 3x_3 + 3x_4 + 3x_5 = 41 \\
x_1 + 2x_2 + 3x_3 + 4x_4 + 4x_5 = 50 \\
x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 = 55
\end{cases}
$$

## 2. Matriks Augmented

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
1 & 2 & 2 & 2 & 2 & 29 \\
1 & 2 & 3 & 3 & 3 & 41 \\
1 & 2 & 3 & 4 & 4 & 50 \\
1 & 2 & 3 & 4 & 5 & 55
\end{array}
\right]
$$

## 3. Eliminasi Gauss (OBE)

**Matriks Augmented Awal:** $$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
1 & 2 & 2 & 2 & 2 & 29 \\
1 & 2 & 3 & 3 & 3 & 41 \\
1 & 2 & 3 & 4 & 4 & 50 \\
1 & 2 & 3 & 4 & 5 & 55
\end{array}
\right]
$$

### Langkah 1: nolkan elemen di bawah pivot kolom 1

Operasi baris: $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, $R_4 \leftarrow R_4 - R_1$, $R_5 \leftarrow R_5 - R_1$

Penjelasan:
1. Pivot pertama ada di kolom 1 baris 1 (angka 1).
2. Di bawahnya (baris 2, 3, 4, dan 5 kolom 1) semuanya ada angka 1.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan baris 1 dari baris 2, 3, 4, dan 5.

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 1 & 1 & 1 & 14 \\
0 & 1 & 2 & 2 & 2 & 26 \\
0 & 1 & 2 & 3 & 3 & 35 \\
0 & 1 & 2 & 3 & 4 & 40
\end{array}
\right]
$$

### Langkah 2: nolkan elemen di bawah pivot kolom 2

Operasi baris: $R_3 \leftarrow R_3 - R_2$, $R_4 \leftarrow R_4 - R_2$, $R_5 \leftarrow R_5 - R_2$

Penjelasan:
1. Pivot kedua ada di kolom 2 baris 2 (angka 1).
2. Di bawahnya (baris 3, 4, dan 5 kolom 2) semuanya ada angka 1.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan baris 2 dari baris 3, 4, dan 5.

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 1 & 1 & 1 & 14 \\
0 & 0 & 1 & 1 & 1 & 12 \\
0 & 0 & 1 & 2 & 2 & 21 \\
0 & 0 & 1 & 2 & 3 & 26
\end{array}
\right]
$$

### Langkah 3: nolkan elemen di bawah pivot kolom 3

Operasi baris: $R_4 \leftarrow R_4 - R_3$, $R_5 \leftarrow R_5 - R_3$

Penjelasan:
1. Pivot ketiga ada di kolom 3 baris 3 (angka 1).
2. Di bawahnya (baris 4 dan 5 kolom 3) ada angka 1.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan baris 3 dari baris 4 dan 5.

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 1 & 1 & 1 & 14 \\
0 & 0 & 1 & 1 & 1 & 12 \\
0 & 0 & 0 & 1 & 1 & 9 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

### Langkah 4: nolkan elemen di bawah pivot kolom 4

Operasi baris: $R_5 \leftarrow R_5 - R_4$

Penjelasan:
1. Pivot keempat ada di kolom 4 baris 4 (angka 1).
2. Di bawahnya (baris 5 kolom 4) ada angka 1.
3. Kita ingin membuat elemen tersebut menjadi 0.
4. Caranya dengan mengurangkan baris 4 dari baris 5.

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

### 5. Lanjutan: Eliminasi Gauss-Jordan (Mengnolkan elemen di atas pivot)

Setelah mendapatkan Matriks Eselon Baris, kita nolkan elemen di atas setiap pivot:

**Langkah 5:** Nolkan elemen di atas pivot kolom 5 ($R_4-R_5, R_3-R_5, R_2-R_5, R_1-R_5$)
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

**Langkah 6:** Nolkan elemen di atas pivot kolom 4 ($R_3-R_4, R_2-R_4, R_1-R_4$)
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

**Langkah 7:** Nolkan elemen di atas pivot kolom 3 ($R_2-R_3, R_1-R_3$)
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

**Langkah 8:** Nolkan elemen di atas pivot kolom 2 ($R_1-R_2$)
**Matriks Eselon Baris Terreduksi:**
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

### Hasil Akhir (Gauss-Jordan):
Dari matriks di atas, kita langsung mendapatkan:
$x_1 = 1$, $x_2 = 2$, $x_3 = 3$, $x_4 = 4$, $x_5 = 5$.

## SAGE CELL
![original image](https://cdn.mathpix.com/snip/images/9NrdItnsMwNfPd79vcynviSdvuHconiQ6djYwgQqlRU.original.fullsize.png)
![original image](https://cdn.mathpix.com/snip/images/q3EyFKmPej_8BdP-1PUZDw2VKU1PGpULSioEuwmCiKI.original.fullsize.png)