def moves(n, x, y):
    with open('hanoi_tower.txt', 'a+') as tw:
        if n == 1:
            tw.write(f'Блин {n}: Стержень {x} -> Стержень {y}.\n')
            print(f'Блин {n}: Стержень {x} -> Стержень {y}.\n')
        else:
            moves(n - 1, x, moves.result - x - y)
            tw.write(f'Блин {n}: Стержень {x} -> Стержень {y}.\n')
            print(f'Блин {n}: Стержень {x} -> Стержень {y}.\n')
            moves(n - 1, moves.result - x - y, y)
            moves.counter += 1
    return moves.counter

disc_number = int(input('Введите количество блинов: '))
rods_number = int(input('Введите количество стержней: '))
moves.result = rods_number * 2
moves.counter = 1

moves(disc_number, 1, rods_number)
with open('hanoi_tower.txt', 'a+') as tw:
    tw.write(f'\nМинимальное количество ходов для решения головоломки: {moves(disc_number, 1, rods_number)}')