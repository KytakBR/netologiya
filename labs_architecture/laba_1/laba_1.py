import matplotlib.pyplot as plt
import numpy as np

# Параметры моделирования
h = 0.000001  # Шаг времени (1 мкс)
t = 0.001  # Общее время моделирования (1 мс)

# Временная шкала
x = np.arange(0, t, h)[:-1]  # Создаём массив длиной 1000

# Генерация сигналов с частотой 5 кГц и 10 кГц
y_5kHz = np.tile(np.concatenate((np.full(100, 0.5), np.full(100, 4.5))), 5)
y_10kHz = np.tile(np.concatenate((np.full(50, 0.5), np.full(50, 4.5))), 10)

# Постоянная времени
T2 = 0.00002

# Учёт ёмкости для сигнала 5 кГц
u_5kHz = [y_5kHz[0]]
for i in range(1, len(y_5kHz)):
    u_5kHz.append(u_5kHz[-1] + h * (y_5kHz[i] - u_5kHz[-1]) / T2)

# Учёт ёмкости для сигнала 10 кГц
u_10kHz = [y_10kHz[0]]
for i in range(1, len(y_10kHz)):
    u_10kHz.append(u_10kHz[-1] + h * (y_10kHz[i] - u_10kHz[-1]) / T2)

# Генерация случайных помех с амплитудой ±0.2 В
noise = np.random.uniform(-0.2, 0.2, len(x))
u_5kHz_noisy = np.array(u_5kHz) + noise
u_10kHz_noisy = np.array(u_10kHz) + noise

# Пороговые значения
Umin1, Umax1 = 1.5, 3.5
Umin2, Umax2 = 2, 4

# Функция моделирования логического каскада
def logical_cascade(input_signal, Umin, Umax):
    output_signal = [0.5]  # Начальное значение логического "0"
    for i in range(1, len(input_signal)):
        if output_signal[-1] == 0.5 and input_signal[i] > Umax:
            output_signal.append(4.5)  # Переключение в "1"
        elif output_signal[-1] == 4.5 and input_signal[i] < Umin:
            output_signal.append(0.5)  # Переключение в "0"
        elif output_signal[-1] == 0.5 and input_signal[i] <= Umax:
            output_signal.append(0.5)  # Остаётся "0"
        elif output_signal[-1] == 4.5 and input_signal[i] >= Umin:
            output_signal.append(4.5)  # Остаётся "1"
    return output_signal

# Логический каскад для сигналов с помехами
output_5kHz = logical_cascade(u_5kHz_noisy, Umin1, Umax1)
output_10kHz = logical_cascade(u_10kHz_noisy, Umin2, Umax2)

# Построение графиков в одном окне
plt.figure(figsize=(10, 20))

# График 1: Входные сигналы
plt.subplot(5, 1, 1)
plt.plot(x, y_5kHz, label="Сигнал 5 кГц", linestyle="--")
plt.plot(x, y_10kHz, label="Сигнал 10 кГц", linestyle=":")
plt.title("Входные сигналы (5 кГц и 10 кГц)")
plt.xlabel("Время (с)")
plt.ylabel("Напряжение (В)")
plt.legend()
plt.grid()

# График 2: Сигналы с учётом ёмкости 5 кГц
plt.subplot(5, 1, 2)
plt.plot(x, y_5kHz, '--', label="Входной сигнал 5 кГц")
plt.plot(x, u_5kHz, label="С учётом ёмкости 5 кГц")
plt.title("Сигналы с учётом ёмкостной составляющей 5 кГц")
plt.xlabel("Время (с)")
plt.ylabel("Напряжение (В)")
plt.legend()
plt.grid()

# График 2: Сигналы с учётом ёмкости 10 кГц
plt.subplot(5, 1, 3)
plt.plot(x, y_10kHz, '--', label="Входной сигнал 10 кГц")
plt.plot(x, u_10kHz, label="С учётом ёмкости 10 кГц")
plt.title("Сигналы с учётом ёмкостной составляющей 10 кГц")
plt.xlabel("Время (с)")
plt.ylabel("Напряжение (В)")
plt.legend()
plt.grid()


# График 3: Сигналы с помехами
plt.subplot(5, 1, 4)
plt.plot(x, u_5kHz_noisy, label="С помехами 5 кГц")
plt.plot(x, u_10kHz_noisy, label="С помехами 10 кГц")
plt.title("Сигналы с помехами")
plt.xlabel("Время (с)")
plt.ylabel("Напряжение (В)")
plt.legend()
plt.grid()

# График 4: Выходной сигнал
plt.subplot(5, 1, 5)
plt.plot(x, output_5kHz, label="Выходной сигнал 5 кГц")
plt.plot(x, output_10kHz, label="Выходной сигнал 10 кГц")
plt.title("Выходной сигнал логического каскада 5 кГц и 10 кГц")
plt.xlabel("Время (с)")
plt.ylabel("Напряжение (В)")
plt.legend()
plt.grid()

# Показать все графики
plt.tight_layout()
plt.show()

