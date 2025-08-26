# Basit bir X ve O oyunu
tahta = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tahtaYazdir():
    for satir in tahta:
        print("|".join(satir))
        print("-" * 5)

def hamleYap(oyuncu, satir, sutun):
    if tahta[satir][sutun] == " ":
        tahta[satir][sutun] = oyuncu
        return True
    else:
        print("Bu hamle geçersiz, tekrar deneyin.")
        return False
    
def kazananKontrol():
    for i in range(3):
        if tahta[i][0] == tahta[i][1] == tahta[i][2] != " ":
            return tahta[i][0]
        if tahta[0][i] == tahta[1][i] == tahta[2][i] != " ":
            return tahta[0][i]
    if tahta[0][0] == tahta[1][1] == tahta[2][2] != " ":
        return tahta[0][0]
    if tahta[0][2] == tahta[1][1] == tahta[2][0] != " ":
        return tahta[0][2]
    return None


def tahtaDoluMu():
    for satir in tahta:
        if " " in satir:
            return False
    return True

def oyun():
    oyuncular = ["X", "O"]
    siradaki = 0
    while True:
        tahtaYazdir()
        oyuncu = oyuncular[siradaki]
        print(f"Sıra {oyuncu} oyuncusunda.")
        try:
            satir = int(input("Satır (0, 1, 2): "))
            sutun = int(input("Sütun (0, 1, 2): "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue
        if hamleYap(oyuncu, satir, sutun):
            kazanan = kazananKontrol()
            if kazanan:
                tahtaYazdir()
                print(f"Tebrikler! {kazanan} kazandı!")
                break
            elif tahtaDoluMu():
                tahtaYazdir()
                print("Oyun berabere bitti!")
                break
            siradaki = 1 - siradaki
oyun()
