from datetime import datetime


def parse_date(date_string):
    try:
        date_object = datetime.strptime(date_string, '%A, %B %d, %Y')
        return date_object
    except ValueError:
        try:
            date_object = datetime.strptime(date_string, '%A, %m.%d.%y')
            return date_object
        except ValueError:
            try:
                date_object = datetime.strptime(date_string, '%A, %d %B %Y')
                return date_object
            except ValueError:
                print(f'Некорректный формат даты. Повторите попытку.\n')


while True:
    date_string: str = input(f'Введите дату в формате газеты (или введите символ "q" для завершения): ')
    if date_string == 'q':
        break
    date_object = parse_date(date_string)
    if date_object is not None:
        print(date_object)
