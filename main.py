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
    now_date = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y'),
    note = {
        'id': len(notes) + 1,
        'title': title,
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
            print(f'Заголовок: {note["title"]}')
            print(f'{note["note_body"]}')
            print('****************************\n')

    else:
        print('\n****************************')
        print('Заметок нет')
        print('****************************\n')


def delete_note():
    """
    Запрашивает у пользователя идентификатор заметки, удаляет заметку из списка notes
    """
    note_id = int(input('Введите номер заметки: '))
    global notes
    new_notes = [note for note in notes if note['id'] != note_id]
    notes = new_notes


while flag_work:
    print('1. Добавить заметку')
    print('2. Удалить заметку')
    print('3. Просмотреть все заметки')
    print('4. Выход')

    choice = input('Введите номер команды: ')

    if choice == '1':
        add_note()
    elif choice == '2':
        delete_note()
    elif choice == '3':
        show_all_notes()
    elif choice == '4':
        flag_work = False
    else:
        print('Неверный номер команды')
