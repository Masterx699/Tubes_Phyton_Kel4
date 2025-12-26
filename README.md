# Analisis Efisiensi Penggunaan Bahan Bakar Pada Mobil Menggunakan Machine Learning 

## Deskripsi
Proyek ini bertujuan untuk menganalisis dan memprediksi efisiensi bahan bakar mobil berdasarkan karakteristik kendaraan menggunakan machine learning. Efisiensi bahan bakar diklasifikasikan menjadi dua kategori, yaitu irit dan boros.

## Tujuan
1. Menganalisis pola penggunaan bahan bakar pada mobil.
2. Mengidentifikasi karakteristik kendaraan yang mempengaruhi efisiensi bahan bakar.
3. Membangun model machine learning untuk memprediksi kategori mobil irit atau boros bahan bakar.
4. Memberikan rekomendasi kendaraan yang lebih efisien dan ramah lingkungan.

## Dataset
Dataset yang digunakan berasal dari https://github.com/hananlu/basicPython/blob/master/Dataset/cars2.json

yang berisi spesifikasi mobil seperti : 
1. Nama mobil (`Name`)
2. Jumlah silinder (`Cylinders`)
3. Kapasitas mesin (`Displacement`)
4. Tenaga mesin (`Horsepower`)
5. Berat kendaraan (`Weight_in_lbs`)
6. Akselerasi (`Acceleration`)
7. Tahun produksi (`Year`)
8. Asal kendaraan (`Origin`)
9. Konsumsi bahan bakar dalam Miles Per Gallon (MPG) (`Miles_per_Gallon`)

## Machine Learning
Model utama yang digunakan pada proyek ini adalah Logistic Regression dengan pembagian data menggunakan train-test split sedangkan evaluasi model menggunakan akurasi dan presisi irit yang berdasarkan confusion matrix.

## Fitur Yang Digunakan
Berdasarkan scatter plot, korelasi terbanyak antara masing masing label dengan Miles Per Gallon adalah kapasitas mesin, berat kendaraan, dan horespowernya. Dari ketiga label inilah yang akan dijadikan sebagai fitur.

## Label
Label dibuat menggunakan median dari MPG dimana setiap data yang lebih besar dari median MPG akan diklasifikasikan sebagai irit dan data yang lebih kecil dari median MPG akan diklasifikasikan sebagai boros.

## Visualisasi
Visualisasi yang ditampilkan pada proyek ini adalah:
1. Perbandingan antara berat kendaraan dengan MPG
2. Perbandingan antara kekuatan mesin dengan MPG
3. Perbandingan antara kapasitas mesin dengan MPG
4. Distribusi kendaraan irit dan boros
5. Confusion matrix

## Hasil Dan Kesimpulan
1. Kapasitas mesin dan berat kendaraan memiliki pengaruh signifikan terhadap efisiensi bahan bakar.
2. Model Logistic Regression mampu mengklasifikasikan mobil irit dan boros dengan performa yang baik, sekitar 0.93 atau 93% untuk akurasi dan 0.94 atau 94% untuk presisi menjawab irit.
3. Berdasarkan hasil tersebut, kendaraan dengan berat yang ringan dan kapasitas mesin lebih sedikit direkomendasikan sebagai pilihan yang lebih hemat bahan bakar dan ramah lingkungan.

## Coretan
https://www.canva.com/design/DAG7mBzojS8/lrzYnMPsFRdp7nWtoJKuUQ/edit?utm_content=DAG7mBzojS8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
