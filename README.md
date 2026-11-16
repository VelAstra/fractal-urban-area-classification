# Fractal Analysis for Urban Area Classification Suite

> **Proyek Capstone 6**: Klasifikasi Morfologi dan Kepadatan Wilayah Perkotaan Berbasis Analisis Fraktal Citra Satelit  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Memanfaatkan dimensi fraktal (*Box-Counting Fractal Dimension* dan *Radial Dimension*) untuk menganalisis kepadatan struktur bangunan dan kisi jalan dari citra penginderaan jauh satelit, guna mengklasifikasikan wilayah perkotaan padat (*dense urban*), pemukiman sub-urban (*suburban*), dan area pedesaan agrikultur (*rural*).

### Pembagian Tugas Tim 4 Mahasiswa
1. **Mahasiswa 1**: Satellite Tile Ingestion & Segmentasi Jejak Bangunan.
2. **Mahasiswa 2**: Ekstraksi Dimensi Fraktal Box-Counting & Dimensi Radial.
3. **Mahasiswa 3**: Modul Klasifikasi Morfologi Spasial & Pemetaan Zonasi.
4. **Mahasiswa 4**: Antarmuka Grafis (Tkinter GUI), Visualisasi Peta Kepadatan, & Evaluasi Metrik.

---

## Cara Menjalankan

```bash
# Menjalankan klasifikasi zona pada tile satelit
python cli.py classify sample_data/tile_dense_urban.png

# Menjalankan antarmuka grafis
python cli.py gui

# Menjalankan uji otomatis
python -m unittest discover tests
```
