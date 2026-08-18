#!/usr/bin/env python3
# engine.py - Mesin Spam Utama

import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Import modul
from modules.spam_otp import spam_otp
from modules.spam_wa import spam_wa
from modules.spam_sms import spam_sms
from modules.spam_ngl import spam_ngl
from modules.spam_call import spam_call

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
║              {Fore.YELLOW}SPAM MACHINE v2.0{Fore.CYAN}                          ║
║              {Fore.WHITE}Multi-Fitur Spammer Tools{Fore.CYAN}                   ║
╠══════════════════════════════════════════════════════════╣
║  {Fore.GREEN}[1]{Fore.WHITE} Spam OTP         {Fore.CYAN}│{Fore.WHITE} Banjir kode verifikasi    {Fore.CYAN}║
║  {Fore.GREEN}[2]{Fore.WHITE} Spam WhatsApp    {Fore.CYAN}│{Fore.WHITE} Banjir OTP WhatsApp       {Fore.CYAN}║
║  {Fore.GREEN}[3]{Fore.WHITE} Spam SMS         {Fore.CYAN}│{Fore.WHITE} Banjir SMS gateway        {Fore.CYAN}║
║  {Fore.GREEN}[4]{Fore.WHITE} Spam NGL         {Fore.CYAN}│{Fore.WHITE} Banjir pesan anonim       {Fore.CYAN}║
║  {Fore.GREEN}[5]{Fore.WHITE} Spam Telepon     {Fore.CYAN}│{Fore.WHITE} Banjir panggilan          {Fore.CYAN}║
║  {Fore.GREEN}[6]{Fore.WHITE} Spam Semua       {Fore.CYAN}│{Fore.WHITE} Kombinasi semua fitur     {Fore.CYAN}║
║  {Fore.GREEN}[0]{Fore.WHITE} Keluar           {Fore.CYAN}│{Fore.WHITE} Exit program              {Fore.CYAN}║
╚══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")

def pilih_thread():
    """Pilih jumlah thread"""
    print(f"\n{Fore.CYAN}Pilih Jumlah Thread:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}[1]{Fore.WHITE} 1 Thread (lambat)")
    print(f"  {Fore.GREEN}[2]{Fore.WHITE} 5 Thread (normal)")
    print(f"  {Fore.GREEN}[3]{Fore.WHITE} 10 Thread (cepat)")
    print(f"  {Fore.GREEN}[4]{Fore.WHITE} 20 Thread (sangat cepat)")
    print(f"  {Fore.GREEN}[5]{Fore.WHITE} 50 Thread (maksimal)")
    
    pilihan = input(f"\n{Fore.YELLOW}[?] Pilih (1-5, enter untuk 5): {Style.RESET_ALL}").strip()
    
    thread_map = {"1": 1, "2": 5, "3": 10, "4": 20, "5": 50}
    return thread_map.get(pilihan, 5)

def run_menu(pilihan):
    """Jalankan menu yang dipilih"""
    if pilihan == "1":
        # Spam OTP
        phone = input(f"{Fore.YELLOW}[?] Nomor target (08xxx): {Style.RESET_ALL}").strip()
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah OTP: {Style.RESET_ALL}").strip() or "50")
        threads = pilih_thread()
        spam_otp(phone, jumlah, threads)
    
    elif pilihan == "2":
        # Spam WhatsApp
        phone = input(f"{Fore.YELLOW}[?] Nomor target (08xxx): {Style.RESET_ALL}").strip()
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah WA OTP: {Style.RESET_ALL}").strip() or "50")
        threads = pilih_thread()
        spam_wa(phone, jumlah, threads)
    
    elif pilihan == "3":
        # Spam SMS
        phone = input(f"{Fore.YELLOW}[?] Nomor target (08xxx): {Style.RESET_ALL}").strip()
        pesan = input(f"{Fore.YELLOW}[?] Pesan SMS: {Style.RESET_ALL}").strip() or "Kode verifikasi: 123456"
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah SMS: {Style.RESET_ALL}").strip() or "50")
        threads = pilih_thread()
        spam_sms(phone, jumlah, pesan, threads)
    
    elif pilihan == "4":
        # Spam NGL
        username = input(f"{Fore.YELLOW}[?] Username NGL target: {Style.RESET_ALL}").strip()
        pesan = input(f"{Fore.YELLOW}[?] Pesan NGL: {Style.RESET_ALL}").strip() or "Halo, ada yang mau disampaikan"
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah NGL: {Style.RESET_ALL}").strip() or "50")
        threads = pilih_thread()
        spam_ngl(username, jumlah, pesan, threads)
    
    elif pilihan == "5":
        # Spam Telepon
        phone = input(f"{Fore.YELLOW}[?] Nomor target (08xxx): {Style.RESET_ALL}").strip()
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah panggilan: {Style.RESET_ALL}").strip() or "20")
        threads = pilih_thread()
        spam_call(phone, jumlah, threads)
    
    elif pilihan == "6":
        # Spam Semua
        phone = input(f"{Fore.YELLOW}[?] Nomor target (08xxx): {Style.RESET_ALL}").strip()
        jumlah = int(input(f"{Fore.YELLOW}[?] Jumlah per fitur: {Style.RESET_ALL}").strip() or "20")
        threads = pilih_thread()
        
        print(f"\n{Fore.CYAN}[+] Memulai Spam Semua Fitur...{Style.RESET_ALL}\n")
        spam_otp(phone, jumlah, threads)
        spam_wa(phone, jumlah, threads)
        spam_sms(phone, jumlah, "Pesan otomatis", threads)
        spam_call(phone, jumlah // 2, threads)

def main():
    """Fungsi utama"""
    while True:
        clear_screen()
        banner()
        
        pilihan = input(f"{Fore.YELLOW}[?] Pilih menu: {Style.RESET_ALL}").strip()
        
        if pilihan == "0":
            print(f"\n{Fore.RED}[+] Keluar...{Style.RESET_ALL}")
            sys.exit(0)
        elif pilihan in ["1", "2", "3", "4", "5", "6"]:
            run_menu(pilihan)
            input(f"\n{Fore.CYAN}Tekan Enter untuk kembali ke menu...{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}[!] Pilihan tidak valid!{Style.RESET_ALL}")
            input(f"{Fore.CYAN}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
