from function.csvTools import parseCSV # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error

import os 
def load(folderData):
    print("Loading...")
    fixingFolderTidakAda(folderData)
    fixingCsvTidakAda(folderData)
    required_csv =  ["user.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    data = []
    for File in required_csv:
        if File in ["gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]:
            data.append(urutDataBerdasarTanggal(parseCSV(folderData+"/"+File)))
        else:
            data.append(parseCSV(folderData+"/"+File))
    print("Selamat datang di \"Kantong Ajaib!\"")
    return tuple(data)
def createNewFile(fileName, header):
    newFile = open(fileName,'w')
    newFile.write(header)
    newFile.close()
def fixingCsvTidakAda(folderData):
    required_csv =  ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","user.csv","consumable_history.csv"]
    for (root, dirs, files) in os.walk(folderData,topdown=False):
        Files = files
    headers = {
    "consumable_history.csv" :"id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah",
    "consumable.csv":"id;nama;deskripsi;jumlah;rarity",
    "gadget.csv":"id;nama;deskripsi;jumlah;rarity;tahun ditemukan",
    "user.csv":"nama;username;password;alamat;role",
    "gadget_return_history.csv":"id;id_peminjaman;tanggal_pengembalian;jumlah_pengembalian;sisa_pengembalian;last_returned",
    "gadget_borrow_history.csv":"id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned"
    }
    for x in required_csv: 
        if x in Files: #jika sudah ada filenya
            pass
        else: #jika tidak ada file tersebut
            createNewFile(folderData+"/"+x,headers[x])

def fixingFolderTidakAda(folderData):
    Dirs = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            Dirs.append((root+"/"+name)[2:].replace("\\","/"))
    if folderData in Dirs:
        pass
    else: #folderData not in Dirs
        os.mkdir("./"+folderData)