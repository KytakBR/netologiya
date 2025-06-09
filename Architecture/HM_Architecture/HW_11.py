import multiprocessing
from multiprocessing import shared_memory
import time

# Функция производителя
def producer(shared_memory_name, buffer_size):
    existing_shm = shared_memory.SharedMemory(name=shared_memory_name)
    buffer = existing_shm.buf
    message = "Привет от производителя!"
    encoded_message = message.encode('utf-8')
    buffer[:len(encoded_message)] = encoded_message  # Записываем байты в буфер
    print("Производитель: Сообщение отправлено.")
    existing_shm.close()

# Функция потребителя
def consumer(shared_memory_name, buffer_size):
    time.sleep(1)  # Убедимся, что производитель записал сообщение
    existing_shm = shared_memory.SharedMemory(name=shared_memory_name)
    buffer = existing_shm.buf
    received_message = bytes(buffer[:buffer_size]).decode('utf-8').strip('\x00')  # Читаем и декодируем сообщение
    print(f"Потребитель: Получено сообщение - {received_message}")
    existing_shm.close()

# Основная функция программы
def main():
    buffer_size = 1024
    shared_memory_name = "shared_memory"

    # Создаем общую память
    shm = shared_memory.SharedMemory(create=True, size=buffer_size, name=shared_memory_name)

    try:
        # Создаем процессы производителя и потребителя
        producer_process = multiprocessing.Process(target=producer, args=(shared_memory_name, buffer_size))
        consumer_process = multiprocessing.Process(target=consumer, args=(shared_memory_name, buffer_size))

        # Запускаем процессы
        producer_process.start()
        consumer_process.start()

        # Ожидаем завершения процессов
        producer_process.join()
        consumer_process.join()

    finally:
        # Удаляем общую память
        shm.close()
        shm.unlink()

if __name__ == "__main__":
    main()
