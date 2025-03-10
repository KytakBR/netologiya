n = int(input("Введите ширину шоколадки: "))
m = int(input("Введите длину шоколадки: "))
def break_chocolate(n, m):
    if (n, m) == (0, 0) or (n, m) == (1, 1):
        return 0
    return (n - 1) + n * (m - 1)
result = break_chocolate(n, m)
print(f"Минимальное количество разломов: {result}")
