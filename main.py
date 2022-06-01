"""
SIMPLE SLOT MACHINE BUAH BUAHAN
"""
import random
import os
import time

# Valid list, var
buah = ('🥭', '🍎', '🍊', '🥑', '🍌', '🥭', '🍎', '🍊', '🍌', '🥑', '💣')
saldo = 1000
bet = None
baris1 = None
baris2 = None
baris3 = None
baris4 = None
baris5 = None
freeSpin = 0

# opening


def opening():
    global saldo, bet
    os.system('cls')
    print('Selamat data di game slot 🎰')
    print(f'Saldo awal kamu adalah Rp.{saldo}')
    print("===================")
    print("RULES")
    print("===================")
    print("Jika ada buah yang sama lebih dari 6/8 maka saldo akan bertambah sesuai bet dan nilai buah\n\njika tidak ada satupun buah yang berjumlah 6/8 maka saldo akan berkurang seusai bet\nSetiap buah memiliki nilai berupa perkalian, berikut nilai buah :")
    print("===================")
    print('6 🍎 = x1   6 🍌 = x2 \n6 🥭 = x3   6 🍊 = x4 \n6 🥑 = x5 \n\n8 🍎 = x3   8 🍌 = x4\n8 🥭 = x5   8 🍊 = x6\n8 🥑 = x7')

    print('\n4 💣 = x10 + Free Spin 1x')
    print("===================")
    time.sleep(1)
    Mulai()


def Mulai():
    """
    Tanya player apakah ingin memulai game?
    """
    start = input('Apakah kamu ingin mulai ?? \n[Y / N ] = ')
    start = start.lower()  # Lower str

    # Valid input start
    if start == 'yes' or start == 'y':
        print('Loading...')
        time.sleep(1)
        print('Semoga beruntung')
        time.sleep(1)
        os.system('cls')
        play()
    elif start == 'no' or start == 'n':
        print("Terimakasih telah bermain,semoga harimu penuh keberuntungan.")
        print("Menutup Game...")
        time.sleep(1)
        os.system('cls')
        exit()
    else:
        # Wrong input
        os.system('cls')
        print('Input yang kamu masukkan salah!')
        Mulai()


def play():
    global saldo, bet

    # Input Bet
    print("Masukkan bet terlebih dahulu sebelum memulai spin")
    print("===================")
    print("Min bet = Rp.5 \nMax bet = Rp.30")
    print(f'Saldo Rp.{saldo}')
    print("===================")
    bet = int(input("Bet = "))
    # valid bet
    if int(bet) < 5:
        print("Min bet harus lebih dari Rp.5")
        time.sleep(2)
        os.system('cls')
        play()
    elif int(bet) > 30:
        print("Max bet adalah Rp.30")
        time.sleep(2)
        os.system('cls')
        play()
    # else:
    #     sys.exc_info(bet)

    time.sleep(.5)
    os.system('cls')

    print(f"Bet sudah di tentukan, bet mu adalah = Rp.{bet} \nMemulai Game...")
    time.sleep(3)
    print('Loading...')
    os.system('cls')
    spin()


def askPlayAgain():
    Again = input('Apakah kamu ingin mulai lagi?? \n[Y / N ] = ')

    if Again == 'yes' or Again == 'y':
        # os.system('cls')
        spin()
    elif Again == 'no' or Again == 'n':
        os.system('cls')
        print("Terimakasih telah bermain,semoga harimu penuh keberuntungan.")
        print("Menutup Game...")
        time.sleep(1)
        os.system('cls')
        exit()
    else:
        # Wrong input
        print('Input yang kamu masukkan salah!')
        askPlayAgain()


def Random():
    randomBuah = random.sample(buah, 6)
    return randomBuah


def spin():
    global saldo, bet, hitungApple, hitungPisang, hitungMangga, hitungJeruk, hitungAvocado, hitungScater,freeSpin

    baris1 = Random()
    baris2 = Random()
    baris3 = Random()
    baris4 = Random()
    baris5 = Random()
    print("Loading...")
    time.sleep(2)
    os.system('cls')
    print("===================")
    print(" | ".join(baris1))
    print(" | ".join(baris2))
    print(" | ".join(baris3))
    print(" | ".join(baris4))
    print(" | ".join(baris5))
    print("===================")

    hasil = baris1 + baris2 + baris3 + baris4 + baris5

    hitungApple = hasil.count('🍎')
    hitungPisang = hasil.count('🍌')
    hitungMangga = hasil.count('🥭')
    hitungJeruk = hasil.count('🍊')
    hitungAvocado = hasil.count('🥑')
    hitungScater = hasil.count('💣')

    print(f"🍎 = {hitungApple} " + f" 🍌 = {hitungPisang}")
    print(f"🥭 = {hitungMangga} " + f" 🍊 = {hitungJeruk}")
    print(f"🥑 = {hitungAvocado} " + f" 💣 = {hitungScater}")
    print("===================")

    Hitung()


def spinScater():
    global saldo, bet, hitungApple, hitungPisang, hitungMangga, hitungJeruk, hitungAvocado, hitungScater,freeSpin

    baris1 = Random()
    baris2 = Random()
    baris3 = Random()
    baris4 = Random()
    baris5 = Random()
    print("Loading...")
    time.sleep(2)
    os.system('cls')
    print("===================")
    print(" | ".join(baris1))
    print(" | ".join(baris2))
    print(" | ".join(baris3))
    print(" | ".join(baris4))
    print(" | ".join(baris5))
    print("===================")

    hasil = baris1 + baris2 + baris3 + baris4 + baris5

    hitungApple = hasil.count('🍎')
    hitungPisang = hasil.count('🍌')
    hitungMangga = hasil.count('🥭')
    hitungJeruk = hasil.count('🍊')
    hitungAvocado = hasil.count('🥑')
    hitungScater = hasil.count('💣')

    print(f"🍎 = {hitungApple} " + f" 🍌 = {hitungPisang}")
    print(f"🥭 = {hitungMangga} " + f" 🍊 = {hitungJeruk}")
    print(f"🥑 = {hitungAvocado} " + f" 💣 = {hitungScater}")
    print("===================")

    hitungScater = 4
    if freeSpin == 1:
        hitungScater = 0
        freeSpin = 0
    Hitung()


