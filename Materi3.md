# Laporan Refleksi Geometri
## Pencerminan Titik terhadap Sumbu X dan Sumbu Y

---

## 🔗 Demo Interaktif
clik link ini untuk mengarah ke colab

[![Open In Colab](https://colab.research.google.com/drive/1FDJRB4oR3z_4xqgwWDbaixOl96mhPCF9?usp=sharing)]

> **Cara pakai:** Klik badge di atas → Colab terbuka → Jalankan cell → UI langsung muncul.

---

## 1. Pengertian Refleksi

Refleksi (pencerminan) adalah transformasi geometri yang memindahkan setiap titik pada suatu bidang ke posisi baru dengan cara mencerminkannya terhadap suatu garis sumbu. Hasil refleksi memiliki jarak yang sama terhadap sumbu cermin, tetapi berada di sisi yang berlawanan.

> **Analogi:** Bayangkan kamu berdiri di depan cermin. Bayangan kamu berada di jarak yang sama dengan jarak kamu ke cermin, tetapi di sisi yang berlawanan.

---

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

---

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

---

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
- Nilai **x dibalik tandanya** — titik berpindah melewati sumbu Y secara horizontal
- Jarak titik ke sumbu Y **tetap sama**

### Ilustrasi Pergeseran

```
Y
^
4 | *(-4,4)-*(-2,4)      *(2,4)--*(4,4)
  |  |       |           |        |
2 | *(-4,2)-*(-2,2)      *(2,2)--*(4,2)
  |                  |
--+------------------+-----------------> X
     refleksi Y (merah)       asal (biru)
```

### Contoh Perhitungan

| Titik | Koordinat Asal | Proses | Hasil Refleksi Y |
|-------|---------------|--------|-----------------|
| Titik 1 | (2, 2) | x: 2 → −2 | (−2, 2) |
| Titik 2 | (4, 2) | x: 4 → −4 | (−4, 2) |
| Titik 3 | (4, 4) | x: 4 → −4 | (−4, 4) |
| Titik 4 | (2, 4) | x: 2 → −2 | (−2, 4) |

---

## 5. Perbandingan Refleksi X dan Refleksi Y

| Aspek | Refleksi Sumbu X | Refleksi Sumbu Y |
|-------|-----------------|-----------------|
| Sumbu cermin | Garis horizontal (y = 0) | Garis vertikal (x = 0) |
| Matriks | `[[1,0],[0,-1]]` | `[[-1,0],[0,1]]` |
| Koordinat yang berubah | Nilai y (dibalik) | Nilai x (dibalik) |
| Koordinat yang tetap | Nilai x | Nilai y |
| Arah pergeseran | Vertikal (atas ↔ bawah) | Horizontal (kiri ↔ kanan) |
| Determinan matriks | −1 | −1 |

> **Catatan:** Determinan = −1 menandakan refleksi membalik orientasi bangun (searah jarum jam menjadi berlawanan arah jarum jam).

---

## 6. Sifat-Sifat Refleksi

1. **Isometri** — Jarak antar titik tidak berubah. Bangun hasil refleksi kongruen (sama bentuk dan ukuran) dengan bangun asalnya.

2. **Orientasi terbalik** — Urutan titik searah jarum jam pada bangun asal menjadi berlawanan arah jarum jam pada hasil refleksi.

3. **Refleksi dua kali = Identitas** — Merefleksikan dua kali terhadap sumbu yang sama mengembalikan titik ke posisi asal:
   ```
   M_x × M_x = I  →  (x, y) → (x, -y) → (x, y)
   ```

4. **Refleksi X lalu Y = Rotasi 180°** — Merefleksikan terhadap sumbu X kemudian Y menghasilkan rotasi setengah putaran:
   ```
   M_y × M_x = | -1   0 |  ← matriks rotasi 180°
               |  0  -1 |
   ```

5. **Titik pada sumbu tidak berpindah** — Titik tepat di sumbu X (y=0) tidak berubah saat refleksi X, begitu pula sebaliknya.

---

## 7. Implementasi Program

Program dibuat menggunakan **Python** dengan dua versi:

| Versi | Library | Environment |
|-------|---------|-------------|
| Desktop | Tkinter + Matplotlib | Lokal (laptop) |
| Cloud | ipywidgets + Matplotlib | Google Colab |

### Kode Inti Refleksi

```python
# Menghitung koordinat hasil refleksi
ref_x = [(x, -y) for x, y in points]   # Refleksi terhadap sumbu X
ref_y = [(-x, y) for x, y in points]   # Refleksi terhadap sumbu Y
```

### Cara Kerja Animasi

Animasi menggunakan **interpolasi linear** — titik bergerak dari posisi asal ke posisi refleksi selama 40 frame:

```python
t = frame / 40          # t bergerak dari 0.0 → 1.0
xt = x0 + (x1 - x0) * t   # posisi x sementara
yt = y0 + (y1 - y0) * t   # posisi y sementara
```

| Frame | t | Posisi sementara (target (2, −2)) |
|-------|---|----------------------------------|
| 0  | 0.00 | (2.0, 2.0) — posisi awal |
| 10 | 0.25 | (2.0, 1.0) — seperempat jalan |
| 20 | 0.50 | (2.0, 0.0) — tepat di sumbu X |
| 30 | 0.75 | (2.0, −1.0) — tiga perempat |
| 40 | 1.00 | (2.0, −2.0) — posisi refleksi |

### Fitur Program

- Input 4 titik koordinat (x, y) secara manual
- Tombol **Tampilkan** — menggambar bangun asal
- Tombol **Refleksi X** — animasi pencerminan ke sumbu X
- Tombol **Refleksi Y** — animasi pencerminan ke sumbu Y
- Toggle layer — show/hide masing-masing bangun
- Tabel koordinat — menampilkan semua titik asal dan hasil refleksi
- Tombol **Contoh** — mengisi input otomatis dengan kotak (2,2)–(4,4)
- Tombol **Hapus** — reset semua input dan grafik

---

## 8. Kesimpulan

Refleksi geometri adalah operasi pencerminan yang mengubah posisi titik dengan aturan sederhana berbasis matriks transformasi linear:

- **Refleksi sumbu X** → Matriks `[[1,0],[0,-1]]` → balik nilai y: `(x, y) → (x, −y)`
- **Refleksi sumbu Y** → Matriks `[[-1,0],[0,1]]` → balik nilai x: `(x, y) → (−x, y)`

Bangun yang dihasilkan selalu **kongruen** dengan bangun asalnya — sama bentuk dan ukuran, hanya posisinya yang tercermin. Jarak setiap titik ke sumbu cermin selalu terjaga sama antara titik asal dan titik hasil refleksi.

--- 
*Demo interaktif: [![Open In Colab](https://colab.research.google.com/drive/1Lz38CM2TZ-KhdKLYer2dtQ_u4aGe6XMO?usp=sharing)