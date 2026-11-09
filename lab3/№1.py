f=True
while f:
    try:
        a=int(input("Ведите число:"))
        f=False
    except ValueError:
        print("Введите положительное число")

S=0
if  0<=a<=50:
    for i in range (a,51):
        S+= i**2
    print(f"Сумма чисел {a} равна {S} ")
else:
    print("Введите число от 0 до 50")


F=True
while f:
    try:
        n=int(input("Введите число:"))
        F=False
    except ValueError:
        print("Введите положительное число")

while 