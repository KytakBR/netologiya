import csv

# Функция для загрузки данных из CSV-файла
def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Функция для преобразования данных
# Пример преобразования: форматирование суммы чека или исправление регистра
def transform_data(row):
    row['age'] = float(row['age'])  # Преобразуем возраст в число
    row['bill'] = float(row['bill'])  # Преобразуем сумму чека в число
    return row

# Функция для формирования текстового описания
# Применяет шаблон для создания строки описания
def create_description(row):
    gender_map = {'male': 'мужского', 'female': 'женского'}
    gender = gender_map.get(row['sex'].lower(), 'неопределенного')
    device_map = {'mobile': 'мобильного', 'desktop': 'настольного'}
    device = device_map.get(row['device_type'].lower(), 'неизвестного')

    return (f"Пользователь {row['name']} {gender} пола, {int(row['age'])} лет совершил(а) покупку на "
            f"{int(row['bill'])} у.е. с {device} браузера {row['browser']}. "
            f"Регион, из которого совершалась покупка: {row['region']}.\n -------------------")

# Функция для записи описаний в TXT-файл
def write_to_txt(descriptions, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n\n')

# Основной процесс
if __name__ == "__main__":
    input_file = 'web_clients_correct.csv'  # Путь к входному файлу
    output_file = 'client_descriptions.txt'  # Путь к выходному файлу

    # Шаг 1: Загрузка данных
    data = load_csv(input_file)

    # Шаг 2: Преобразование данных
    transformed_data = [transform_data(row) for row in data]

    # Шаг 3: Формирование описаний
    descriptions = [create_description(row) for row in transformed_data]

    # Шаг 4: Запись описаний в файл
    write_to_txt(descriptions, output_file)

    print(f"Описания покупателей успешно сохранены в файл: {output_file}")
