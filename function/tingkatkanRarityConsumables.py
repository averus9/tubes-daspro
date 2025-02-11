import time
import datetime
import sys
import os
from function.mintaConsumable import *  # pylint: disable=import-error
from function.kembalikanGadget import validasiTanggal  # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka  # pylint: disable=import-error
from function.validasiTahundanJumlah import tahunvalid, jumlahvalid # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error
# from mintaConsumable import *
campurSkript = """
Halo {}, kamu ingin campur apa?
    Tekan:
        1 "Aku tahu ID consumable yang mau aku campur Dora !!!"
        2 "Aku cuma tahu beberapa katanya Dora !!!" -----Bingung Aku
        0 "udah gamau nyampur"
"""


def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def randomize(key, durasi):
    timeAwal = time.time()
    timeString = str((time.time())).replace(".", "")
    a = int(timeString[len(timeString)-3:])
    c = 0
    # String to be displayed when the application is loading
    load_str = "mengocok dadu...."
    ls_len = len(load_str)


    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    i = 0

    for seed in lcg(10007, a, c, key):
        timeJalan = time.time()
        if timeJalan > timeAwal + durasi:
            break
        else:
            # semakin rendah, animasi makin cepat
            time.sleep(0.007) 
                                
            # convert string ke dalam list
            load_str_list = list(load_str) 
            
            # dapatkan ordinal
            x = ord(load_str_list[i])
            
            # y untuk nyimpan ordinal perubahan
            y = 0                             
    

            if x != 32 and x != 46:             
                if x>90:
                    y = x-32
                else:
                    y = x + 32
                load_str_list[i]= chr(y)
            
            res =''             
            for j in range(ls_len):
                res = res + load_str_list[j]
                
            sys.stdout.write("\r"+res + animation[anicount])
            sys.stdout.flush()
    

            load_str = res
    
            
            anicount = (anicount + 1)% 4
            i =(i + 1)% ls_len
    print("\n")
    return seed



def tentukanRange(rarity: dict):
    # range 1 milyar
    # 0 sampai satu milyar

    s = rarity["S"]/100
    a = rarity["A"]/100
    b = rarity["B"]/100
    c = rarity["C"]/100
    # (s,a,b,c) = normalize(s,a,b,c)
    batasAtas = 10000
    # tentukan range dari c
    rangeC = (0, c*batasAtas)
    rangeB = (rangeC[1], rangeC[1]+b*batasAtas)
    rangeA = (rangeB[1], rangeB[1]+a*batasAtas)
    rangeS = (rangeA[1], rangeA[1]+s*batasAtas)

    return {"S": rangeS, "A": rangeA, "B": rangeB, "C": rangeC}


def hasilRandomRarity(range: dict, random):
    for x in ["S", "A", "B", "C"]:
        rangeRarity = range[x]
        if random >= rangeRarity[0] and random < rangeRarity[1]:
            return x
    return "M"


def jumlahKeseluruhan(dataConsumable):
    jumlahKeseluruhan = 0
    for item in dataConsumable[1:]:
        jumlahKeseluruhan += int(item["jumlah"])
    return jumlahKeseluruhan


def rumusRarityUmum(pengaruhS, pengaruhA, pengaruhB, pengaruhC, dataConsumable):
    jumlah = jumlahKeseluruhan(dataConsumable)
    return {"S": pengaruhS, "A": pengaruhA, "B": pengaruhB, "C": pengaruhC}


def fraksiJumlah(rarity, dataConsumable):
    jumlahKeseluruhan = 0
    jumlah = 0
    for item in dataConsumable[1:]:
        jumlahKeseluruhan += int(item["jumlah"])
        if item["rarity"] == rarity:
            jumlah += int(item["jumlah"])
    if jumlahKeseluruhan == 0:
        return 0
    else:
        return jumlah/jumlahKeseluruhan


def rumusRarityJumlahInventory(dataConsumable):
    pengaruh = {}
    for rarity in ["S", "A", "B", "C"]:
        fraksi = fraksiJumlah(rarity, dataConsumable)
        if fraksi == 0:
            pengaruh[rarity] = 0
        else:
            pengaruh[rarity] = 1/fraksi
    return pengaruh  # dictionary of integer


