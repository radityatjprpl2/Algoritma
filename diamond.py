v = 5

for i in range(v):
    spasi = " " * (v - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)

v = 5

for i in range(v -2, -1, -1):
    spasi = " " * (v - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)
