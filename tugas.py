data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#no.1
for a, i in data_panen.items():
    print(f"lokasi{a}")
    print(f"nama lokasi: {i['nama_lokasi']}")
    print("hasil panen: ")
    for u,e in i['hasil_panen'].items():
        print(f" - {u}:{e}")

#no.2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print ("jumlah hasil panen jagung: {hasil_jagung_lokasi2}")

#no.3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"nama lokasi: {nama_lokasi3}")

#no.4
hasil_padi = {key: lokasi['hasil_panen']['padi'] for key, lokasi in data_panen.items()}
hasil_kedelai = {key: lokasi['hasil_panen']['kedelai'] for key, lokasi in data_panen.items()}
print("Hasil Panen Padi:", hasil_padi)
print("Hasil Panen Kedelai:", hasil_kedelai)

#no.5
jumlah_hasil_padi = {
    "lokasi1": data_panen["lokasi1"]["hasil_panen"]["padi"],
    "lokasi2": data_panen["lokasi2"]["hasil_panen"]["padi"],
    "lokasi3": data_panen["lokasi3"]["hasil_panen"]["padi"],
    "lokasi4": data_panen["lokasi4"]["hasil_panen"]["padi"],
    "lokasi5": data_panen["lokasi5"]["hasil_panen"]["padi"],
}

jumlah_hasil_kedelai = {
    "lokasi1": data_panen["lokasi1"]["hasil_panen"]["kedelai"],
    "lokasi2": data_panen["lokasi2"]["hasil_panen"]["kedelai"],
    "lokasi3": data_panen["lokasi3"]["hasil_panen"]["kedelai"],
    "lokasi4": data_panen["lokasi4"]["hasil_panen"]["kedelai"],
    "lokasi5": data_panen["lokasi5"]["hasil_panen"]["kedelai"],
}

print("Jumlah Hasil Panen Padi:", jumlah_hasil_padi)
print("Jumlah Hasil Panen Kedelai:", jumlah_hasil_kedelai)

#no.6
kondisi_lokasi = {}

for key, lokasi in data_panen.items():
    padi = lokasi["hasil_panen"]["padi"]
    jagung = lokasi["hasil_panen"]["jagung"]
    
    if padi > 1300 or jagung > 800:
        kondisi_lokasi[key] = "Memerlukan perhatian khusus"
    else:
        kondisi_lokasi[key] = "Dalam kondisi baik"

for lokasi, kondisi in kondisi_lokasi.items():
    print(f"{data_panen[lokasi]['nama_lokasi']} ({lokasi}): {kondisi}")


