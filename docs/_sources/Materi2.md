## A. Determinan

### 1
Matriks 2x2, pakai rumus cepat ad - bc

$$
A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}
$$

$$
\det(A) = (-7)(4) - (-5)(1) = -28 + 5 = -23
$$

---

### 2
Ekspansi baris pertama

$$
A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}
$$

Baris pertama: [0, 2, -3]

$$
\det(A) = 0 - 2(1 \cdot 1 - (-1)\cdot0) + (-3)(1\cdot0 - (-2)\cdot0)
$$

$$
= -2(1) + (-3)(0) = -2
$$

---

### 3
Baris saling bergantung

$$
A = \begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

Terlihat pola simetris dan tidak independen

$$
\det(A) = 0
$$

---

## B. Invers Matriks

Syarat: determinan tidak boleh 0

---

### 4
Gunakan rumus invers 2x2

$$
A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{-23}
\begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
-4/23 & -5/23 \\
1/23 & 7/23
\end{bmatrix}
$$

---

### 5
Determinan tidak nol, jadi bisa diinvers

$$
A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}
$$

$$
\det(A) = -2
$$

$$
A^{-1} =
\begin{bmatrix}
-1 & -1 & -5/2 \\
-1/2 & 0 & -3/2 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### 6
Determinan nol

$$
\det(A) = 0
$$

Tidak memenuhi syarat invers

$$
\text{Matriks tidak memiliki invers}
$$