def rumusPengaruhKeseluruhan(pengaruhRarityUmum, pengaruhRarityJumlahInventory):
    for rarity2 in ["S", "A", "B", "C"]:
        for rarity3 in ["S", "A", "B", "C"]:
            pengaruhRarityUmum[rarity2][rarity3] = pengaruhRarityUmum[rarity2][rarity3] * \
                pengaruhRarityJumlahInventory[rarity2]
    return pengaruhRarityUmum


def rarityPascaPenambahanItem(rarity: str, jumlah: int, pengaruhKeseluruhan: dict, rarityBasis: dict):
    rarityBaru = {}
    for rarity2 in ["S", "A", "B", "C"]:
        rarityBaru[rarity2] = rarityBasis[rarity2] + \
            jumlah*pengaruhKeseluruhan[rarity][rarity2]

    return rarityBaru  # dictionary of integer


def tingkatkanRarityConsumables(dataConsumable, dataRiwayat,username, idPencampur):
    print("Sebelum main, masukkan tanggal dulu yah hehe.... ")
    def prosedurMasukkanTanggal():
        masukkanTanggal = False
        while not masukkanTanggal:
            # tanggal
            day = input("Masukkan tanggal: ")
            while (validasiAngka(day) == False): # pylint: disable=E0602, E0603
                print("Masukkan angka! (˘･_･˘)")
                day = input("Masukkan tanggal: ")
            day = int(day)
            # bulan
            month = input("Masukkan bulan: ")
            while (validasiAngka(month) == False):
                print("Masukkan angka! (˘･_･˘)")
                month = input("Masukkan bulan: ")
            month = int(month)
            # tahun
            year = input("Masukkan tahun: ")
            while (validasiAngka(year) == False):
                print("Masukkan angka! (˘･_･˘)")
                year = input("Masukkan tahun: ")
            year = int(year)
            # validasi
            masukkanTanggal = validasiTanggal(day, month, year)
            if masukkanTanggal == False:
                print(
                    "Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
        dmy = datetime.datetime(year, month, day)
        tanggal = dmy.strftime(
            "%d") + "/" + dmy.strftime("%m") + "/" + dmy.strftime("%Y")
        return tanggal
    tanggal = prosedurMasukkanTanggal()
    def deklarasiSistemRarity():
        pengaruhRarityUmum = {"S": rumusRarityUmum(0.4, -0.4/21, -1.6/21, -6.4/21, dataConsumable), "A": rumusRarityUmum(0.2, 0.4, -0.2, -0.4, dataConsumable),
                                                "B": rumusRarityUmum(0.1, 0.2, 0., -0.12, dataConsumable), "C": rumusRarityUmum(0.00625, 0.025, 0.1, -0.13125, dataConsumable)}
        pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(
            dataConsumable)  # {"S":20}
        pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(
            pengaruhRarityUmum, pengaruhRarityJumlahInventory)
        return pengaruhRarityKeseluruhan
    jumlahBarangDicampur = 0
    rarityBasis = {}
    def prosedurPencampuran():
        rarityBasis = {"S": 2, "A": 16, "B": 36, "C": 46}
        pengaruhRarityKeseluruhan=deklarasiSistemRarity()
        jumlahBarangDicampur = 0
        idConsumable = dapatkanItem( # pylint: disable=E0602, E0603
            dataConsumable, username, campurSkript)  
        siap = False
        while not (siap):
            existStatus = isIdItemAda( idConsumable, dataConsumable)  # pylint: disable=E0602, E0603
            if existStatus["keberadaan"] and idConsumable != "0000000":
                indeks = existStatus["indeks"]
                print("{} | rarity: {} | jumlah: {}".format(dataConsumable[indeks]["nama"],dataConsumable[indeks]["rarity"],dataConsumable[indeks]["jumlah"]))
                jumlah = getJumlahPermintaan( # pylint: disable=E0602, E0603
                    "campur")  
                while jumlah > int(dataConsumable[indeks]["jumlah"]):
                    print("Jumlah yang kamu masukkan berlebih!")
                    jumlah = getJumlahPermintaan( # pylint: disable=E0602, E0603
                        "campur")  
                rarityBasis = rarityPascaPenambahanItem(
                    dataConsumable[indeks]["rarity"], jumlah, pengaruhRarityKeseluruhan, rarityBasis)
                dataConsumable[indeks]["jumlah"] = str(int(dataConsumable[indeks]["jumlah"]) - jumlah)
                idMinta = len(dataRiwayat)

                consumableHistoryDataBaru = {
                    "id": str(idMinta),
                    "id_pengambil": idPencampur,
                    "id_consumable": idConsumable,
                    "tanggal_pengambilan": tanggal,
                    "jumlah": jumlah,
                }
                dataRiwayat.append(consumableHistoryDataBaru)
                jumlahBarangDicampur += 1
            elif not existStatus["keberadaan"] and idConsumable != "0000000" :
                print("item tersebut tidak ada")
            # campur lagi?
            lagi = input("Campur yang lain?(Yy)")
            if lagi.upper() == "Y":
                idConsumable = dapatkanItem(dataConsumable, username, campurSkript)  # pylint: disable=E0602, E0603
                siap = False
            else:
                siap = True
    
    deklarasiSistemRarity()
    prosedurPencampuran()
    # PROSES PENGOCOKAN SETELAH PENCAMPURAN
    if jumlahBarangDicampur > 0:
        rangeDistribusi = tentukanRange(rarityBasis)
        angkaRandom = randomize(jumlahBarangDicampur, 1,)
        rarityHasil = hasilRandomRarity(rangeDistribusi, angkaRandom)
        kemungkinanHasil = getDataBonus(dataConsumable,rarityHasil)
        indeksHasil = angkaRandom % len(kemungkinanHasil)
        print("Yeeay, kamu mendapatkan {}. Rarity: {}".format(kemungkinanHasil[indeksHasil]["nama"],rarityHasil))
        tambahJumlahBonus(kemungkinanHasil[indeksHasil]["id"],1,dataConsumable)
    else:
        print("Kamu tidak mencampur apa-apa")

    # rarityBasis = {"S":2,"A":16,"B":36,"C":46}
    # pengaruhRarityUmum = {"S":rumusRarityUmum(0.4,-0.4/21,-1.6/21,-6.4/21),"A":rumusRarityUmum(0.1,0.4,-0.1,-0.4),"B":rumusRarityUmum(0.025,0.1,0.4,-0.525),"C":rumusRarityUmum(0.00625,0.025,0.1,-0.13125)}
    # pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(dataConsumable) #{"S":20}
    # pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(pengaruhRarityUmum,pengaruhRarityJumlahInventory)
    # rarity = input(">>> ")
    # jumlah = int(input(">>> "))

def tambahJumlahBonus(id,jumlah, dataConsumable):
    i = 1
    for x in dataConsumable[1:]:
        if x["id"] == id:
            dataConsumable[i]["jumlah"] =  str(int(dataConsumable[i]["jumlah"]) + jumlah)
        i += 1
def getDataBonus(dataConsumable,rarity):
    hasil = []
    jumlahItemBonus = 0
    for item in dataConsumable[1:]:
        if item["id"][1:3] == "CB":
            jumlahItemBonus += 1
            if item["rarity"] == rarity:
                hasil.append(item)
    if len(hasil) == 0:
        bonus = [{"id":"CB1","nama":"Air Mata Helmi Hibatullah","deskripsi":"QWERTY","jumlah":"0","rarity":"S"},{"id":"CB2","nama":"Otak Marcho","deskripsi":"QWERTY","jumlah":"0","rarity":"A"},{"id":"CB3","nama":"lays","deskripsi":"QWERTY","jumlah":"0","rarity":"B"},{"id":"CB4","nama":"Makanan Gaenak","deskripsi":"QWERTY","jumlah":"0","rarity":"C"}]
        for x in bonus:
            dataConsumable.append(x)
            if x["rarity"] == rarity:
                hasil.append(x)
    return hasil