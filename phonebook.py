import os
cmd_clear = 'cls' if os.name == 'nt' else 'clear'
os.system(cmd_clear)

file = 'phonebook.txt'
new_file = 'newphonebook.txt'
title = ["ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", "ТЕЛЕФОН"]

def ask_data():
    """
    Ввод данных контакта
    """
    contact = {'second_name': input("ФАМИЛИЯ: "),
        'first_name': input("ИМЯ: "),
        'middle_name': input("ОТЧЕСТВО: ") ,
        'phone_number': input("НОМЕР ТЕЛЕФОНА: ")}
    return contact

def print_title():
    """
    Печать заголовка таблицы
    """
    print("| {:<5} \t\t| {:<5} \t\t| {:<5} \t\t| {:<5} \t|".format(*title))

def print_line(line, is_split: bool):
    """
    Печать переданной строки таблицы
    """
    if not is_split:
        line = line.strip("\n").split("; ")
    print("| {:<5} \t\t| {:<5} \t\t| {:<5} \t\t| {:<5} \t|".format(*line))
       
def add_new_contact():
    """
    Добавление контакта в телефонную книгу
    """
    os.system(cmd_clear)
    print("ЧТОБЫ ДОБАВИТЬ КОНТАКТ ВВЕДИТЕ ДАННЫЕ")
    contact = ask_data()
    with open(file, 'a', encoding='utf-8') as f:
        f.write("; ".join(contact.values()))
        f.write('\n')
    print("КОНТАКТ ДОБАВЛЕН")

def open_phonebook():
    """
    Вывод всех контактов телефонной книги
    """
    os.system(cmd_clear)
    print("ВСЕ КОНТАКТЫ:")
    print_title()
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print_line(line, False)  

def find_contact(copy_delete_switch: bool = False):
    """
    Поиск контактов в телефонной книге
    """
    if not copy_delete_switch:
        os.system(cmd_clear)
    menu_item = None
    found_lines = []
    while menu_item != "0":
        if not copy_delete_switch:
            os.system(cmd_clear)
        print(f"ПОИСК ПО:\n- 1 - ФАМИЛИИ  \n- 2 - ИМЕНИ\n- 3 - ОТЧЕСТВУ\n- 4 - НОМЕРУ ТЕЛЕФОНА\n- 0 - НАЗАД")
        counter = 0
        menu_item = input(">")
        if menu_item in ["1", "2", "3", "4"]:
            title_index = int(menu_item) - 1
            os.system(cmd_clear)
            find_what = input(f"{title[title_index]}: ")
            with open(file, 'r', encoding='utf-8') as f:
                print("РЕЗУЛЬТАТ ПОИСКА:")
                print_title()
                for line in f:
                    line = line.strip("\n").split("; ")
                    if find_what.lower() in line[title_index].lower():
                        if copy_delete_switch:
                            found_lines.append("; ".join(line) + "\n")
                            counter +=1
                            print(counter, end="")
                        print_line(line, True)
            if copy_delete_switch:
                return found_lines            
            input("НАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ")         
        elif menu_item == "0":
            pass
        else:
            print("ТАКОЙ КОМАНДЫ НЕТ, ВЫБЕРЕТЕ ДРУГУЮ")
            input("НАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ")
            os.system(cmd_clear)

def delete_contact():
    """
    Удаление контактов в телефонной книге
    """
    os.system(cmd_clear)
    print("НАЙТИ КОНТАКТ, КОТОРЫЙ ХОТИТЕ УДАЛИТЬ")
    delete_lines = find_contact(True)
    if delete_lines == [] or delete_lines == None:
        return
    print("КАКОЙ ИЗ НАЙДЕННЫХ КОНТАКТОВ ХОТИТЕ УДАЛИТЬ")
    delete_index = input("ВВЕДИТЕ НОМЕР СТРОКИ>")
    if delete_index == "":
        return
    if delete_index.isdigit():
        delete_index = int(delete_index)
        if delete_index in range(1,len(delete_lines)+1):
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            with open(file, 'w', encoding='utf-8') as f:
                for line in lines:
                    if line != delete_lines[delete_index-1]:
                        f.write(line)
            print("КОНТАКТ УДАЛЕН")
        else:
            print("СТРОКИ С ТАКИМ НОМЕРОМ НЕТ")
        
def copy_contact():
    """
    Копирование контактов в новую телефонной книге
    """
    os.system(cmd_clear)
    print("НАЙТИ КОНТАКТ, КОТОРЫЙ ХОТИТЕ СКОПИРОВАТЬ")
    copy_lines = find_contact(True)
    if copy_lines == [] or copy_lines == None:
        return
    print("КАКОЙ ИЗ НАЙДЕННЫХ КОНТАКТОВ ХОТИТЕ СКОПИРОВАТЬ")
    copy_index = input("ВВЕДИТЕ НОМЕР СТРОКИ>")
    if copy_index == "":
        return
    if copy_index.isdigit():
        copy_index = int(copy_index)
        if copy_index in range(1,len(copy_lines)+1):
            with open(new_file, 'w', encoding='utf-8') as f:
                f.write(copy_lines[copy_index-1])
                print("КОНТАКТ СКОПИРОВАН")
        else:
            print("СТРОКИ С ТАКИМ НОМЕРОМ НЕТ")     

def main():
    """
    Основное меню
    """
    menu_item = None
    while menu_item != "0":
        os.system(cmd_clear)
        print(f"Выберете что хотите сделать:\n- 1 - НАЙТИ КОНТАКТ\n- 2 - ДОБАВИТЬ КОНТАКТ\n- 3 - УДАЛИТЬ КОНТАКТ\n- 4 - ВЫВЕСТИ ВСЮ КНИГУ КОНТАКТОВ\n- 5 - КОПИРОВАТЬ КОНТАКТ В НОВУЮ КНИГУ\n- 0 - ВЫХОД")
        menu_item = input(">")
        if menu_item == "1":
            find_contact()
        elif menu_item == "2":
            add_new_contact()
        elif menu_item == "3":
            delete_contact()
        elif menu_item == "4":
            open_phonebook()
        elif menu_item == "5":
            copy_contact()
        elif menu_item == "0":
            pass
        else:
            print("ТАКОЙ КОМАНДЫ НЕТ, ВЫБЕРЕТЕ ДРУГУЮ")
        input("НАЖМИТЕ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ")
   

main()
os.system(cmd_clear)