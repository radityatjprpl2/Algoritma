belanja = []

for i in range(5):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    belanja.append(barang)

print("\nDaftar Belanja:")
for i, barang in enumerate(belanja, start=1):
    print(f"{i}. {barang}")

print(f"\nTotal item: {len(belanja)}")
print(f"Item ke-3: {belanja[2]}")