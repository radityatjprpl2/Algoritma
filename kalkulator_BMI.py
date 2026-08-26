berat = int(input("masukan berat badan (kg): "))
tinggi = int(input("masukan tinggi badan (m): "))
bmi = berat / tinggi ** 2

print ("Berat badan :", BB,"kg")
print ("Tinggi badan :", TB,"cm")

if bmi < 25:
    print ("keterangan : Kurus (underwight)")
if bmi < 50:
    print ("keterangan : normal (ideal)")
if bmi < 100:
    print ("keterangan : gemuk (overweight)")
else:
    print ("keterangan : obesitas (atur pola makan)")