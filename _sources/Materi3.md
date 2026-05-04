# Laporan Refleksi Geometri
## Pencerminan Titik terhadap Sumbu X dan Sumbu Y

## 🔗 Demo Interaktif
clik link ini untuk mengarah ke colab

[![Open In Colab](https://colab.research.google.com/drive/1FDJRB4oR3z_4xqgwWDbaixOl96mhPCF9?usp=sharing)]

> **Cara pakai:** Klik badge di atas → Colab terbuka → Jalankan cell → UI langsung muncul.

***

## 1. Pengertian Refleksi

Refleksi (pencerminan) adalah transformasi geometri yang memindahkan setiap titik pada suatu bidang ke posisi baru dengan cara mencerminkannya terhadap suatu garis sumbu. Hasil refleksi memiliki jarak yang sama terhadap sumbu cermin, tetapi berada di sisi yang berlawanan.

> **Analogi:** Bayangkan kamu berdiri di depan cermin. Bayangan kamu berada di jarak yang sama dengan jarak kamu ke cermin, tetapi di sisi yang berlawanan.

***

## 2. Refleksi sebagai Transformasi Linear (Matriks)

Secara matematis, refleksi adalah **transformasi linear** yang direpresentasikan sebagai perkalian matriks. Setiap titik ditulis sebagai vektor kolom:

```
     | x |
P =  |   |
     | y |
```

Transformasi dilakukan dengan:

```
P' = M × P
```

***

## 3. Refleksi terhadap Sumbu X

### Matriks Refleksi X

```
        |  1   0 |
M_x  =  |        |
        |  0  -1 |
```

### Rumus

```
(x, y)  →  (x, -y)
```

### Cara Kerja Pergeseran

```
| x' |   |  1   0 | | x |   |  x  |
|    | = |        | |   | = |     |
| y' |   |  0  -1 | | y |   | -y  |
```

- Nilai **x tidak berubah** — titik tetap di kolom vertikal yang sama
- Nilai **y dibalik tandanya** — titik berpindah melewati sumbu X secara vertikal
- Jarak titik ke sumbu X **tetap sama**

### Ilustrasi Pergeseran

```
Y
^
4 |  *(2,4)--*(4,4)     ← titik asal (biru)
  |  |        |
2 |  *(2,2)--*(4,2)
  |
--+----------------------------> X
  |
-2|  *(2,-2)-*(4,-2)    ← hasil refleksi X (hijau)
  |  |        |
-4|  *(2,-4)-*(4,-4)
```

### Contoh Perhitungan

| Titik | Koordinat Asal | Proses | Hasil Refleksi X |
|-------|---------------|--------|-----------------|
| Titik 1 | (2, 2) | y: 2 → −2 | (2, −2) |
| Titik 2 | (4, 2) | y: 2 → −2 | (4, −2) |
| Titik 3 | (4, 4) | y: 4 → −4 | (4, −4) |
| Titik 4 | (2, 4) | y: 4 → −4 | (2, −4) |

***

## 4. Refleksi terhadap Sumbu Y

### Matriks Refleksi Y

```
        | -1   0 |
M_y  =  |        |
        |  0   1 |
```

### Rumus

```
(x, y)  →  (-x, y)
```

### Cara Kerja Pergeseran

```
| x' |   | -1   0 | | x |   | -x |
|    | = |        | |   | = |    |
| y' |   |  0   1 | | y |   |  y |
```

- Nilai **y tidak berubah** — titik tetap di baris horizontal yang sama
