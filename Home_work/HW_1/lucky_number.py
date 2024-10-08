num = input("Введите шестизначный номер билета: ")
sum_1 = 0
sum_2 = 0

while len(num) != 6:
    if (len(num) > 6) or (len(num) < 6):
        print(f"\nВы ввели не шестизначное число, повторите попытку")
        num = input("Введите шестизначное число: ")

for i in range(3):
    sum_1 += int(num[i])

for i in range(3, 6):
    sum_2 += int(num[i])

if sum_1 == sum_2:
    print(f'Билет №{num} счастливый')
else:
    print(f'Билет №{num} несчастливый')