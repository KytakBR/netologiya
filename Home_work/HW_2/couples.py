boys = sorted(input("Введите имена мальчиков через пробел: ").split())
girls = sorted(input("Введите имена девочек через пробел: ").split())

if len(boys) == len(girls):
    print(f"\nИдеальные пары:")
    for i in range(len(boys)):
        print(f"{boys[i]} и {girls[i]}")
else:
    print(f"\nВнимание, кто-то может остаться без пары.")