def Hitung():
    global saldo, bet, hitungApple, hitungPisang, hitungMangga, hitungJeruk, hitungAvocado, hitungScater, menang, freeSpin

    # hitung 6
    if hitungScater >= 4:
        if freeSpin == 0:
            menang = bet*10
            saldo += menang
            cekscater()  # Ambil Freespin 10
            getScater()  # Set Scater 4
            Hitung()
        else:
            while freeSpin > 1:
                freeSpin -= 1
                getScater()
                time.sleep(1)
                print(f'Saldo Rp.{saldo}')
                print(f'Free Spin : {freeSpin}')
                time.sleep(1)
                totalScater()
                while freeSpin == 1:
                    Hitung()
    elif hitungApple >= 6:
        menang = bet
        saldo += menang
        print(f"🍎 {hitungApple}, Selamat Kamu Mendapatkan Rp.{menang} 🍎")

    elif hitungPisang >= 6:
        menang = bet*2
        saldo += menang
        print(f"🍌 {hitungPisang}, Selamat Kamu Mendapatkan Rp.{menang} 🍌")
    elif hitungMangga >= 6:
        menang = bet*3
        saldo += menang
        print(f"🥭 {hitungMangga}, Selamat Kamu Mendapatkan Rp.{menang} 🥭")
    elif hitungJeruk >= 6:
        menang = bet*4
        saldo += menang
        print(f"🍊 {hitungJeruk}, Selamat Kamu Mendapatkan Rp.{menang} 🍊")
    elif hitungAvocado >= 6:
        menang = bet*5
        saldo += menang
        print(f"🥑 {hitungAvocado}, Selamat Kamu Mendapatkan Rp.{menang} 🥑")

    # hitung 8
    elif hitungApple >= 8:
        menang = bet*3
        saldo += menang
        print(f"🍎 {hitungApple}, Selamat Kamu Mendapatkan Rp.{menang} 🍎")
    elif hitungPisang >= 8:
        menang = bet*4
        print(f"🍌 {hitungPisang}, Selamat Kamu Mendapatkan Rp.{menang} 🍌")
    elif hitungMangga >= 8:
        menang = bet*5
        saldo += menang
        print(f"🥭 {hitungMangga}, Selamat Kamu Mendapatkan Rp.{menang} 🥭")
    elif hitungJeruk >= 8:
        menang = bet*6
        saldo += menang
        print(f"🍊 {hitungJeruk}, Selamat Kamu Mendapatkan Rp.{menang} 🍊")
    elif hitungAvocado >= 8:
        menang = bet*7
        saldo += menang
        print(f"🥑 {hitungAvocado}, Selamat Kamu Mendapatkan Rp.{menang} 🥑")
    else:
        menang = bet
        saldo -= menang
        print("")

    print(f'Saldo Rp.{saldo}')
    askPlayAgain()


def cekscater():
    global saldo, bet, menang, hitungScater, freeSpin
    freeSpin = 10


def getScater():
    global hitungScater, freeSpin
    hitungScater = 4


def totalScater():
    global saldo, bet, hitungApple, hitungPisang, hitungMangga, hitungJeruk, hitungAvocado, hitungScater, menang, freeSpin

    if hitungApple >= 6:
        menang = bet
        saldo += menang
        print(f"🍎 {hitungApple}, Selamat Kamu Mendapatkan Rp.{menang} 🍎")

    elif hitungPisang >= 6:
        menang = bet*2
        saldo += menang
        print(f"🍌 {hitungPisang}, Selamat Kamu Mendapatkan Rp.{menang} 🍌")
    elif hitungMangga >= 6:
        menang = bet*3
        saldo += menang
        print(f"🥭 {hitungMangga}, Selamat Kamu Mendapatkan Rp.{menang} 🥭")
    elif hitungJeruk >= 6:
        menang = bet*4
        saldo += menang
        print(f"🍊 {hitungJeruk}, Selamat Kamu Mendapatkan Rp.{menang} 🍊")
    elif hitungAvocado >= 6:
        menang = bet*5
        saldo += menang
        print(f"🥑 {hitungAvocado}, Selamat Kamu Mendapatkan Rp.{menang} 🥑")

    # hitung 8
    elif hitungApple >= 8:
        menang = bet*3
        saldo += menang
        print(f"🍎 {hitungApple}, Selamat Kamu Mendapatkan Rp.{menang} 🍎")
    elif hitungPisang >= 8:
        menang = bet*4
        print(f"🍌 {hitungPisang}, Selamat Kamu Mendapatkan Rp.{menang} 🍌")
    elif hitungMangga >= 8:
        menang = bet*5
        saldo += menang
        print(f"🥭 {hitungMangga}, Selamat Kamu Mendapatkan Rp.{menang} 🥭")
    elif hitungJeruk >= 8:
        menang = bet*6
        saldo += menang
        print(f"🍊 {hitungJeruk}, Selamat Kamu Mendapatkan Rp.{menang} 🍊")
    elif hitungAvocado >= 8:
        menang = bet*7
        saldo += menang
        print(f"🥑 {hitungAvocado}, Selamat Kamu Mendapatkan Rp.{menang} 🥑")
    else:
        menang = bet
        saldo -= menang
        print("")
    spinScater()


opening()
