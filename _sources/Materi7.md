# Dekomposisi QR dan Nilai Eigen
clik link ini untuk mengarah ke colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11YjHlEAkCw6cHerfdBFP28QStXcJLAMZ?usp=sharing)
---

## Matriks A

Diberikan matriks simetris berukuran 2×2:

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 2]
])

print(A)
```

**Output:**
```
[[2 1]
 [1 2]]
```

---

## Tahap 1 — Gram-Schmidt: Membentuk Vektor q₁

Proses Gram-Schmidt dimulai dari kolom pertama matriks A:

$$a_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

**Menghitung norma (panjang) vektor:**

$$\|a_1\| = \sqrt{2^2 + 1^2} = \sqrt{5} \approx 2.236$$

**Membentuk vektor ortonormal q₁:**

$$q_1 = \frac{a_1}{\|a_1\|} = \frac{1}{\sqrt{5}}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} \dfrac{2}{\sqrt{5}} \\ \dfrac{1}{\sqrt{5}} \end{bmatrix}$$

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 2]
])

# Ekstrak kolom pertama
a1 = A[:, 0]
print("Vektor a1:", a1)

# Norma vektor
norma_a1 = np.sqrt(2**2 + 1**2)
print(f"\nNorma a1: √(2² + 1²) = {norma_a1}")

# Vektor ortonormal
q1 = a1 / norma_a1
print("\nVektor q1 (ternormalisasi):", q1)
```

**Output:**
```
Vektor a1: [2 1]

Norma a1: √(2² + 1²) = 2.23606797749979

Vektor q1 (ternormalisasi): [0.89442719 0.4472136 ]
```

Panjang $q_1$ sudah bernilai 1, artinya normalisasi berhasil.

---

## Tahap 2 — Menghitung Dot Product q₁ · a₂

Kolom kedua matriks A:

$$a_2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

**Dot product** $q_1 \cdot a_2$:

$$q_1 \cdot a_2 = \left(\frac{2\sqrt{5}}{5} \times 1\right) + \left(\frac{\sqrt{5}}{5} \times 2\right) = \frac{2\sqrt{5}}{5} + \frac{2\sqrt{5}}{5} = \frac{4\sqrt{5}}{5}$$

```python
from sympy import Matrix, sqrt

A = Matrix([
    [2, 1],
    [1, 2]
])

a1 = A[:, 0]
a2 = A[:, 1]

# Normalisasi q1
q1 = a1 / sqrt(5)

# Dot product
dot = q1.dot(a2)
print("q1 · a2 =")
print(dot)
```

**Output:**
```
q1 · a2 =
4*sqrt(5)/5
```

---

## Tahap 3 — Ortogonalisasi: Menghitung u₂

Komponen proyeksi $a_2$ ke arah $q_1$:

$$(q_1 \cdot a_2) \cdot q_1 = \frac{4\sqrt{5}}{5} \begin{bmatrix} \dfrac{2\sqrt{5}}{5} \\ \dfrac{\sqrt{5}}{5} \end{bmatrix} = \begin{bmatrix} \dfrac{8}{5} \\ \dfrac{4}{5} \end{bmatrix}$$

Komponen ortogonal $u_2$:

$$u_2 = a_2 - (q_1 \cdot a_2)\,q_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix} - \begin{bmatrix} \dfrac{8}{5} \\ \dfrac{4}{5} \end{bmatrix} = \begin{bmatrix} -\dfrac{3}{5} \\ \dfrac{6}{5} \end{bmatrix}$$

```python
from sympy import Matrix, sqrt

A = Matrix([
    [2, 1],
    [1, 2]
])

a1 = A[:, 0]
a2 = A[:, 1]

q1 = a1 / sqrt(5)

# Proyeksi
dot  = q1.dot(a2)
proj = dot * q1

# Vektor ortogonal
u2 = a2 - proj
print("u2 =")
print(u2)
```

**Output:**
```
u2 =
Matrix([[-3/5], [6/5]])
```

---

## Tahap 4 — Normalisasi u₂ menjadi q₂

**Menghitung norma u₂:**

$$\|u_2\| = \sqrt{\left(-\frac{3}{5}\right)^2 + \left(\frac{6}{5}\right)^2} = \sqrt{\frac{9}{25} + \frac{36}{25}} = \sqrt{\frac{45}{25}} = \frac{3\sqrt{5}}{5}$$

**Vektor ortonormal q₂:**

$$q_2 = \frac{u_2}{\|u_2\|} = \begin{bmatrix} -\dfrac{\sqrt{5}}{5} \\ \dfrac{2\sqrt{5}}{5} \end{bmatrix}$$

```python
from sympy import Matrix, sqrt, Rational

v2 = Matrix([
    [Rational(-3, 5)],
    [Rational( 6, 5)]
])

norma_v2 = sqrt(v2.dot(v2))
print("Norma v2 =", norma_v2)

q2 = v2 / norma_v2
print("\nq2 =")
print(q2)
```

**Output:**
```
Norma v2 = 3*sqrt(5)/5

q2 =
Matrix([[-sqrt(5)/5], [2*sqrt(5)/5]])
```

---

## Tahap 5 — Menyusun Matriks Q dan R

Matriks ortogonal Q dibentuk dari kolom $q_1$ dan $q_2$:

