import numpy as np
import matplotlib.pyplot as plt

# Параметры
frequencies = [10e3, 5e3, 2e3]  # Частоты в Гц
amplitude = 5  # Амплитуда сигнала
duration = 1e-3  # Длительность в секундах
dt = 1e-6  # Шаг моделирования в секундах
forbidden_zone = (2, 4)  # Запрещённая зона

# Временная шкала
time = np.arange(0, duration, dt)

# Генерация периодического сигнала (треугольный сигнал для каждой частоты)
signals = [amplitude * (2 * np.abs(2 * (time * f - np.floor(time * f + 0.5))) - 1) for f in frequencies]

# Логический каскад
logical_outputs = []
for signal in signals:
    logic_output = np.zeros_like(signal)
    logic_output[signal > forbidden_zone[1]] = 5  # Верхняя граница
    logic_output[signal < forbidden_zone[0]] = 0  # Нижняя граница
    logical_outputs.append(logic_output)

# Визуализация
fig, axs = plt.subplots(len(frequencies), 2, figsize=(12, 8), sharex=True)
for i, (signal, logic_output, f) in enumerate(zip(signals, logical_outputs, frequencies)):
    # Исходный сигнал
    axs[i, 0].plot(time * 1e3, signal, label=f"Треугольный сигнал, {f / 1e3:.1f} кГц")
    axs[i, 0].axhline(forbidden_zone[0], color='red', linestyle='--', label='Нижняя граница запрещённой зоны')
    axs[i, 0].axhline(forbidden_zone[1], color='red', linestyle='--', label='Верхняя граница запрещённой зоны')
    axs[i, 0].set_title(f"Исходный сигнал ({f / 1e3:.1f} кГц)")
    axs[i, 0].set_ylabel("Амплитуда")
    axs[i, 0].legend()

    # Выход логического каскада
    axs[i, 1].plot(time * 1e3, logic_output, label='Выход логического каскада', color='green')
    axs[i, 1].set_title(f"Логический выход ({f / 1e3:.1f} кГц)")
    axs[i, 1].set_ylabel("Сигнал")
    axs[i, 1].legend()

# Общие настройки
for ax in axs[-1, :]:
    ax.set_xlabel("Время (мс)")
plt.tight_layout()
plt.show()