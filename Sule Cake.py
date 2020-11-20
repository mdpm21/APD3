import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    clear_screen()
    print("================================================")
    print("\t\t\tSULE CAKE")
    print("Created by Muhammad Daffa Putra Mahardika")
    print("================================================")
    print('Anda ingin membeli kue apa?')
    print("[1] Kue keju")
    print("[2] Kue coklat")
    print("[0] Keluar")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        kue_keju()
    elif(selected_menu == "2"):
        kue_coklat()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def kue_keju():
    clear_screen()
    kue_keju = 6000
    print('Harga satu kue keju : 6000')
    total = int(input('Masukan total kue keju yang dibeli: '))
    if (total >= 1) and (total <= 3):
        print('Anda tidak mendapatkan diskon')
        print('Tambah kue keju jika ingin menadapat diskon')
        total_harga = total * kue_keju
        print('Total harga adalah : ', total_harga)

    elif (total >= 4) and (total <= 15):
        print('Anda akan membeli ', total,' kue keju')
        print('Anda mendapatkan diskon 10%')
        total_harga = total * kue_keju
        print('Total harga sebelum diskon adalah : ', total_harga)
        diskon = 0.1
        total_harga_diskon = total * kue_keju * diskon
        harga_promo = total_harga - total_harga_diskon
        print('Total harga setelah diskon adalah : ', harga_promo)

    elif (total >= 16) and (total <= 25):
        print('Anda akan membeli ', total, ' kue keju')
        print('Anda mendapatkan diskon 15%')
        total_harga = (total * kue_keju)
        print('Total harga sebelum diskon adalah : ', total_harga)
        diskon = 0.15
        total_harga_diskon = (total * kue_keju * diskon)
        harga_promo = total_harga - total_harga_diskon
        print('Total harga setelah diskon adalah : ', harga_promo)
    
    else:
        print('Total kue keju tidak tersedia')
        back_to_menu()


def kue_coklat():
    clear_screen()
    kue_coklat = 3500
    print('Harga satu kue coklat : 3500')
    total = int(input('Masukan total kue coklat yang dibeli: '))
    if (total >= 1) and (total <= 4):
        print('Anda tidak mendapatkan diskon')
        print('Tambah kue coklat jika ingin menadapat diskon')
        total_harga = (total * kue_coklat)
        print('Total harga adalah : ', total_harga)

    elif(total >= 5) and (total <= 20):
        print('Anda akan membeli ', total, ' kue coklat')
        print('Anda mendapatkan diskon 7%')
        total_harga = (total * kue_coklat)
        print('Total harga sebelum diskon adalah : ', total_harga)
        diskon = 0.7
        total_harga_diskon = (total * kue_coklat * diskon)
        harga_promo = total_harga - total_harga_diskon
        print('Total harga setelah diskon adalah : ', harga_promo)

    elif(total >= 21) and (total <= 35):
        print('Anda akan membeli ', total, ' kue coklat')
        print('Anda mendapatkan diskon 12%')
        total_harga = (total * kue_coklat)
        print('Total harga sebelum diskon adalah : ', total_harga)
        diskon = 0.12
        total_harga_diskon = (total * kue_coklat * diskon)
        harga_promo = total_harga - total_harga_diskon
        print('Total harga setelah diskon adalah : ', harga_promo)
    
    else:
        print('Total kue coklat tidak tersedia')
        back_to_menu()



def close_app():
    clear_screen()
    print('==========================================================')
    print('Terima kasih telah berbelanja di SULE CAKE')
    print('==========================================================')
    time.sleep(3)
    exit()

def back_to_menu():
    print('\n')
    input('Tekan Enter untuk kembali...')
    show_menu()


if __name__ == "__main__":
    while True:
        show_menu()