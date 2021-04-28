from CsvTools import parseCSV
gadgetData = parseCSV("data" + "/gadget.csv")
consumableData = parseCSV("data" + "/consumable.csv")

def ubahjumlah(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    jumlah = input("Masukkan jumlah: ")
    
    def IsFound(ID, data):
        found = False
        i = 1
        while i < len(data) and not found:
            if data[i]["id"] == ID:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False
    
    # ALGORITMA
    if ID[0] == "G":
        if IsFound(ID, data):
            for i in range(len(data)):
                if data[i]["jumlah"] < jumlah and jumlah > 0:
                    data[i]["jumlah"] += jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                elif data[i]["jumlah"] > jumlah and jumlah > 0:
                    data[i]["jumlah"] += jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                elif data[i]["jumlah"] > jumlah and jumlah < 0:
                    data[i]["jumlah"] -= jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                else:
                    print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + data[i]["jumlah"] + "(<" + jumlah + ")")
        else:
            print("Tidak ada item dengan ID tersebut.")
    elif ID[0] == "C":
        if IsFound(ID, data):
            for i in range(len(data)):
                if data[i]["jumlah"] < jumlah and jumlah > 0:
                    data[i]["jumlah"] += jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                elif data[i]["jumlah"] > jumlah and jumlah > 0:
                    data[i]["jumlah"] += jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                elif data[i]["jumlah"] > jumlah and jumlah < 0:
                    data[i]["jumlah"] -= jumlah
                    print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                else:
                    print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + data[i]["jumlah"] + "(<" + jumlah + ")")
        else:
            print("Tidak ada item dengan ID tersebut.")
    else:
        print("Tidak ada item dengan ID tersebut.")