import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #NIM: 2009106036 + 10 = 46
        angka = int(input("Masukkan angka: "))
        x = 1
        y = 1
        while (x <= angka):
            print (y)
            y += 1
            if (y == 10):
                y -= 9
            x += 1
        break
    except ValueError:
        print("Nomor yang anda masukan tidak valid. Coba lagi...")
        time.sleep(3)
