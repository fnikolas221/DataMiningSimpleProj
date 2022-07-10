import matplotlib.pyplot as plt
from prettytable import PrettyTable

#KET SOAL
#kri1 : r = rendah,  s = sedang, t = tinggi, st = sangat tinggi
#kri2 : b = berat,   r = ringan
#kri3 : y = ya,      t = tidak
#kri4 : s = sering, ts = tidak sering
#kri5 : n = nyeri,   t = tidak
#kri6 : y = ya,      t = tidak
#ket  : n = negatif, p = positif
#Berapa Class Hasilnya.......

data = {
    "nomor": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "kri1" : ["r","r","s","s","s","s","s","s","t","t","t","t","t","t","st","st","st","st","st","st"],
    "kri2" : ["b","b","b","r","r","r","b","b","b","b","b","r","r","r","b","b","b","r","r","r"],
    "kri3" : ["y","t","t","t","y","y","y","y","t","y","y","y","t","y","y","t","t","y","y","t"],
    "kri4" : ["s","ts","s","s","ts","s","s","ts","s","s","s","ts","s","s","ts","ts","s","s","s","s"],
    "kri5" : ["n","t","n","t","n","n","n","t","n","t","n","n","t","n","t","n","t","n","t","n"],
    "kri6" : ["y","y","t","y","t","t","t","y","t","y","y","t","t","t","y","y","y","t","y","t"],
    "ket"  : ["n","n","n","n","n","n","n","p","p","p","p","n","n","p","p","p","p","p","n","n"]
}

def make_autopct(values):
     def my_autopct(pct):
         total = sum(values)
         val = int(round(pct*total/100.0))
         return '({v:d})'.format(v=val)
     return my_autopct

def diagram(data):
   labels = 'Positif', 'Negatif'
   sizes = [data["ket"].count("p"), data["ket"].count("n")]
   colors = ['green', 'red']
   explode = (0.2, 0)
   # Plot
   plt.pie(sizes, explode=explode, labels=labels, colors=colors,
   autopct=make_autopct(sizes), shadow=True, startangle=140)
   plt.show()  

def tabel(data):
  tabel = PrettyTable()
  tabel.field_names = ["No","Kriteria 1","Kriteria 2","Kriteria 3","Kriteria 4","Kriteria 5","Kriteria 6","Keterangan"]
  for i in range(len(data["nomor"])):
    tabel.add_row([data["nomor"][i],data["kri1"][i],data["kri2"][i],data["kri3"][i],data["kri4"][i],data["kri5"][i],data["kri6"][i],data["ket"][i]])
  print(tabel)
  
def naive(p,nomor,akri1,akri2,akri3,akri4,akri5,akri6):
    kun = "p"
    tid = "n"
    #Kriteria 1
    aa = 0
    bb = 0
    for i in range(p):
        if data.get("kri1")[i] == akri1 and data.get("ket")[i] == kun:
            aa+=1
        elif data.get("kri1")[i] == akri1 and data.get("ket")[i] == tid:
            bb+=1

    #Kriteria 2
    cc = 0
    dd = 0
    for i in range(p):
        if data.get("kri2")[i] == akri2 and data.get("ket")[i] == kun:
            cc+=1
        elif data.get("kri2")[i] == akri2 and data.get("ket")[i] == tid:
            dd+=1

    #Kriteria 3
    ee = 0
    ff = 0
    for i in range(p):
        if data.get("kri3")[i] == akri3 and data.get("ket")[i] == kun:
            ee+=1
        elif data.get("kri3")[i] == akri3 and data.get("ket")[i] == tid:
            ff+=1

    #Kriteria 4
    gg = 0
    hh = 0
    for i in range(p):
        if data.get("kri4")[i] == akri4 and data.get("ket")[i] == kun:
            gg+=1
        elif data.get("kri4")[i] == akri4 and data.get("ket")[i] == tid:
            hh+=1

    #Kriteria 5
    ii = 0
    jj = 0
    for i in range(p):
        if data.get("kri5")[i] == akri5 and data.get("ket")[i] == kun:
            ii+=1
        elif data.get("kri5")[i] == akri5 and data.get("ket")[i] == tid:
            jj+=1

    #Kriteria 6
    kk = 0
    ll = 0
    for i in range(p):
        if data.get("kri6")[i] == akri6 and data.get("ket")[i] == kun:
            kk+=1
        elif data.get("kri6")[i] == akri6 and data.get("ket")[i] == tid:
            ll+=1

    #class
    bi = (aa/data["ket"].count(kun))*(cc/data["ket"].count(kun))*(ee/data["ket"].count(kun))*(gg/data["ket"].count(kun))*(ii/data["ket"].count(kun))*(kk/data["ket"].count(kun))
    bo = (bb/data["ket"].count(tid))*(dd/data["ket"].count(tid))*(ff/data["ket"].count(tid))*(hh/data["ket"].count(tid))*(jj/data["ket"].count(tid))*(ll/data["ket"].count(tid))

    bis = bi * data["ket"].count(kun) / len(data.get("ket"))
    bos = bo * data["ket"].count(tid) / len(data.get("ket"))

    if bis > bos:
        print("Keterangan Positif : ",bis," > ","Keterangan Negatif : ",bos)
        data["nomor"].append(nomor)
        data["kri1"].append(akri1)
        data["kri2"].append(akri2)
        data["kri3"].append(akri3)
        data["kri4"].append(akri4)
        data["kri5"].append(akri5)
        data["kri6"].append(akri6)
        data["ket"].append(kun)
        print(">>>> Anda Positif Malaria")
    else:
        print("Keterangan Positif : ",bis," <= ","Keterangan Negatif : ",bos)
        data["nomor"].append(nomor)
        data["kri1"].append(akri1)
        data["kri2"].append(akri2)
        data["kri3"].append(akri3)
        data["kri4"].append(akri4)
        data["kri5"].append(akri5)
        data["kri6"].append(akri6)
        data["ket"].append(tid)
        print(">>>> Anda Negatif Malaria")

print("##"*22,"DATA SEBELUM","##"*22)
tabel(data)
diagram(data)

#soal
nomor = 21
akri1 = "t"
akri2 = "b"
akri3 = "y"
akri4 = "ts"
akri5 = "t"
akri6 = "y"

print("\n")
naive (len(data.get('nomor')),nomor,akri1,akri2,akri3,akri4,akri5,akri6)
print("\n")
print("##"*22,"DATA SESUDAH","##"*22)
tabel(data)
diagram(data)

