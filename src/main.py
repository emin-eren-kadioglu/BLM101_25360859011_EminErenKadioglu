def rle_encode(veri):
    if not veri:
        return ""
    encoded = ""
    i = 0
    while i < len(veri):
        char = veri[i]
        count = 1
        i += 1
        # Karakter aynı olduğu sürece ve sayaç 9'dan küçükken say
        while i < len(veri) and veri[i] == char and count < 9:
            count += 1
            i += 1
        encoded += f"{char}{count}"
    return encoded

def rle_decode(compressed):
    decoded = ""
    i = 0
    while i < len(compressed):
        # Format garantili olduğu için:
        # Çift indexler karakterdir (0, 2, 4...)
        # Tek indexler adettir (1, 3, 5...)
        char = compressed[i] # Karakteri al
        if i + 1 < len(compressed):
            count = int(compressed[i+1]) # Yanındaki rakamı al
            decoded += char * count
        i += 2 # İkişer ikişer atla
    return decoded

def oran_hesapla(origin, compressed):
    if len(origin) == 0: return 0
    oran = (1 - len(compressed) / len(origin)) * 100
    return round(oran, 2)

# --- ANA PROGRAM ---
def main():
    while True:
        print("\n--- RLE Sıkıştırıcı ---")
        girdi = input("Veriyi girin (Metin veya 0/1 Matrisi): ")
        if girdi == "exit": break
        if not girdi: continue

        # ENCODE
        cmprs = rle_encode(girdi)
        
        # ORAN
        oran = oran_hesapla(girdi, cmprs)
        
        print(f"[-] Orijinal: {girdi}")
        print(f"[+] Encoded : {cmprs}") 
        print(f"[%] Oran    : %{oran}")

        # DECODE SAĞLAMA
        decoded = rle_decode(cmprs)
        
        if girdi == decoded:
            print("[✓] decode işlemi BAŞARILI. Veri kaybı yok.")
        else:
            print("[!] HATA: Veri bozuldu!")

if __name__ == "__main__":
    main()
