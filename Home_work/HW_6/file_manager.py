import json

# Чтение данных из файла 'purchase_log.txt' в память
user_data = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as file_find:
    for line_find in file_find:
        data = json.loads(line_find)
        # Заполняем словарь {user_id: category}
        user_data[data["user_id"]] = data["category"]

# Открываем файл 'end_file.csv' один раз для записи
with open('end_file.csv', 'w') as output_file:
    # Чтение из файла 'visit_log__1_.csv' построчно
    with open('visit_log__1_.csv', 'r', encoding='utf-8') as file:
        for line in file:
            # Удаляем лишние пробелы и символы перевода строки
            line = line.strip()
            # Получаем id до первой запятой
            line_id = line.split(',', 1)[0]
            # Ищем соответствие в словаре user_data
            if line_id in user_data:
                # Пишем в файл 'funnel.csv' данные о визите и категории
                print(f"{line},{user_data[line_id]}\n")
                output_file.write(f"{line},{user_data[line_id]}\n")