import csv


def read_csv(path: str):
    """
    Приводим цсв в божеский вид

    Args:
        path (str): путь к файлу
    """

    df = dict()
    with open(path, encoding='utf-8') as csv_file:
        lines = csv.reader(csv_file, delimiter=';')
        head = True
        for line in lines:
            if head:
                head = False
                continue
            name = line[0]
            department = line[1]
            part = line[2]
            position = line[3]
            grade = line[4]
            wage = line[5]
            if df.get(department, 0) == 0:
                df[department] = dict()
            if df[department].get(part, 0) == 0:
                df[department][part] = dict()
            df[department][part][name] = [position, grade, wage]
    return df


def main_menu(df: dict):
    """Выводим три опции и ждем отклика"""
    task = input(
        'Что делаем? (1-3):\n1: Иерархия\n2: Вывести отчет\n3: Сохранить отчет\n'
        )
    if task not in '123':
        print('Такой опции нет :(')
    elif task == '1':
        hierarchy(df)
    elif task == '2':
        bring_info(df)
    elif task == '3':
        save_info(df)


def hierarchy(df: dict):
    """Выводим иерархию отделов"""
    for department in df:
        for part in df[department]:
            for name in df[department][part]:
                print(df[department][part][name])
    continew(df)


def bring_info(df: dict):
    """Выводим сводный отчет по департаментам"""
    for department in df:
        quantity = 0
        min_max_ratio = 0
        minimal_wage = 10000000000
        maximum_wage = 0
        summa = 0
        for part in df[department]:
            for name in df[department][part]:
                wage = int(df[department][part][name][2])
                quantity += 1
                if wage > maximum_wage:
                    maximum_wage = wage
                if wage < minimal_wage:
                    minimal_wage = wage
                summa += wage
        average_wage = summa/quantity
        min_max_ratio = maximum_wage - minimal_wage
        print(f'{department}: количество - {quantity}, з/п вилка - {min_max_ratio}, средняя з/п - {average_wage}')
    continew(df)


def save_info(df: dict):
    """Сохраняем отчет, часть кода взял c https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/"""
    blank = []
    for department in df:
        quantity = 0
        min_max_ratio = 0
        minimal_wage = 10000000000
        maximum_wage = 0
        summa = 0
        for part in df[department]:
            for name in df[department][part]:
                wage = int(df[department][part][name][2])
                quantity += 1
                if wage > maximum_wage:
                    maximum_wage = wage
                if wage < minimal_wage:
                    minimal_wage = wage
                summa += wage
        average_wage = summa/quantity
        min_max_ratio = maximum_wage - minimal_wage
    blank.append([department, quantity, min_max_ratio, average_wage])
    with open('Отчет.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Department', 'Количество', 'З/П вилка', 'Средняя З/П'])
        writer.writerows(blank)
    # Не разобрался с тем, как сохранить изменения, но логика такая
    continew(df)


def continew(df: dict):
    """Game over. Вставьте монетку"""
    keep_it_going = input('Вывести меню? Да/Нет\n')
    if keep_it_going == 'Да':
        main_menu(df)


def start():
    """Считываем путь к файлу и выводим меню"""
    print('Привет! Введите путь к файлу')
    path = input()
    df = read_csv(path)

    main_menu(df)


if __name__ == '__main__':
    start()
