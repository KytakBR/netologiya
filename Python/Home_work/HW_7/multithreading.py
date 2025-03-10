import time
import concurrent.futures

# Формула 1: f(x) = x^2 - x^2 + x^4 - x^5 + x + x
def formula_1(x):
    return x**2 - x**2 + x**4 - x**5 + x + x

# Формула 2: f(x) = x + x
def formula_2(x):
    return x + x

# Формула 3: результат вычислений 1 + результат вычислений 2
def formula_3(result_1, result_2):
    return result_1 + result_2

# Функция для выполнения вычислений
def compute(iterations):
    start_time = time.time()

    # Шаг 1 и Шаг 2: Параллельное выполнение формул 1 и 2
    step_1_start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures_1 = executor.map(formula_1, range(iterations))
        futures_2 = executor.map(formula_2, range(iterations))
        results_1 = list(futures_1)
        results_2 = list(futures_2)
    step_1_end = time.time()

    # Шаг 3: Последовательное выполнение формулы 3
    step_2_start = time.time()
    results_3 = [formula_3(r1, r2) for r1, r2 in zip(results_1, results_2)]
    step_2_end = time.time()

    end_time = time.time()

    return {
        "step_1_duration": step_1_end - step_1_start,
        "step_2_duration": step_2_end - step_2_start,
        "total_duration": end_time - start_time,
    }

# Выполнение для 10,000 и 100,000 итераций
results_10k = compute(10_000)
results_100k = compute(100_000)

# Вывод результатов
print("Результаты для 10,000 итераций:")
print(f"Шаг 1 и Шаг 2 (параллельно): {results_10k['step_1_duration']} сек.")
print(f"Шаг 3 (последовательно): {results_10k['step_2_duration']} сек.")
print(f"Общее время выполнения: {results_10k['total_duration']} сек.\n")

print("Результаты для 100,000 итераций:")
print(f"Шаг 1 и Шаг 2 (параллельно): {results_100k['step_1_duration']} сек.")
print(f"Шаг 3 (последовательно): {results_100k['step_2_duration']} сек.")
print(f"Общее время выполнения: {results_100k['total_duration']} сек.")