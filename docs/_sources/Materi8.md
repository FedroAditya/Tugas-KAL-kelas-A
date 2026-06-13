**Google Colab | Penjelasan Lengkap Kode & Output**

> 🔗 **Link Notebook Colab:** [Buka di Google Colab](https://colab.research.google.com/drive/1mwvPe41DYtNWffLw7xmxVsxCTYTNWk4X?usp=sharing)

# Face Recognition Eigenface + SVD
**Penjelasan Lengkap Kode & Alur Kerja**

---

## 📁 Struktur Dataset
Berdasarkan struktur ekstraksi ZIP yang digunakan, dataset memiliki susunan folder seperti ini:

```text
dataset/
├── bahlil/
│   ├── bahlil (1).png/jpg
│   ├── BAHLIL.png/jpg
│   └── download.png/jpg
└── king nasir/
    ├── King nasir con camisa para mi amiga.png/jpg
    ├── King Nasir.png/jpg
    └── nasir.png/jpg

```

Terdapat **2 orang (kelas)** yaitu `bahlil` dan `king nasir`, masing-masing dengan **3 foto wajah** untuk data training. Total data = **6 gambar**.

---

## ⚙️ Tahap 1 — Setup, Import, dan Load Dataset

```python
!pip install opencv-python matplotlib scikit-learn -q
import cv2, os, zipfile, numpy as np, matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances

```

Program menggunakan `cv2` untuk manipulasi gambar, `numpy` untuk perhitungan matriks (SVD), `matplotlib` untuk visualisasi, dan modul `euclidean_distances` dari `scikit-learn` untuk menghitung kemiripan jarak antar wajah.

### Proses Load Dataset:

Fungsi `load_dataset(path)` melakukan *looping* ke setiap folder orang, membaca setiap gambar, dan melakukan 3 tahap *preprocessing* utama:

1. **Grayscale:** `cv2.IMREAD_GRAYSCALE` menyederhanakan gambar dengan membuang dimensi warna (hanya hitam-putih).
2. **Resize:** Menyeragamkan ukuran semua gambar menjadi `100x100` piksel.
3. **Flatten:** Mengubah matriks gambar 2D (100x100) menjadi *array* 1 dimensi (vektor) dengan **10.000 elemen**.

**Output dari Tahap 1:**

```text
Jumlah data training : 6
Ukuran matrix data (X) : (6, 10000)

```

Matrix `X` ini berisi 6 baris (merepresentasikan 6 gambar) dan 10.000 kolom (merepresentasikan nilai tiap piksel).

---

## 📊 Tahap 2 — Hitung Mean Face (Rata-rata Wajah)

```python
mean_face = np.mean(X, axis=0)

```

Di sini, program menghitung rata-rata nilai kecerahan pada *setiap piksel* dari seluruh ke-6 gambar *training*. Karena *array* berukuran 10.000, `mean_face` juga akan menghasilkan *array* 1D berisi 10.000 nilai rata-rata.

Fungsinya adalah mencari "pola wajah dasar" dari keseluruhan dataset sebelum mencari fitur pembeda dari tiap individu.

---

## 📊 Tahap 3 — Normalisasi Data (Matrix A)

```python
A = X - mean_face

```

Setiap nilai piksel pada gambar *training* dikurangi dengan nilai `mean_face`.

* Jika nilainya **positif**, piksel tersebut lebih terang dari rata-rata.
* Jika nilainya **negatif**, piksel tersebut lebih gelap dari rata-rata.

Tujuannya adalah memusatkan data (*center data*) di titik nol. Matrix `A` inilah yang benar-benar menyimpan informasi "perbedaan/keunikan" setiap wajah dari wajah rata-rata, dan siap dimasukkan ke dalam algoritma SVD.

---

## 🔢 Tahap 4 — SVD (Singular Value Decomposition)

```python
U, S, VT = np.linalg.svd(A, full_matrices=False)

```

Fungsi inti dari sistem ini. SVD memecah matrix `A` (6 x 10000) menjadi tiga matrix terpisah:

1. **Matrix U (6 x 6):** Vektor singular kiri. Tidak terlalu digunakan untuk tahapan proyeksi selanjutnya pada kode ini.
2. **Matrix S / Sigma (6,):** Berisi *Singular Values* yang otomatis diurutkan dari nilai terbesar ke terkecil. Nilai `S` mewakili seberapa besar "informasi" atau variasi yang ditangkap oleh masing-masing komponen.
3. **Matrix VT (6 x 10000):** Vektor singular kanan (*transpose*). **Setiap baris di VT adalah satu Eigenface.** Karena dataset ada 6 gambar, rank maksimalnya adalah 6. Jadi dihasilkan 6 baris Eigenface berukuran 10.000 piksel.

---

## 🖼️ Tahap 5 — Pemilihan & Visualisasi Eigenface

```python
k = 10
if k > len(VT):
    k = len(VT)
eigenfaces = VT[:k]

```

Target awalnya mengambil 10 Eigenface utama. Namun, karena ada validasi `if k > len(VT)`, dan total baris `VT` hanya 6, maka program otomatis menyesuaikan nilai `k = 6`.

Variabel `eigenfaces` sekarang berisi 6 fitur utama pengenalan wajah. Tiap vektor 1D di `eigenfaces` di-*reshape* kembali menjadi 100x100 dan diplot memakai `plt.imshow()`, menghasilkan gambar abstrak seperti bayangan wajah (*ghost faces*).

---

## 📐 Tahap 6 — Proyeksi Training ke Eigenspace

```python
projected_train = np.dot(A, eigenfaces.T)

```

Ini adalah langkah mengompresi data (*Dimensionality Reduction*). Alih-alih mengenali wajah berdasarkan 10.000 piksel, 6 gambar *training* awal (`A`) diubah (diproyeksikan) ke dalam "ruang eigenface".

* `A` berukuran (6 x 10000)
* `eigenfaces.T` berukuran (10000 x 6)
* Hasilnya `projected_train` berukuran **(6 x 6)**.

Sekarang, setiap 1 gambar wajah hanya direpresentasikan oleh **6 angka** saja (bobot komponen). Ini yang membuat pencarian menjadi sangat ringan dan cepat.

---

## 🧪 Tahap 7 — Input & Proyeksi Wajah Baru (Testing)

Saat gambar uji dimasukkan, gambar tersebut wajib melalui "jalur" *preprocessing* yang persis sama dengan data *training*:

```python
# 1. Load & Flatten jadi vektor (10.000,)
test_vector = test_img.flatten().astype(np.float32)

# 2. Normalisasi (Kurangi mean face)
test_normalized = test_vector - mean_face

# 3. Proyeksikan ke Eigenspace
projected_test = np.dot(test_normalized, eigenfaces.T)

```

Gambar *testing* yang awalnya berukuran 10.000 piksel kini berhasil diekstrak fiturnya menjadi hanya **1 baris array berisi 6 angka** (ukuran 1 x 6).

---

## 🎯 Tahap 8 — Hitung Jarak & Penentuan Hasil (Recognition)

```python
distances = euclidean_distances([projected_test], projected_train)
best_match_index = np.argmin(distances)
hasil = y[best_match_index]

```

Fungsi *library* `sklearn` bekerja di tahap akhir ini:

1. **`euclidean_distances`**: Menghitung jarak garis lurus (geometri) antara koordinat gambar *test* (6 angka) dengan keenam koordinat gambar *training*.
2. **`np.argmin(distances)`**: Mencari *index* (posisi data) yang nilai jaraknya **paling kecil**. Jarak terkecil berarti wajah tersebut adalah yang **paling mirip**.
3. **`y[best_match_index]`**: Memanggil label kelas (`bahlil` atau `king nasir`) pada *index* yang paling cocok tersebut untuk ditampilkan sebagai hasil akhir.

```

```