

import os

data = []
path =  'tel_dict.txt'
dir = os.path.dirname(os.path.realpath(__file__)) + '\\'
full_path = dir + path

def f_exit():
    print ('Выход')

def f_load():
    tel_dict = open(full_path, 'r', encoding='utf-8')
    with open(full_path, 'r', encoding='utf-8') as tel_dict:
        for line in tel_dict:
            n = line.split()
            dict_ = {
                "l_name": n[0],
                "f_name": n[1],
                "s_name": n[2],
                "tel": n[3],
            }
            data.append(dict_)
    return None

def f_add():
    data_file = open(path, 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами: ")
    data_file.write(f'{s}\n')
    data_file.close()

def f_print():
    for item in data:
          print(*(f"{v}" for v in item.values()))
    
def f_find():
    find_txt = input("Введите фамилию: ")
    for item in data:
        if item["l_name"] == find_txt.capitalize():
            print(item)

def f_copy():

#    file_new = open('new_' + path,'w')
    in_line_num = int(input("Введите номер строки: "))
    with open(full_path, encoding='utf-8') as file_d:
        f_lines = file_d.readlines()
        if in_line_num <= len(f_lines):
            for line_n, line in enumerate(f_lines):
                if (line_n+1) == in_line_num:
                    with open(dir + 'new_' + path,'w+', encoding='utf-8') as file_new:
                        file_new.write(line)
        else:
            print('Такой строки нет')


menu = [{'id': '0', 'desc': 'Выход', 'func': f_exit},
        {'id': '1', 'desc': 'Печать', 'func': f_print},
        {'id': '2', 'desc': 'Новый контакт', 'func': f_add },
        {'id': '3', 'desc': 'Найти', 'func': f_find },
        {'id': '4', 'desc': 'Скопировать', 'func': f_copy }
]

def main ():
    sel_n = 100
    f_load()
    for it in menu:
        print (it['id'], it['desc'])
    while sel_n != 0:
        sel_n = int(input('Выберите действие:'))
        
        if sel_n < len (menu):
            # print(m[sel_n]['func'])
            menu[sel_n]['func']()
        else:
            break


if __name__ == "__main__":
    main()