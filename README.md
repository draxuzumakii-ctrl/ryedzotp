# SPAM MACHINE v2.0

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-red)

**SPAM MACHINE** adalah tools multi-fitur untuk pengujian keamanan dan edukasi.

## ⚠️ DISCLAIMER

Tools ini dibuat **HANYA** untuk tujuan edukasi dan pengujian keamanan.
Penggunaan untuk aktivitas ilegal adalah tanggung jawab pengguna sepenuhnya.

## 🔥 FITUR

| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| Spam OTP | Banjir kode verifikasi | ✅ |
| Spam WhatsApp | Banjir OTP WhatsApp | ✅ |
| Spam SMS | Banjir SMS gateway | ✅ |
| Spam NGL | Banjir pesan anonim | ✅ |
| Spam Telepon | Banjir panggilan | ✅ |
| Spam Email | Banjir email | ✅ |
| Spam Semua | Kombinasi semua | ✅ |

## 🚀 INSTALLASI

### Termux (Android)
```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install requests colorama cryptography pycryptodome rich
git clone https://github.com/USERNAME/spam-machine.git
cd spam-machine
python3 main.py
