from prettytable import PrettyTable
PTables = PrettyTable()

#knn
print("="*60)
print("Penerapan Algoritma KNN dalam Memprediksi Penyakit Diabetes")
print("="*60)

data = {
    "beratBadan" : ["Kurus","Kurus","Normal","Obesitas","Obesitas","Obesitas","Normal","Kurus","Kurus","Obesitas","Kurus","Normal","Normal","Obesitas","Kurus","Normal","Kurus","Obesitas","Normal","Obesitas"],
    "jenisKelamin" : ["Laki-Laki","Perempuan","Laki-Laki","Laki-Laki","Laki-Laki","Perempuan","Perempuan","Laki-Laki","Laki-Laki","Laki-Laki","Perempuan","Perempuan","Laki-Laki","Perempuan","Laki-Laki","Laki-Laki","Perempuan","Laki-Laki","Perempuan","Perempuan"],
    "tekananDarah" : ["Normal","Normal","Normal","Tinggi","Rendah","Rendah","Rendah","Tinggi","Rendah","Tinggi","Tinggi","Tinggi","Normal","Tinggi","Normal","Tinggi","Tinggi","Rendah","Normal","Rendah"],
    "gulaDarah" : ["Tinggi","Tinggi","Tinggi","Tinggi","Normal","Normal","Normal","Tinggi","Normal","Normal","Normal","Tinggi","Normal","Tinggi","Rendah","Rendah","Rendah","Tinggi","Rendah","Tinggi"],
    "riwayat" : ["t","t","y","t","y","y","y","t","y","y","y","y","y","t","y","y","y","y","y","y"]
}

kasus = []
nama = "Ridho"
k1d = "Obesitas"
k2d = "Laki-Laki"
k3d = "Tinggi"
k4d = "Tinggi"

def knn(p):
    print("\n")
    print("Nama : ",nama)
    print("Berat badan : ",k1d)
    print("Jenis kelamin : ",k2d)
    print("Tekanan darah : ",k3d)
    print("Gula darah : ",k4d)
    print(">>>> Maka darimana penyakit diabetes",nama,"berasal?")
    print("\n")
    # menentukan bobot dari masing masing kriteria yang ada 
    k1 = 0.7
    k2 = 0.5
    k3 = 0.6
    k4 = 0.7

    nilaia = 0
    nilaib = k1
    nilaic = 0
    nilaid = k2
    nilaie = 0
    nilaif = k3
    nilaig = 0
    nilaih = k4
    # menentukan nilai a,c,e,g berdasarkan bobot yang sudah ditentukan
    for i in range(p):
        if data["gulaDarah"][i] == k4d:
            nilaig = 2.5
        else:
            nilaig = 0.7
        if data["tekananDarah"][i] == k3d:
            nilaie = 2.5
        else:
            nilaie = 0.6
        if data["jenisKelamin"][i] == k2d:
            nilaic = 2.5
        else:
            nilaic = 0.5
        if data["beratBadan"][i]== k1d:
            nilaia = 2.5
        else:
            nilaia = 0.7
        
        nk = ((nilaia*nilaib)+(nilaic*nilaid)+(nilaie*nilaif)+(nilaig*nilaih))/(nilaib+nilaid+nilaif+nilaih)
        kasus.append(nk)
        #jika nilai kedekatan yang diperoleh sama, 
        #maka dicari banyaknya nilai kedekatan turunan atau tidak turunan, 
        #jika lebih banyak turunan maka hasilnya turunan, jika sebaliknya maka tidak turunan
        #jika sama maka diambil nilai kedekatan yang muncul lebih awal
        nky = []
        nkn = []
        for i in range(len(kasus)):
            if(kasus[i]==max(kasus)):
                if data["riwayat"][i] == "y":
                    nky.append("y")
                else:
                    nkn.append("t")
        riwayat = ''
        for x in range(len(kasus)):
            if(kasus[x]==max(kasus)):
                riwayat = data["riwayat"][x]
                break
        if len(nky) > len(nkn):

            riwayat = "Turunan"
        else:
            riwayat = "Tidak Turunan"
    tablesoal(data)
    table(kasus)
    print("Jadi keterangan",nama, "adalah",riwayat)
    
def table(kedekatan):
    no = 0
    ket = ''
    PTables = PrettyTable()
    PTables.field_names = ["No.", "Kasus", "Nilai Kedekatan","Riwayat"]
    for i in range (len(kedekatan)):
        no+=1
        ket= data["riwayat"][i]
        if ket =="y":
            ket = "Turunan"
        else:
            ket = "Tidak Turunan"
        PTables.add_row([no, "Kasus " + str(no), kasus[i],ket])
    print(PTables)
    
def tablesoal(data):
    no = 0
    ket = ''
    PTables = PrettyTable()
    PTables.field_names = ["No.", "Berat Badan", "Jenis Kelamin","Tekanan Darah","Gula Darah","Riwayat"]
    for i in range (len(data['beratBadan'])):
        no+=1
        ket= data["riwayat"][i]
        if ket =="y":
            ket = "Turunan"
        else:
            ket = "Tidak Turunan"
        PTables.add_row([no, data['beratBadan'][i], data['jenisKelamin'][i] , data['tekananDarah'][i], data['gulaDarah'][i], ket])
    print(PTables)

knn(len(data.get('beratBadan')))
