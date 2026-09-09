for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
    print()
#

n = int(input("masukan angka: "))
i = 1
while i <= n:
    if i % 15 == 0 :
        print("fizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)
    i+=1