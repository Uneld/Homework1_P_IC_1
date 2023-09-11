import datetime

notes = []
flag_work = True


def add_note():
    """
    Запрашивает у пользователя заголовок и текст заметки, создает новую заметку с уникальным идентификатором
    и временными метками в формате JSON, добавляет заметку в список notes.
    """
    title = input('Введите заголовок заметки: ')
    note_body = input('Введите текст заметки: ')
    now_date = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    print(now_date)
    note = {
        'id': len(notes) + 1,
        'note_title': title,
        'note_body': note_body,
        'create_date': now_date,
        'update_date': now_date
    }
    notes.append(note)


def show_all_notes():
    """
    Выводит все заметки в списке notes, если они есть, или сообщение о том, что заметок нет.
    """
    if notes:
        for note in notes:
            print(f'\n******** Номер: {note["id"]} ********')
            print(f'Заголовок: {note["note_title"]}')
            print(f'{note["note_body"]}')
            print(f'Последнее изменение: {note["update_date"]}')
            print('****************************\n')

    else:
        print('\n****************************')
        print('Заметок нет')
        print('****************************\n')


def delete_note():
    """
    Запрашивает у пользователя номер заметки, удаляет заметку из списка notes,
    если не найдено выводит сообщение
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
    else:
        print(f'\nЗаметка с номером: {note_id} не найдена\n')


def edit_note():
    """
    Запрашивает у пользователя номер заметки, находит заметку в списке notes,
    запрашивает у пользователя новый заголовок и текст заметки, обновляет заметку с новой информацией
    и временными метками.
    """
    note_id = int(input('Введите номер заметки: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['note_title'] = title
            note['note_body'] = body
            note['update_date'] = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
            return
    print(f'\nЗаметка с номером: {note_id} не найдена\n')


while flag_work:
    print('1. Добавить заметку')
    print('2. Редактировать заметку')
    print('3. Удалить заметку')
    print('4. Просмотреть все заметки')
    print('5. Выход')

    choice = input('Введите номер команды: ')

    if choice == '1':
        add_note()
    elif choice == '2':
        edit_note()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        show_all_notes()
    elif choice == '5':
        flag_work = False
    else:
        print('Неверный номер команды')
