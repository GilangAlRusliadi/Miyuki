# Miyuki GUI (Gradio Version)

Miyuki GUI (Gradio Version) adalah antarmuka berbasis web untuk mengunduh video menggunakan modul **Miyuki**, terinspirasi dari [Miyuki-WebGUI](https://github.com/cailurus/Miyuki-WebGUI). Proyek ini menggunakan **Gradio** sebagai framework untuk memberikan pengalaman pengguna yang lebih ringan dan cepat dalam mengunduh video dari berbagai sumber.

## Features

- **Antarmuka Sederhana**: UI berbasis **Gradio** untuk memasukkan URL video dan mengelola unduhan dengan mudah.
- **Proses Unduhan Real-Time**: Menampilkan progress setiap unduhan secara langsung di UI.
- **Dukungan Banyak Tugas**: Memungkinkan pengunduhan beberapa video secara berurutan.
- **Penyimpanan Lokal**: Video yang diunduh disimpan langsung ke sistem pengguna.

## Requirements

- Python 3.7 atau lebih tinggi
- `ffmpeg` (wajib untuk pengolahan video)
- `requirements.txt` untuk dependensi yang diperlukan

## Installation

1. **Clone repository**:
   ```bash
   git clone https://github.com/GilangAlRusliadi/Miyuki.git
   cd Miyuki
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install ffmpeg** (jika belum tersedia di sistem):
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`
   - **Windows**: Download dari [ffmpeg.org](https://ffmpeg.org/)

## Usage

1. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```
   Akses UI di browser melalui `http://localhost:7860`

2. **Unduh Video**:
   - Masukkan URL video pada input yang tersedia.
   - Klik tombol "Download" untuk memulai proses.
   - Progress unduhan akan ditampilkan di UI secara real-time.

## License

Proyek ini berlisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Acknowledgements

Terinspirasi dari [Miyuki-WebGUI](https://github.com/cailurus/Miyuki-WebGUI) dan menggunakan mesin **Miyuki** dari proyek [MissAV-Downloader](https://github.com/MiyukiQAQ/MissAV-Downloader/).
