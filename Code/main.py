import joblib

def pengubah_satuan(hp, berat_kg, cc):
    LBS = 2.20462
    CU_IN = 16.3871

    berat_lbs = berat_kg * LBS
    mesin_cu_in = cc / CU_IN

    return hp, berat_lbs, mesin_cu_in

def dataset():
    model = joblib.load("X:/Code/Tubes_Phyton_Kel4/Model ML/model_logistic.joblib")

    Nama = input("Masukkan Nama Kendaraan : ")
    hp = float(input("Masukkan horsepower kendaraan (hp): "))
    berat_kg = float(input("Masukkan berat kendaraan (kg): "))
    cc = float(input("Masukkan kapasitas mesin (cc): "))

    hp, berat_lbs, mesin_cu_in = pengubah_satuan(hp, berat_kg, cc)

    analisis = [[hp, berat_lbs, mesin_cu_in]]
    preds = model.predict(analisis)

    if preds[0] == 1:
        hasil = "IRIT"
    else:
        hasil = "BOROS"

    print("\n=== HASIL ANALISIS ===")
    print(f"Nama Mobil          : {Nama}")
    print(f"Horsepower          : {hp}")
    print(f"Berat Kendaraan     : {berat_lbs:.2f} lbs")
    print(f"Kapasitas Mesin     : {mesin_cu_in:.2f} cu in")
    print(f"Hasil Prediksi      : {hasil}")

    return hasil


while True:
    print("\n=== MENU ===")
    print("1. Analisis Menggunakan Model Logistic Regression")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        dataset()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
