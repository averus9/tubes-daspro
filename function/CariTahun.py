# Program CariTahun
# berisi prosedur untuk melakukan pencarian gadget sesuai kategori tahun

def CariTahun(data):
# I.S. data sudah dalam bentuk list of dictionary;
# F.S. menampilkan seluruh gadget sesuai kategori tahun yang dicari.
# KAMUS LOKAL
    # data : array of dictionary (data yang akan diproses)
    # tahun : integer
    # kategori : char (sudah pasti <,<=,=,>=,>)
    # gadget : string

    def IsFound(year, cat):
    # fungsi IsFound menghasilkan True jika menemukan barang
    # sesuai rarity yang dicari dan False jika tidak ditemukan
    # KAMUS LOKAL
        # cat : char (<, <=, =, >=, >)
        # found : bool
        # year, i : integer
    # ALGORITMA
        found = False
        i = 0
        while i < len(data) and not found:
            if cat == "<" and int(data[i]["tahun ditemukan"]) < year:
                found = True
            elif cat == "<=" and int(data[i]["tahun ditemukan"]) <= year:
                found = True
            elif cat == "=" and int(data[i]["tahun ditemukan"]) == year:
                found = True
            elif cat == ">=" and int(data[i]["tahun ditemukan"]) >= year:
                found = True
            elif cat == ">" and int(data[i]["tahun ditemukan"]) > year:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False

# ALGORITMA    
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print("\nHasil pencarian:\n")
    if IsFound(tahun, kategori):
        for i in range(len(data)):
            gadget = ("Nama            : {0}\n" + 
                      "Deskripsi       : {1}\n" +
                      "Jumlah          : {2}\n" +
                      "Rarity          : {3}\n" +                
                      "Tahun Ditemukan : {4}\n").format(data[i]["nama"], data[i]["deskripsi"], data[i]["jumlah"],
                      data[i]["rarity"],data[i]["tahun ditemukan"])
                     
            if kategori == "<" and int(data[i]["tahun ditemukan"]) < tahun:
                print(gadget)
            elif kategori == "<=" and int(data[i]["tahun ditemukan"]) <= tahun:
                print(gadget)
            elif kategori == "=" and int(data[i]["tahun ditemukan"]) == tahun:
                print(gadget)
            elif kategori == ">=" and int(data[i]["tahun ditemukan"]) >= tahun:
                print(gadget)
            elif kategori == ">" and int(data[i]["tahun ditemukan"]) > tahun:
                print(gadget)
    else:
        print(f"Gadget dengan tidak ditemukan!")
