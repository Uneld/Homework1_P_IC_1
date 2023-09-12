import datetime
import json
import os

FILE_PATH = 'notes.json'
notes = []
flag_work = True


def add_note():
    """
    Запрашивает у пользователя заголовок и текст заметки, создает новую заметку с уникальным идентификатором
    и временными метками в формате JSON, добавляет заметку в список notes и сохраняет в файл.
    """
    title = input('Введите заголовок заметки: ')
    note_body = input('Введите текст заметки: ')
    now_date = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    note = {
        'id': len(notes) + 1,
        'note_title': title,
        'note_body': note_body,
        'create_date': now_date,
        'update_date': now_date
    }
    notes.append(note)
    save_notes()


def show_note(note):
    print(f'\n******** Номер: {note["id"]} ********')
    print(f'Заголовок: {note["note_title"]}')
    print(f'Текст: {note["note_body"]}')
    print(f'Последнее изменение: {note["update_date"]}\n')


def show_all_notes():
    """
    Выводит все заметки в списке notes, если они есть, или сообщение о том, что заметок нет.
    """
    if notes:
        for note in notes:
            show_note(note)
    else:
        print('\n!!! Заметок нет !!!\n')


def delete_note():
    """
    Запрашивает у пользователя номер заметки, удаляет заметку из списка notes,
    если не найдено выводит сообщение. И сохраняет в файл изменненый спсиок.
    """
    note_id = int(input('Введите номер заметки: '))
    global notes
    found_note = False
    new_notes = []
    for note in notes:
        if note['id'] == note_id:
            found_note = True
        else:
            new_notes.append(note)
    if found_note:
        notes = new_notes
        save_notes()
    else:
        print(f'\n!!! Заметка с номером: {note_id} не найдена. !!!\n')


def edit_note():
    """
    Запрашивает у пользователя номер заметки, находит заметку в списке notes,
    запрашивает у пользователя новый заголовок и текст заметки, обновляет заметку с новой информацией
    и временными метками. И сохраняет в файл изменненый спсиок.
    """
    note_id = int(input('Введите номер заметки: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['note_title'] = title
            note['note_body'] = body
            note['update_date'] = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
            save_notes()
            return
    print(f'\n!!! Заметка с номером: {note_id} не найдена. !!!\n')


def show_note_by_id():
    """
       Запрашивает у пользователя идентификатор заметки, находит заметку в списке notes
       и выводит информацию о заметке, если она найдена.
       """
    note_id = int(input('Введите номер заметки: '))
    for note in notes:
        if note['id'] == note_id:
            show_note(note)
            return
    print(f'\n!!! Заметка с номером: {note_id} не найдена. !!!\n')


def show_notes_by_date():
    """
    Запрашивает у пользователя дату, находит все заметки в списке notes, созданные или обновленные в эту дату,
    и выводит информацию о заметках, если не найдены выдает сообщение.
    """
    while True:
        input_str = input('Введите дату в формате dd-mm-yyyy, q - для выхода: ')  # запрашиваем дату у пользователя
        try:
            if input_str == 'q':  # q для выхода из цикла ввода если передумали
                return
            date_input = datetime.datetime.strptime(input_str, '%d-%m-%Y').date()  # пытаемся распарсить введенную дату
            break
        except ValueError:
            print('!!! Некорректный формат даты. Попробуйте еще раз. !!!')

    found_notes = []
    for note in notes:
        # берем число месяц год у заметки
        date_create = datetime.datetime.strptime(note['create_date'], '%H:%M:%S %d-%m-%Y').date()
        date_update = datetime.datetime.strptime(note['update_date'], '%H:%M:%S %d-%m-%Y').date()
        # сравниваем с введенной, если подходит добавляем в новый список
        if date_create == date_input or date_update == date_input:
            found_notes.append(note)
    if found_notes:
        for note in found_notes:
            show_note(note)
    else:
        print(f'\n!!! Заметки за {date_input} не найдены. !!!\n')


def show_notes_last_week():
    """
    Находит все заметки в списке notes, созданные или обновленные за последнюю неделю и выводит информацию о заметках,
    если не найдены выдает сообщение
    """
    now_date = datetime.datetime.now()  # получаем текущую дату
    past_date = now_date - datetime.timedelta(days=7)  # получаем дату на 7 дней назад
    found_notes = []
    for note in notes:
        # берем число месяц год у заметки
        date_create = datetime.datetime.strptime(note['create_date'], '%H:%M:%S %d-%m-%Y')
        date_update = datetime.datetime.strptime(note['update_date'], '%H:%M:%S %d-%m-%Y')
        # проверяем входит ли дата заметки в диапазон недели, если входит добавляем в новый список
        if past_date <= date_create <= now_date or past_date <= date_update <= now_date:
            found_notes.append(note)
    if found_notes:
        for note in found_notes:
            show_note(note)
    else:
        print('\n!! Заметки за последнюю неделю не найдены. !!!\n')


def save_notes():
    """
    Сохраняет заметки из списка notes в файл в формате JSON.
    """
    with open(FILE_PATH, 'w') as file:
        # записываем список notes в файл в формате JSON с отступом в 4 пробела.
        json.dump(notes, file, indent=4)


def load_notes():
    """
    Загружает заметки из файла в формате JSON в глобальный список notes.
    Если файл не найден, список notes остается пустым.
    """
    if os.path.isfile(FILE_PATH): # проверяем есть ли файл, и если есть загружаем в наш список
        with open(FILE_PATH, 'r') as file:
            notes.extend(json.load(file))
    else:
        print('!!! Невозможно загрузить данные. Файл отсутвует. !!!')


load_notes()  # подгружаем заметки из файла
while flag_work: # попадаем в основное меню программы
    print('1. Добавить заметку')
    print('2. Редактировать заметку')
    print('3. Удалить заметку')
    print('4. Просмотреть заметку по номеру')
    print('5. Просмотреть заметки по дате')
    print('6. Просмотреть заметки за последнюю неделю')
    print('7. Просмотреть все заметки')
    print('8. Выход')

    choice = input('Введите номер команды: ')

    if choice == '1':
        add_note()
    elif choice == '2':
        edit_note()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        show_note_by_id()
    elif choice == '5':
        show_notes_by_date()
    elif choice == '6':
        show_notes_last_week()
    elif choice == '7':
        show_all_notes()
    elif choice == '8':
        flag_work = False
    else:
        print('Неверный номер команды')
