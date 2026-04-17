import multiprocessing
import time
import os

daftar_gambar = [8, 7, 9, 6, 8, 1, 1, 1, 1, 1] 

def proses_kompresi(id_gambar, durasi):
    pid = os.getpid()
    print(f"[Core {pid}] Memproses Gambar ke-{id_gambar} (Beban: {durasi}s)...")
    time.sleep(durasi)
    print(f"--- [Core {pid}] Selesai Gambar ke-{id_gambar}")

if __name__ == "__main__":
    print("=== ETS: KOMPRESI GAMBAR (STATIC UNEVEN DISTRIBUTION) ===\n")
    
    start_time = time.time()
    num_cores = 2 
    
    chunk_size = len(daftar_gambar) // num_cores
    
    tugas = list(enumerate(daftar_gambar))
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        pool.starmap(proses_kompresi, tugas)

    end_time = time.time()
    total_waktu = end_time - start_time
    waktu_ideal = sum(daftar_gambar) / num_cores

    print("\n" + "="*45)
    print(f"Total Waktu Eksekusi (Real)  : {total_waktu:.2f} detik")
    print(f"Estimasi Waktu Ideal         : {waktu_ideal:.2f} detik")
    print("="*45)
    
    print("\nPenjelasan Analisis:")
    print(f"Core 1 mengerjakan total beban: {sum(daftar_gambar[:5])} detik")
    print(f"Core 2 mengerjakan total beban: {sum(daftar_gambar[5:])} detik")
    print("Ini menunjukkan ketimpangan beban (Uneven Distribution).")
    print("Kondisi IDEAL tercapai jika beban Core 1 ≈ Core 2.")

    