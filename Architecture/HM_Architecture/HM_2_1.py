import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Таблица истинности для мультиплексора
print("Таблица истинности для мультиплексора:")
data_mux = {
    "a1": [0, 0, 1, 1],
    "a2": [0, 1, 0, 1],
    "Выбранный вход": ["X1", "X2", "X3", "X4"],
    "F": ["X1", "X2", "X3", "X4"],
}
df_mux = pd.DataFrame(data_mux)
print(df_mux, "\n")

# 2. Таблица истинности для дешифратора
print("Таблица истинности для дешифратора:")
data_decoder = {
    "a1": [0, 0, 1, 1],
    "a2": [0, 1, 0, 1],
    "D1": [1, 0, 0, 0],
    "D2": [0, 1, 0, 0],
    "D3": [0, 0, 1, 0],
    "D4": [0, 0, 0, 1],
}
df_decoder = pd.DataFrame(data_decoder)
print(df_decoder, "\n")

# 3. Параметры времени
h = 1e-6  # Шаг времени, 1 мкс
t_min = 10e-6  # Длительность минимального импульса, 10 мкс
duration = 160e-6  # Общая длительность моделирования, 160 мкс
time = np.arange(0, duration, h)

# 4. Генерация входных сигналов (меандры)
def generate_signal(time, period):
    return ((time % period) < (period / 2)).astype(int) * 5

# Периоды сигналов
periods = [t_min * (2 ** i) for i in range(4)]  # Для X1, X2, X3, X4
signals_x = [generate_signal(time, period) for period in periods]

# Адресные сигналы a1 и a2
periods_a = [t_min * (2 ** i) for i in range(2)]  # Для a1, a2
a1 = generate_signal(time, periods_a[1])  # Меандр с периодом 40 мкс
a2 = generate_signal(time, periods_a[0])  # Меандр с периодом 20 мкс

# 5. Дешифратор (выходы D1-D4)
not_a1 = (a1 == 0).astype(int) * 5
not_a2 = (a2 == 0).astype(int) * 5

d1 = (not_a1 & not_a2)  # D1 = ~a1 & ~a2
d2 = (not_a1 & a2)      # D2 = ~a1 & a2
d3 = (a1 & not_a2)      # D3 = a1 & ~a2
d4 = (a1 & a2)          # D4 = a1 & a2

# 6. Мультиплексор (выход F)
f = (d1 * signals_x[0] + d2 * signals_x[1] + d3 * signals_x[2] + d4 * signals_x[3]) > 0
f = f.astype(int) * 5  # Преобразование в 0 и 5

# 7. Визуализация
fig, axs = plt.subplots(7, 1, figsize=(12, 10), sharex=True)

# Входные сигналы
for i, signal in enumerate(signals_x):
    axs[i].plot(time * 1e6, signal, label=f"X{i+1}")
    axs[i].set_ylabel(f"X{i+1} (В)")
    axs[i].legend(loc='upper right')

# Адресные сигналы
axs[4].plot(time * 1e6, a1, label="a1", color="orange")
axs[4].set_ylabel("a1 (В)")
axs[4].legend(loc='upper right')

axs[5].plot(time * 1e6, a2, label="a2", color="purple")
axs[5].set_ylabel("a2 (В)")
axs[5].legend(loc='upper right')

# Выходной сигнал F
axs[6].plot(time * 1e6, f, label="F", color="green")
axs[6].set_ylabel("F (В)")
axs[6].set_xlabel("Время (мкс)")
axs[6].legend(loc='upper right')

plt.tight_layout()
plt.show()
