# Argparse
from function.TambahItem import tambahitem
from function.simpan import simpan
from function.register import register
from function.PinjamGadget import pinjamGadget
from function.login import login
from function.LihatRiwayatPinjamGadget import lihatRiwayatPinjamGadget
from function.kembalikanGadget import kembalikanGadgetMain
from function.keluar import keluar
from function.CariTahun import cariTahun
from function.CariRarity import cariRarity
from function.load import load
from function.bantuan import bantuan
from function.lihatRiwayatKembalikanGadget import lihatRiwayatKembalikanGadget
import os
clear = lambda: os.system('cls')
# from function.CsvTools import parseCSV
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderData", help="folder dari data",
                    type=str)
args = parser.parse_args()
folderData = args.folderData

# Import fungsi secara keseluruhan


def main():
    clear()
    print("="*25 + "MENU UTAMA" + "="*25)
    (userData,
     gadgetData,
     consumableData,
     gadgetBorrowHistoryData,
     gadgetReturnHistoryData,
     consumableHistoryData,
     ) = load(folderData)
    kondisi = True
    user_status = {"username": "", "role": ""}
    def adminAllowedAction(perintah):
        if perintah == "register":
            register(userData)
        elif perintah == "carirarity":
            cariRarity(gadgetData)
        elif perintah == "caritahun":
            cariTahun(gadgetData)
        elif perintah == "tambahitem":
            tambahitem(gadgetData, consumableData)
        elif perintah == "hapusitem":
            pass
        elif perintah == "ubahjumlah":
            pass
        elif perintah == "riwayatpinjam":
            lihatRiwayatPinjamGadget(gadgetBorrowHistoryData)
        elif perintah == "riwayatkembali":
            lihatRiwayatKembalikanGadget(gadgetReturnHistoryData,userData,gadgetData,gadgetBorrowHistoryData)
        elif perintah == "riwayatambil":
            pass
    def userAllowedAction(perintah):
        if perintah == "carirarity":
            cariRarity(gadgetData)
        elif perintah == "caritahun":
            cariTahun(gadgetData)
        elif perintah == "pinjam":
            pinjamGadget(gadgetData, gadgetBorrowHistoryData, user_status["username"])
        elif perintah == "kembalikan":
            kembalikanGadgetMain(
                user_status["username"], gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData)
        elif perintah == "minta":
            pass
    
    print("masukkan perintah: (bingung? masukkan 'bantuan')")
    while kondisi:
        perintah = input()
        if perintah == "login":
            user_status = login(userData)
        elif perintah == "bantuan":
            role = user_status["role"]
            bantuan(role)
        elif perintah == "keluar":
            newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                "userData": userData,
                "gadgetData": gadgetData,
                "consumableData": consumableData,
                "consumableHistoryData": consumableHistoryData,
                "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                "gadgetReturnHistoryData": gadgetReturnHistoryData
            }
            kondisi = keluar(kondisi, newDatas, folderData)
        if user_status["role"] == "admin":
            print("masukkan perintah: (bingung? masukkan 'bantuan')"+" "*30 +"masuk sebagai: "+user_status["username"])
            adminAllowedAction(perintah)
        elif user_status["role"] == "user":
            print("masukkan perintah: (bingung? masukkan 'bantuan')"+" "*30 +"masuk sebagai: "+user_status["username"])
            userAllowedAction(perintah)
        

if __name__ == "__main__":
    main()