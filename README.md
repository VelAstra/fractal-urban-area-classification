# Fractal Analysis for Urban Area Classification Suite

> **Proyek Capstone 6**: Klasifikasi Morfologi dan Kepadatan Wilayah Perkotaan Berbasis Analisis Fraktal Citra Satelit  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Memanfaatkan dimensi fraktal (*Box-Counting Fractal Dimension* dan *Radial Dimension*) untuk menganalisis kepadatan struktur bangunan dan kisi jalan dari citra penginderaan jauh satelit, guna mengklasifikasikan wilayah perkotaan padat (*dense urban*), pemukiman sub-urban (*suburban*), dan area pedesaan agrikultur (*rural*).

### Pembagian Tugas Tim (2 Mahasiswa)
1. **Aji Kusuma Putra** (`22/503701/PA/21657`): Ingestion ubin satelit, ekstraksi jejak kontur buatan manusia, mesin analisis fraktal box-counting, dan analisis dimensi radial. (Modul: `sample_data/generate_satellite_tiles.py`, `core/fractal_analyzer.py`).
2. **Rayhan Haldi Hermawan** (`24/545406/PA/23176`): Klasifikasi zonasi morfologi perkotaan (Dense Urban, Suburban, Rural), pemetaan ambang densitas, Desktop GUI Tkinter, integrasi CLI, visualisasi peta panas kepadatan kota, dan evaluasi metrik. (Modul: `core/classifier.py`, `core/evaluation.py`, `gui/app.py`, `cli.py`).

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
