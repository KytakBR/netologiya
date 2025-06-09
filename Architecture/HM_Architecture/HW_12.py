import os
import stat
import subprocess


def get_filesystem_info(path):
    """Вывод информации о файловой системе для заданного пути."""
    stats = os.statvfs(path)
    print(f"Информация о файловой системе для пути: {path}")
    print(f"Размер блока (байты): {stats.f_bsize}")
    print(f"Количество блоков: {stats.f_blocks}")
    print(f"Количество свободных блоков: {stats.f_bfree}")
    print(f"Количество доступных блоков для пользователя: {stats.f_bavail}")
    print(f"Количество inode: {stats.f_files}")
    print(f"Количество свободных inode: {stats.f_ffree}")
    print(f"Количество доступных inode для пользователя: {stats.f_favail}")
    # Определение типа файловой системы
    try:
        result = subprocess.run(['df', '-T', path], stdout=subprocess.PIPE, text=True, check=True)
        lines = result.stdout.splitlines()
        if len(lines) > 1:
            fs_type = lines[1].split()[1]  # Второй столбец второй строки
            print(f"Тип файловой системы: {fs_type}")
    except Exception as e:
        print(f"Не удалось определить тип файловой системы: {e}")
    print("-" * 50)


def get_file_info(file_path):
    """Вывод информации о выбранном файле."""
    stats = os.stat(file_path)
    file_type = {
        stat.S_IFREG: "Обычный файл",
        stat.S_IFDIR: "Каталог",
        stat.S_IFCHR: "Символьное устройство",
        stat.S_IFBLK: "Блочное устройство",
        stat.S_IFIFO: "FIFO (канал)",
        stat.S_IFLNK: "Символьная ссылка",
        stat.S_IFSOCK: "Сокет"
    }.get(stat.S_IFMT(stats.st_mode), "Неизвестный тип")

    print(f"Информация о файле: {file_path}")
    print(f"Inode: {stats.st_ino}")
    print(f"Тип файла: {file_type}")
    print(f"Атрибуты файла: {oct(stats.st_mode)}")
    print(f"Размер файла (байты): {stats.st_size}")
    print(f"Владелец (UID): {stats.st_uid}")
    print(f"Группа (GID): {stats.st_gid}")
    print(f"Количество жёстких ссылок: {stats.st_nlink}")
    print("-" * 50)


if __name__ == "__main__":
    # Укажите пути для анализа
    filesystem_path = "/"
    file_paths = ["/etc/passwd", "/tmp/example.txt"]  # Убедитесь, что файлы существуют

    # Вывод информации о файловой системе
    get_filesystem_info(filesystem_path)

    # Вывод информации о файлах
    for file_path in file_paths:
        if os.path.exists(file_path):
            get_file_info(file_path)
        else:
            print(f"Файл {file_path} не существует.")
