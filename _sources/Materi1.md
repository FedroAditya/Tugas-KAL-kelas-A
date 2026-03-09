# Tugas Eliminasi Gaussan

## 1. SPL (Sistem Persamaan Linear)

$$
\begin{cases}
2x_1 + 3x_2 + x_3 + 4x_4 + 2x_5 = 37 \\
x_1 + 4x_2 + 2x_3 + x_4 + 3x_5 = 34 \\
3x_1 + x_2 + 5x_3 + 2x_4 + x_5 = 33 \\
4x_1 + 2x_2 + 3x_3 + 5x_4 + x_5 = 42 \\
x_1 + 5x_2 + x_3 + 3x_4 + 4x_5 = 46
\end{cases}
$$

## 2. Matriks Augmented

$$
\left[
\begin{array}{ccccc|c}
2 & 3 & 1 & 4 & 2 & 37 \\
1 & 4 & 2 & 1 & 3 & 34 \\
3 & 1 & 5 & 2 & 1 & 33 \\
4 & 2 & 3 & 5 & 1 & 42 \\
1 & 5 & 1 & 3 & 4 & 46
\end{array}
\right]
$$

## 3. Eliminasi Gauss (OBE)

### Langkah 1: Jadikan pivot kolom 1 menjadi 1
**Operasi baris:** $R_1 \leftarrow \frac{1}{2}R_1$

**Penjelasan:** Pivot pertama berada di baris 1, kolom 1 (angka 2). Agar mudah digunakan untuk eliminasi, kita jadikan nilainya 1 dengan mengalikan baris pertama dengan $\frac{1}{2}$.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
1 & 4 & 2 & 1 & 3 & 34 \\
3 & 1 & 5 & 2 & 1 & 33 \\
4 & 2 & 3 & 5 & 1 & 42 \\
1 & 5 & 1 & 3 & 4 & 46 \\
\end{array}
\right]
$$

### Langkah 2: Nolkan elemen di bawah pivot kolom 1
**Operasi baris:**
* $R_2 \leftarrow R_2 - 1R_1$
* $R_3 \leftarrow R_3 - 3R_1$
* $R_4 \leftarrow R_4 - 4R_1$
* $R_5 \leftarrow R_5 - 1R_1$

**Penjelasan:** Kita akan membuat angka di bawah pivot pertama menjadi 0. Kita operasikan baris ke-2 hingga ke-5 dengan mengurangkan kelipatan dari baris pertama.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 5/2 & 3/2 & -1 & 2 & 31/2 \\
0 & -7/2 & 7/2 & -4 & -2 & -45/2 \\
0 & -4 & 1 & -3 & -3 & -32 \\
0 & 7/2 & 1/2 & 1 & 3 & 55/2 \\
\end{array}
\right]
$$

### Langkah 3: Jadikan pivot kolom 2 menjadi 1
**Operasi baris:** $R_2 \leftarrow \frac{2}{5}R_2$

**Penjelasan:** Lanjut ke kolom 2. Pivot ada di baris 2 (angka $5/2$). Kita kalikan baris ke-2 dengan kebalikannya yaitu $\frac{2}{5}$ agar menjadi 1.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & -7/2 & 7/2 & -4 & -2 & -45/2 \\
0 & -4 & 1 & -3 & -3 & -32 \\
0 & 7/2 & 1/2 & 1 & 3 & 55/2 \\
\end{array}
\right]
$$

### Langkah 4: Nolkan elemen di bawah pivot kolom 2
**Operasi baris:**
* $R_3 \leftarrow R_3 + \frac{7}{2}R_2$
* $R_4 \leftarrow R_4 + 4R_2$
* $R_5 \leftarrow R_5 - \frac{7}{2}R_2$

**Penjelasan:** Kita nolkan elemen pada baris 3, 4, dan 5 di kolom 2 menggunakan patokan baris ke-2 yang sudah disederhanakan.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 28/5 & -27/5 & 4/5 & -4/5 \\
0 & 0 & 17/5 & -23/5 & 1/5 & -36/5 \\
0 & 0 & -8/5 & 12/5 & 1/5 & 29/5 \\
\end{array}
\right]
$$

### Langkah 5: Jadikan pivot kolom 3 menjadi 1
**Operasi baris:** $R_3 \leftarrow \frac{5}{28}R_3$

**Penjelasan:** Lanjut ke kolom 3. Pivot ada di baris 3 (angka $28/5$). Kita jadikan 1 dengan mengalikannya dengan $\frac{5}{28}$.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 1 & -27/28 & 1/7 & -1/7 \\
0 & 0 & 17/5 & -23/5 & 1/5 & -36/5 \\
0 & 0 & -8/5 & 12/5 & 1/5 & 29/5 \\
\end{array}
\right]
$$

### Langkah 6: Nolkan elemen di bawah pivot kolom 3
**Operasi baris:**
* $R_4 \leftarrow R_4 - \frac{17}{5}R_3$
* $R_5 \leftarrow R_5 + \frac{8}{5}R_3$

**Penjelasan:** Kita nolkan elemen pada baris 4 dan 5 di kolom ke-3 menggunakan patokan baris ke-3.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 1 & -27/28 & 1/7 & -1/7 \\
0 & 0 & 0 & -37/28 & -2/7 & -47/7 \\
0 & 0 & 0 & 6/7 & 3/7 & 39/7 \\
\end{array}
\right]
$$

### Langkah 7: Jadikan pivot kolom 4 menjadi 1
**Operasi baris:** $R_4 \leftarrow -\frac{28}{37}R_4$

**Penjelasan:** Pivot ke-4 ada di baris 4 (angka $-37/28$). Kita kalikan baris 4 dengan kebalikannya yaitu $-\frac{28}{37}$ agar menjadi 1.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 1 & -27/28 & 1/7 & -1/7 \\
0 & 0 & 0 & 1 & 8/37 & 188/37 \\
0 & 0 & 0 & 6/7 & 3/7 & 39/7 \\
\end{array}
\right]
$$

### Langkah 8: Nolkan elemen di bawah pivot kolom 4
**Operasi baris:** $R_5 \leftarrow R_5 - \frac{6}{7}R_4$

**Penjelasan:** Kita nolkan satu-satunya elemen tersisa di bawah pivot ke-4 (pada baris ke-5).

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 1 & -27/28 & 1/7 & -1/7 \\
0 & 0 & 0 & 1 & 8/37 & 188/37 \\
0 & 0 & 0 & 0 & 9/37 & 45/37 \\
\end{array}
\right]
$$

### Langkah 9: Jadikan pivot kolom 5 menjadi 1
**Operasi baris:** $R_5 \leftarrow \frac{37}{9}R_5$

**Penjelasan:** Sebagai tahap terakhir untuk eselon baris, jadikan elemen ujung pada baris 5 kolom 5 menjadi 1 dengan mengalikannya dengan kebalikannya yaitu $\frac{37}{9}$.

$$
\left[
\begin{array}{ccccc|c}
1 & 3/2 & 1/2 & 2 & 1 & 37/2 \\
0 & 1 & 3/5 & -2/5 & 4/5 & 31/5 \\
0 & 0 & 1 & -27/28 & 1/7 & -1/7 \\
0 & 0 & 0 & 1 & 8/37 & 188/37 \\
0 & 0 & 0 & 0 & 1 & 5 \\
\end{array}
\right]
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