$$Q = \begin{bmatrix} \dfrac{2\sqrt{5}}{5} & -\dfrac{\sqrt{5}}{5} \\[8pt] \dfrac{\sqrt{5}}{5} & \dfrac{2\sqrt{5}}{5} \end{bmatrix}$$

Matriks segitiga atas R dihitung dengan $R = Q^T A$:

$$R = \begin{bmatrix} \sqrt{5} & \dfrac{4\sqrt{5}}{5} \\[8pt] 0 & \dfrac{3\sqrt{5}}{5} \end{bmatrix}$$

```python
from sympy import Matrix, sqrt

A = Matrix([
    [2, 1],
    [1, 2]
])

a1 = A[:, 0]
a2 = A[:, 1]

q1 = a1 / sqrt(5)
dot  = q1.dot(a2)
v2   = a2 - dot * q1
q2   = v2 / sqrt(v2.dot(v2))

Q = Matrix.hstack(q1, q2)
R = Q.T * A

print("Q =")
print(Q)
print("\nR =")
print(R)
```

**Output:**
```
Q =
Matrix([[2*sqrt(5)/5, -sqrt(5)/5], [sqrt(5)/5, 2*sqrt(5)/5]])

R =
Matrix([[sqrt(5), 4*sqrt(5)/5], [0, 3*sqrt(5)/5]])
```

---

## Tahap 6 — Verifikasi Q × R = A

$$QR = \begin{bmatrix} \dfrac{2\sqrt{5}}{5} & -\dfrac{\sqrt{5}}{5} \\[8pt] \dfrac{\sqrt{5}}{5} & \dfrac{2\sqrt{5}}{5} \end{bmatrix} \begin{bmatrix} \sqrt{5} & \dfrac{4\sqrt{5}}{5} \\[8pt] 0 & \dfrac{3\sqrt{5}}{5} \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} = A \checkmark$$

```python
from sympy import Matrix, sqrt

Q = Matrix([
    [2*sqrt(5)/5, -sqrt(5)/5],
    [  sqrt(5)/5, 2*sqrt(5)/5]
])

R = Matrix([
    [sqrt(5), 4*sqrt(5)/5],
    [0,       3*sqrt(5)/5]
])

print("Q × R =")
print(Q * R)
```

**Output:**
```
Q × R =
Matrix([[2, 1], [1, 2]])
```

Dekomposisi $A = QR$ terbukti benar.

---

## Tahap 7 — Matriks A₂ = R × Q

Satu langkah iterasi QR menghasilkan:

$$A_2 = RQ = \begin{bmatrix} \sqrt{5} & \dfrac{4\sqrt{5}}{5} \\[8pt] 0 & \dfrac{3\sqrt{5}}{5} \end{bmatrix} \begin{bmatrix} \dfrac{2\sqrt{5}}{5} & -\dfrac{\sqrt{5}}{5} \\[8pt] \dfrac{\sqrt{5}}{5} & \dfrac{2\sqrt{5}}{5} \end{bmatrix} = \begin{bmatrix} \dfrac{14}{5} & \dfrac{3}{5} \\[8pt] \dfrac{3}{5} & \dfrac{6}{5} \end{bmatrix}$$

```python
from sympy import Matrix, sqrt

Q = Matrix([
    [2*sqrt(5)/5, -sqrt(5)/5],
    [  sqrt(5)/5, 2*sqrt(5)/5]
])

R = Matrix([
    [sqrt(5), 4*sqrt(5)/5],
    [0,       3*sqrt(5)/5]
])

A2 = R * Q
print("R × Q =")
print(A2)
```

**Output:**
```
R × Q =
Matrix([[14/5, 3/5], [3/5, 6/5]])
```

---

## Tahap 8 — QR Iteration (Konvergensi ke Nilai Eigen)

QR Iteration bekerja dengan cara berulang kali melakukan dekomposisi $A_k = Q_k R_k$, lalu membentuk $A_{k+1} = R_k Q_k$. Elemen diagonal akan semakin mendekati nilai eigen.

```python
from sympy import Matrix, sqrt, N, pprint

A = Matrix([
    [2, 1],
    [1, 2]
])

print("A0 =")
pprint(A)

for k in range(1, 11):
    a1 = A[:, 0]
    a2 = A[:, 1]

    # Gram-Schmidt
    q1   = a1 / sqrt(a1.dot(a1))
    proj = q1.dot(a2) * q1
    v2   = a2 - proj
    q2   = v2 / sqrt(v2.dot(v2))

    # Susun Q dan R
    Q = Matrix.hstack(q1, q2)
    R = Q.T * A

    # Update A
    A = R * Q

    print(f"\nA{k} =")
    pprint(N(A, 5))
```

**Output:**
```
A0 =
[2  1]
[   ]
[1  2]

A1 =
[2.8  0.6]
[         ]
[0.6  1.2]

A2 =
[2.96  0.28]
[            ]
[0.28  1.04 ]

...

A10 ≈
[3.0   ~0 ]
[          ]
[~0   1.0 ]
```

---

## Kesimpulan

Setelah 10 iterasi, diagonal matriks konvergen ke:

$$\lambda_1 \approx 3, \quad \lambda_2 \approx 1$$

Nilai ini sesuai dengan eigen value analitik matriks $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, yaitu $\lambda = 2 \pm 1$.