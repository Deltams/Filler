import os
import random
import tkinter as tk
import tkinter.messagebox as mb
import math
import socket
from collections import deque

root = tk.Tk()
root.title('Filler')
root.geometry('800x640+350+100')
root.resizable(False, False)
root.bind('<Escape>', lambda e: root.destroy())
try:
    root.iconbitmap('icon.ico')
except:
    pass

photo_red_0 = tk.PhotoImage(file="img/red_0.png")
photo_red_1 = tk.PhotoImage(file="img/red_1.png")

photo_blue_0 = tk.PhotoImage(file="img/blue_0.png")
photo_blue_1 = tk.PhotoImage(file="img/blue_1.png")

photo_purple_0 = tk.PhotoImage(file="img/purple_0.png")
photo_purple_1 = tk.PhotoImage(file="img/purple_1.png")

photo_green_0 = tk.PhotoImage(file="img/green_0.png")
photo_green_1 = tk.PhotoImage(file="img/green_1.png")

photo_silver_0 = tk.PhotoImage(file="img/silver_0.png")
photo_silver_1 = tk.PhotoImage(file="img/silver_1.png")

photo_yellow_0 = tk.PhotoImage(file="img/yellow_0.png")
photo_yellow_1 = tk.PhotoImage(file="img/yellow_1.png")

holst = tk.Canvas(width=800, height=540)
holst.pack()

holst2 = tk.Canvas(width=800, height=100)
holst2.pack()

player1_name = 'Player1'
player2_name = 'Player2'

p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
sc1 = holst2.create_text(100, 35, text='0', fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
sc2 = holst2.create_text(700, 35, text='0', fill="Black", font=('Harlow Solid Italic', 16, 'normal'))

string_tag = 'red_bred'

string_color = ['red_0', 'blue_0', 'purple_0', 'green_0', 'silver_0', 'yellow_0']
arr_colors = []
arr_step = []

player1 = True
player2 = False

player1_color = '-1'
player2_color = '-1'

player1_score = 0
player2_score = 0

string_ip = 'localhost'

computer = 0 # 0 - игроки играют между собой. 1 - л. у. с. 2 - ср. у. с. и 3 - в. у. с. 4 - компьютер против компьютера

def read_file_name():
    s = ''
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\\name.txt'
    with open(file, 'r') as f:
        s = f.readline()
        s = s.replace(' ', '').split(',')
    return s

def write_file_name(s):
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\\name.txt'
    with open(file, 'w') as f:
        ans = ''
        for i in range(len(s)):
            ans += s[i] + ', '
        ans = ans[:len(ans)-2]
        f.write(ans)

def read_file_score():
    s = ''
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\score.txt'
    with open(file, 'r') as f:
        s = f.readline()
        s2 = f.readline()
        s = s.replace(' ', '').replace('\n', '').split(',')
        s2 = s2.replace(' ', '').split(',')
        ans = []
        for i in range(len(s2)):
            ans.append([s[i], s2[i]])
    return ans

def write_file_score(s):
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\score.txt'
    with open(file, 'w') as f:
        ans = ''
        for i in range(len(s)):
            ans += s[i][0] + ', '
        ans = ans[:len(ans)-2] + '\n'
        for i in range(len(s)):
            ans += s[i][1] + ', '
        ans = ans[:len(ans)-2]
        f.write(ans)
        
##def task4_desktop():
##    s = read_file()
##    if s[0] != '1':
##        s[0] = '1'
##        write_file(s)
##        file = os.path.abspath(os.path.join('BoolGame4.exe',"../../..")) + '\\task4\dist\BoolGame4.exe'
##        os.startfile(file)

def set_name():
    global p2
    global player2_name
    global player1_name
    global p1
    global player1
    global computer
    name = read_file_name()
    player1_name = name[0]
    player2_name = name[1]
    if computer == 4:
        return
    holst2.delete(p1)
    if player1:
        if computer == 0:
            holst2.delete(p2)
            p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
    else:
        if computer == 0:
            holst2.delete(p2)
            p2 = holst2.create_text(700, 10, text=player2_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))

def onclick_chr_3(event, name, name2):
    if len(name.get()) > 12:
        tmp = name.get()
        name.delete(0,tk.END)
        name.insert(0,tmp[:len(tmp)-1])
    if len(name2.get()) > 12:
        tmp = name2.get()
        name2.delete(0,tk.END)
        name2.insert(0,tmp[:len(tmp)-1])
    if len(name.get()) < 4 or len(name2.get()) < 4:
        return
        
    s = [name.get(), name2.get()]
    write_file_name(s)
    set_name()

def open_child_root3():
    child_root = tk.Toplevel(root)
    child_root.title('Параметры')
    child_root.geometry('600x400+450+220')
    child_root.resizable(False, False)
    child_root.grab_set()
    child_root.bind('<Escape>', lambda e: child_root.destroy())
    s = read_file_name()
    label_zero = tk.Label(child_root, text='', font=('Arial', 11, 'normal'), justify='left').pack(pady=25)
    fr = tk.Frame(child_root)
    label = tk.Label(fr, text='Изменение имени первого игрока', font=('Arial', 11, 'normal'), justify='left').pack(pady=20)
    name = tk.StringVar(child_root, s[0])
    text_label = tk.Entry(fr, textvariable=name, font=('Harlow Solid Italic', 14, 'normal'), width=20, justify='center')
    text_label.pack()
    fr.pack()
    fr2 = tk.Frame(child_root)
    label2 = tk.Label(fr2, text='Изменение имени второго игрока', font=('Arial', 11, 'normal'), justify='left').pack()
    name2 = tk.StringVar(child_root, s[1])
    text_label2 = tk.Entry(fr, textvariable=name2, font=('Harlow Solid Italic', 14, 'normal'), width=20, justify='center')
    text_label2.pack(pady=20)
    fr2.pack()
    child_root.bind("<Key>", lambda e: onclick_chr_3(e, text_label, text_label2))
    #Придумать сохранение имени пользователя и валидацию этих имен
    

def open_child_root2():
    child_root = tk.Toplevel(root)
    child_root.title('Топ 10')
    child_root.geometry('600x400+450+220')
    child_root.resizable(False, False)
    child_root.grab_set()
    child_root.bind('<Escape>', lambda e: child_root.destroy())
    ans = "                                         Топ 10 игроков «Филлер»\n\n\n"
    s = read_file_score()
    for i in range(len(s)):
        ans += f'                                                  {s[i][0]} : {s[i][1]}\n'
    ans += '\n\n\nЧтоб попасть в топ игроков вы должны:\n\n'
    ans += '1. Выиграть компьютер на высоком ур. сложности.\n'
    ans += '2. Набрать очков больше кого-либо в представленной выше таблице.'
    label = tk.Label(child_root, text=ans, font=('Arial', 11, 'normal'), justify='left').pack()

def open_child_root1():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('600x400+450+220')
    child_root.resizable(False, False)
    child_root.grab_set()
    child_root.bind('<Escape>', lambda e: child_root.destroy())
    ans = "                               «Филлер» — игра для двух игроков.\n\n"
    ans += 'Игра проходит на поле, состоящем из квадратных клеток\nнескольких разных цветов.\n\n'
    ans += 'В начале игры клетки раскрашены случайным образом.\n\n'
    ans += 'Каждый игрок начинает игру со своей стартовой клетки\n'
    ans += '(для Player1 - это левый верхний угол, а для Player2 - это\nправый нижний угол.)\n\n'
    ans += 'На каждом ходу игрок изменяет цвет стартовой клетки на любой\n'
    ans += 'другой — при этом все клетки, примыкающие к стартовой по стороне\nи окрашенные в тот же цвет, также перекрашиваются в выбранный цвет.\n\n'
    ans += 'Таким образом игрок «захватывает» соседние клетки, перекрашивая\nсвою область в цвет этих клеток.\n\n'
    ans += 'Игрок не может выбрать цвет, которым на этом ходу\nокрашена область противника.\n\n'
    ans += 'Цель игры состоит в захвате более половины клеток игрового поля.'
    label = tk.Label(child_root, text=ans, font=('Arial', 11, 'normal'), justify='left').pack()

def set_arr_colors(data):
    global arr_colors
    tmp = data.split('\n')
    ans = []
    for i in range(19):
        tmp[i] = tmp[i].replace(' ', '').replace('\n', '').split(',')
        ans.append(tmp[i])
    arr_colors = ans
    
def set_arr_step(data):
    global arr_step
    tmp = data.split('\n')
    ans = []
    for i in range(19):
        tmp[i] = tmp[i].replace(' ', '').replace('\n', '').split(',')
        ans.append(tmp[i])
    arr_step = ans

def set_player1(data):
    global player1
    if data == '1':
        player1 = True
    else:
        player1 = False

def set_player2(data):
    global player2
    if data == '1':
        player2 = True
    else:
        player2 = False

def set_player1_color(data):
    global player1_color
    player1_color = data

def set_player2_color(data):
    global player2_color
    player2_color = data

def set_player1_score(data):
    global player1_score
    player1_score = data

def set_player2_score(data):
    global player2_score
    player2_score = data

def get_data(string):
    global string_ip
    sock2 = socket.socket()
    sock2.connect((string_ip, 9090))
    sock2.send(string.encode('ascii'))

    data2 = sock2.recv(2048)
    sock2.close()
    return data2.decode('utf-8')

def updat_screen():
    global arr_colors
    global arr_step
    global string_tag
    global player2_name
    global player1_name
    global player1_color
    global player2_color
    global player1_score
    global player2_score
    global player1
    global player2
    global sc1
    global sc2
    global p1
    global p2
    
    holst.delete("all")
    set_arr_colors(get_data('get_arr_colors !'))
    set_arr_step(get_data('get_arr_step !'))
    set_player1(get_data('get_player1 !'))
    set_player2(get_data('get_player2 !'))
    set_player1_color(get_data('get_player1_color !'))
    set_player2_color(get_data('get_player2_color !'))
    set_player1_score(get_data('get_player1_score !'))
    set_player2_score(get_data('get_player2_score !'))

    cord_y = 30
    for i in range(1, 18):
        cord_x = 25
        for j in range(1, 27):
            string = string_tag + str(i-1) + '_' + str(j-1)
            rnd = 0
            check_col = True
            if arr_colors[i][j] == '-1' and arr_step[i][j] == '1':
                if player1_color == 'r':
                    rnd = 0
                elif player1_color == 'b':
                    rnd = 1
                elif player1_color == 'p':
                    rnd = 2
                elif player1_color == 'g':
                    rnd = 3
                elif player1_color == 's':
                    rnd = 4
                else:
                    rnd = 5
                check_col = False

            if arr_colors[i][j] == '-1' and arr_step[i][j] == '2':
                if player2_color == 'r':
                    rnd = 0
                elif player2_color == 'b':
                    rnd = 1
                elif player2_color == 'p':
                    rnd = 2
                elif player2_color == 'g':
                    rnd = 3
                elif player2_color == 's':
                    rnd = 4
                else:
                    rnd = 5
                check_col = False
            
            if check_col:
                if arr_colors[i][j] == 'r':
                    rnd = 0
                elif arr_colors[i][j] == 'b':
                    rnd = 1
                elif arr_colors[i][j] == 'p':
                    rnd = 2
                elif arr_colors[i][j] == 'g':
                    rnd = 3
                elif arr_colors[i][j] == 's':
                    rnd = 4
                else:
                    rnd = 5
                    
                if rnd == 0:
                    holst.create_image(cord_x, cord_y, image=photo_red_0, tag=string)
                elif rnd == 1:
                    holst.create_image(cord_x, cord_y, image=photo_blue_0, tag=string)
                elif rnd == 2:
                    holst.create_image(cord_x, cord_y, image=photo_purple_0, tag=string)
                elif rnd == 3:
                    holst.create_image(cord_x, cord_y, image=photo_green_0, tag=string)
                elif rnd == 4:
                    holst.create_image(cord_x, cord_y, image=photo_silver_0, tag=string)
                else:
                    holst.create_image(cord_x, cord_y, image=photo_yellow_0, tag=string)
            else:
                if rnd == 0:
                    holst.create_image(cord_x, cord_y, image=photo_red_1, tag=string)
                elif rnd == 1:
                    holst.create_image(cord_x, cord_y, image=photo_blue_1, tag=string)
                elif rnd == 2:
                    holst.create_image(cord_x, cord_y, image=photo_purple_1, tag=string)
                elif rnd == 3:
                    holst.create_image(cord_x, cord_y, image=photo_green_1, tag=string)
                elif rnd == 4:
                    holst.create_image(cord_x, cord_y, image=photo_silver_1, tag=string)
                else:
                    holst.create_image(cord_x, cord_y, image=photo_yellow_1, tag=string)
            holst.tag_bind(string, '<Button-1>', click)
            cord_x += 30
        cord_y += 30
        
    holst2.delete(sc1)
    holst2.delete(sc2)
    holst2.delete(p1)
    holst2.delete(p2)
    sc1 = holst2.create_text(100, 35, text=str(player1_score), fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    sc2 = holst2.create_text(700, 35, text=str(player2_score), fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if player1:
        p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
    else:
        p2 = holst2.create_text(700, 10, text=player2_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))

def updat_updat():
    global computer
    if computer == -1:
        root.after(200, updat_screen)
        root.after(200, updat_updat)

def next_game():
    global computer
    global player2_name
    global player1_name
    
    player2_name = read_file_name()[1]
    player1_name = read_file_name()[0]

    if computer != -1:
        computer = -1
        updat_updat()
        
    updat_screen()

def new_game():
    get_data('restart_game p')
    next_game()

dis_b = 1
def click_button_dis(text_label, button_dis):
    global dis_b
    global string_ip
    if dis_b == 1:
        button_dis.configure(text = 'Сохранить')
        text_label['state'] = 'normal'
        dis_b = 0
    else:
        string_ip = text_label.get()
        button_dis.configure(text = 'Изменить')
        text_label['state'] = 'disabled'
        dis_b = 1

def open_child_root_ip():
    global string_ip
    child_root = tk.Toplevel(root)
    child_root.title('Подключение к серверу')
    child_root.geometry('600x400+450+220')
    child_root.resizable(False, False)
    child_root.grab_set()
    child_root.bind('<Escape>', lambda e: child_root.destroy())
    label_zero = tk.Label(child_root, text='', font=('Arial', 11, 'normal'), justify='left').pack(pady=25)
    fr = tk.Frame(child_root)
    label = tk.Label(fr, text='Подключиться к IP адресу', font=('Arial', 11, 'normal'), justify='left').pack(pady=20)
    ent_text = tk.StringVar(value=string_ip)
    text_label = tk.Entry(fr, textvariable=ent_text, font=('Harlow Solid Italic', 14, 'normal'), width=20, justify='center')
    text_label.pack()
    text_label['state'] = 'disabled'
    button_dis = tk.Button(fr, text='Изменить', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=lambda: click_button_dis(text_label, button_dis))
    button_dis.pack()
    fr.pack()

def draw_menu():
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu = tk.Menu(file_menu, tearoff=0)
    help_menu2 = tk.Menu(file_menu, tearoff=0)
    help_menu.add_command(label='Легкий ур. сложности', command=easy_lvl)
    help_menu.add_command(label='Средний ур. сложности', command=average_lvl)
    help_menu.add_command(label='Высокий ур. сложности', command=hard_lvl)
    help_menu.add_command(label='Компьютер против компьютера', command=comp_vs_comp)
    file_menu.add_cascade(label='1 игрок', menu=help_menu)
    file_menu.add_command(label='2 игрока на одном pc', command=restart_game_player_2)
    help_menu2.add_command(label='Продолжить игру', command=next_game)
    help_menu2.add_command(label='Новая игра', command=new_game)
    file_menu.add_cascade(label='2 игрока локально', menu=help_menu2)
    file_menu.add_separator()
    file_menu.add_command(label='Топ 10', command=open_child_root2)
    file_menu.add_command(label='Параметры', command=open_child_root3)
    file_menu.add_command(label='Подключение к серверу', command=open_child_root_ip)
    menu_bar.add_cascade(label='Настройки', menu=file_menu)
    menu_bar.add_cascade(label='Справка', command=open_child_root1)
    root.configure(menu=menu_bar)

def onclick_key(event):
    global computer
    t = event.char.lower()
    if t == 'r' or t == 'к':
        if computer == 0:
            restart_game_player_2()
        elif computer == 1:
            easy_lvl()
        elif computer == 2:
            average_lvl()
        elif computer == 3:
            hard_lvl()
        elif computer == 4:
            comp_vs_comp()

root.bind("<Key>", onclick_key)

def comp_vs_comp():
    global computer
    global p2
    global player2_name
    global player1_name
    global p1
    holst2.delete(p1)
    holst2.delete(p2)
    player2_name = 'Computer2'
    player1_name = 'Computer1'
    p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if computer == -1:
        computer = 4
        root.after(200, comp_vs_comp)
    computer = 4
    holst.delete("all")
    create()

def hard_lvl():
    global computer
    global p2
    global player2_name
    global player1_name
    global p1
    holst2.delete(p1)
    holst2.delete(p2)
    player2_name = 'Computer'
    player1_name = read_file_name()[0]
    p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if computer == -1:
        computer = 3
        root.after(200, hard_lvl)
    computer = 3
    holst.delete("all")
    create()

def average_lvl():
    global computer
    global p2
    global player2_name
    global player1_name
    global p1
    holst2.delete(p1)
    holst2.delete(p2)
    player2_name = 'Computer'
    player1_name = read_file_name()[0]
    p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if computer == -1:
        computer = 2
        root.after(200, average_lvl)
    computer = 2
    holst.delete("all")
    create()

def easy_lvl():
    global computer
    global p2
    global player2_name
    global player1_name
    global p1
    holst2.delete(p1)
    holst2.delete(p2)
    player2_name = 'Computer'
    player1_name = read_file_name()[0]
    p2 = holst2.create_text(700, 10, text='Computer', fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if computer == -1:
        computer = 1
        root.after(200, easy_lvl)
    computer = 1
    holst.delete("all")
    create()
    

def restart_game_player_2():
    global computer
    global p2
    global player2_name
    global player1_name
    global p1
    holst2.delete(p1)
    holst2.delete(p2)
    player2_name = read_file_name()[1]
    player1_name = read_file_name()[0]
    p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
    if computer == -1:
        computer = 0
        root.after(200, restart_game_player_2)
    computer = 0
    holst.delete("all")
    create()

# Какие клетки доступны для хода? number от 1 до 2
def which_cells_available(number):
    global player1_color
    global arr_step
    global arr_colors
    ans = []
    st = set()
    for i in range(1, len(arr_step)-1):
        for j in range(1, len(arr_step[i])-1):
            if arr_step[i][j] == str(number):
                if arr_step[i][j+1] == '0' and player1_color != arr_colors[i][j+1] and (str(i) + '_' + str(j+1)) not in st:
                    ans.append([i-1, j, arr_colors[i][j+1]])
                    st.add(str(i) + '_' + str(j+1))
                if arr_step[i][j-1] == '0' and player1_color != arr_colors[i][j-1] and (str(i) + '_' + str(j-1)) not in st:
                    ans.append([i-1, j-2, arr_colors[i][j-1]])
                    st.add(str(i) + '_' + str(j-1))
                if arr_step[i+1][j] == '0' and player1_color != arr_colors[i+1][j] and (str(i+1) + '_' + str(j)) not in st:
                    ans.append([i, j-1, arr_colors[i+1][j]])
                    st.add(str(i+1) + '_' + str(j))
                if arr_step[i-1][j] == '0' and player1_color != arr_colors[i-1][j] and (str(i-1) + '_' + str(j)) not in st:
                    ans.append([i-2, j-1, arr_colors[i-1][j]])
                    st.add(str(i-1) + '_' + str(j))
    return ans

def distance_front(cell):
    global arr_step
    global arr_colors
    tmp_arr_colors = []
    for i in range(len(arr_colors)):
        tmp_ans = []
        for j in range(len(arr_colors[i])):
            tmp_ans.append(arr_colors[i][j])
        tmp_arr_colors.append(tmp_ans)
    dq = deque()
    dq.append([cell[0], cell[1]])
    ans = []
    while len(dq) > 0:
        cl = dq.popleft()
        ans.append(cl)
        if tmp_arr_colors[cl[0]+1][cl[1]+2] == cell[2]:
            dq.append([cl[0], cl[1]+1])
        if tmp_arr_colors[cl[0]+1][cl[1]] == cell[2]:
            dq.append([cl[0], cl[1]-1])
        if tmp_arr_colors[cl[0]+2][cl[1]+1] == cell[2]:
            dq.append([cl[0]+1, cl[1]])
        if tmp_arr_colors[cl[0]][cl[1]+1] == cell[2]:
            dq.append([cl[0]-1, cl[1]])
        tmp_arr_colors[cl[0]+1][cl[1]+1] = '-1'
    dist = 10000
    for i in range(len(arr_step)):
        for j in range(len(arr_step[0])):
            if arr_step[i][j] == '1':
                for q in range(len(ans)):
                    y = abs(ans[q][0] - i + 1)
                    x = abs(ans[q][1] - j + 1)
                    c = int(math.sqrt(x*x + y*y))
                    if dist > c:
                        dist = c
    return dist

##def all_late_col(player, arr_step, arr_colors, z_col):
##    dq = deque()
##    for i in range(1, len(arr_step)-1):
##        for j in range(1, len(arr_step[i])-1):
##            if arr_step[i][j] == player and arr_colors[i][j+1] != '-1' and arr_colors[i][j+1] != z_col:
##                dq.append([i, j+1])
##            if arr_step[i][j] == player and arr_colors[i][j-1] != '-1' and arr_colors[i][j-1] != z_col:
##                dq.append([i, j-1])
##            if arr_step[i][j] == player and arr_colors[i+1][j] != '-1' and arr_colors[i+1][j] != z_col:
##                dq.append([i+1, j])
##            if arr_step[i][j] == player and arr_colors[i-1][j] != '-1' and arr_colors[i-1][j] != z_col:
##                dq.append([i-1, j])
##    return list(dq)
##
##def click_late_game(dq, arr_colors, ):
##    while len(dq) != 0:
##        
##    
##
##def next_step_late_game(player, arr_step, arr_colors, step, score1, score2, col1, col2, ans):
##    if player == 1:
##        all_move = all_late_col(str(player), arr_step, arr_colors, col2)
##        
##    else:
##        all_move = all_late_col(str(player), arr_step, arr_colors, col1)
##        
##        
##
##def late_game(arr_step2, arr_colors2, col1, col2):
##    arr_step = []
##    arr_colors = []
##    copy_col1 = col1[:len(col1)]
##    copy_col2 = col2[:len(col2)]
##    
##    for i in range(len(arr_step2)):
##        ans = []
##        for j in range(len(arr_step2[i])):
##            ans.append(arr_step2[i][j])
##        arr_step.append(ans)
##    for i in range(len(arr_colors2)):
##        ans = []
##        for j in range(len(arr_colors2[i])):
##            ans.append(arr_colors2[i][j])
##        arr_colors.append(ans)
     
def step_comp2():
    cells2 = which_cells_available(2)
    if len(cells2) == 0:
        return
    rnd = int(random.random()*1000) % len(cells2)
    chang_photo(cells2[rnd][0],cells2[rnd][1], cells2[rnd][2])

##def test_comp():
##    cells = which_cells_available(2)
##    if len(cells) == 0:
##        return
##    mn = 10000
##    cell = cells[0]
##    priority_cells = []
##    for i in range(len(cells)):
##        tmp = distance_front(cells[i])
##        if tmp < mn:
##            mn = tmp
##            cell = cells[i]
##        if tmp == 1:
##            priority_cells.append(cells[i])
##    mn = 10000
##    if len(priority_cells) > 1:
##        for i in range(len(priority_cells)):
##            if priority_cells[i][0] + priority_cells[i][1] < mn:
##                mn = priority_cells[i][0] + priority_cells[i][1]
##                cell = priority_cells[i]
##            if 26 - priority_cells[i][0] + priority_cells[i][1] < mn:
##                mn = 26 - priority_cells[i][0] + priority_cells[i][1]
##                cell = priority_cells[i]
##    chang_photo(cell[0], cell[1], cell[2])
    
def step_computer(computer):
##    global arr_step
##    global arr_colors
##    late_game(arr_step, arr_colors)
##    global arr_step
    if computer == 3:
        cells = which_cells_available(2)
        if len(cells) == 0:
            return
        mn = 10000
        cell = cells[0]
        priority_cells = []
##        range_priority = []
        for i in range(len(cells)):
            tmp = distance_front(cells[i])
            if tmp < mn:
                mn = tmp
                cell = cells[i]
            #if tmp == 1 or tmp == 2:
            if tmp == 1:
                priority_cells.append(cells[i])
##                range_priority.append(tmp)
        mn = 10000
        if len(priority_cells) > 1:
            for i in range(len(priority_cells)):
##                check_nice = True
##                for j in range(len(arr_step)):
##                    if arr_step[j][priority_cells[i][1]] == '1':
##                        check_nice = False
##                if check_nice and priority_cells[i][0] + range_priority[i] < mn:
                if priority_cells[i][0] < mn:
##                    mn = priority_cells[i][0] + range_priority[i]
                    mn = priority_cells[i][0]
                    cell = priority_cells[i]
##                if check_nice and 26 - priority_cells[i][0] + range_priority[i] < mn:
                if 26 - priority_cells[i][0] < mn:
##                    mn = 26 - priority_cells[i][0] + range_priority[i]
                    mn = 26 - priority_cells[i][0]
                    cell = priority_cells[i]
        chang_photo(cell[0], cell[1], cell[2])
    elif computer == 2:
        cells = which_cells_available(2)
        if len(cells) == 0:
            return
        rnd = int(random.random()*1000) % len(cells)
        chang_photo(cells[rnd][0],cells[rnd][1], cells[rnd][2])
    elif computer == 4:
        cells1 = which_cells_available(1)
        if len(cells1) == 0:
            return
        rnd = int(random.random()*1000) % len(cells1)
        root.after(100, lambda: chang_photo(cells1[rnd][0],cells1[rnd][1], cells1[rnd][2]))
        root.after(120, lambda: step_comp2())
        
    else:
        cells = which_cells_available(2)
        if len(cells) == 0:
            return
        col_set = set()
        mx = 0
        cell = '-1'
        for i in range(len(cells)):
            if cells[i][2] not in col_set:
                col_set.add(cells[i][2])
                t = 0
                for j in range(len(cells)):
                    if cells[j][2] == cells[i][2]:
                        t += 1
                if t > mx:
                    mx = t
                    cell = cells[i]
        chang_photo(cell[0], cell[1], cell[2])
    

def set_color0(y, x, col):
    global arr_colors
    cord_j = str(x)
    cord_i = str(y)
    arr_colors[int(cord_i)+1][int(cord_j)+1] = col
    string = 'red_bred' + cord_i + '_' + cord_j
    if col == 'r':
        holst.itemconfigure(string, image=photo_red_0)
    elif col == 'b':
        holst.itemconfigure(string, image=photo_blue_0)
    elif col == 'p':
        holst.itemconfigure(string, image=photo_purple_0)
    elif col == 'g':
        holst.itemconfigure(string, image=photo_green_0)
    elif col == 's':
        holst.itemconfigure(string, image=photo_silver_0)
    else:
        holst.itemconfigure(string, image=photo_yellow_0)

def set_color1(y, x, col):
    string = 'red_bred' + str(y) + '_' + str(x)
    if col == 'r':
        holst.itemconfigure(string, image=photo_red_1)
    elif col == 'b':
        holst.itemconfigure(string, image=photo_blue_1)
    elif col == 'p':
        holst.itemconfigure(string, image=photo_purple_1)
    elif col == 'g':
        holst.itemconfigure(string, image=photo_green_1)
    elif col == 's':
        holst.itemconfigure(string, image=photo_silver_1)
    else:
        holst.itemconfigure(string, image=photo_yellow_1)

def chang_photo(y, x, col):
    global arr_colors
    global arr_step
    global player1
    global player2
    global player1_color
    global player2_color
    global player1_score
    global player2_score
    global p1
    global p2
    global sc1
    global sc2
    global holst2
    global computer
    global player2_name
    global player1_name
    cord_j = str(x)
    cord_i = str(y)
    string = 'red_bred' + cord_i + '_' + cord_j
    dq = deque()
    dq.appendleft([y, x])
    if player1:
        player1_color = col
        for i in range(1, len(arr_colors)-1):
            for j in range(1, len(arr_colors[i])-1):
                if arr_step[i][j] == '1':
                    set_color1(i-1, j-1, col)
                if arr_step[i][j] == '1' and arr_step[i][j+1] == '0' and arr_colors[i][j+1] == arr_colors[y+1][x+1]:
                    dq.append([i-1, j])
                if arr_step[i][j] == '1' and arr_step[i][j-1] == '0' and arr_colors[i][j-1] == arr_colors[y+1][x+1]:
                    dq.append([i-1, j-2])
                if arr_step[i][j] == '1' and arr_step[i+1][j] == '0' and arr_colors[i+1][j] == arr_colors[y+1][x+1]:
                    dq.append([i, j-1])
                if arr_step[i][j] == '1' and arr_step[i-1][j] == '0' and arr_colors[i-1][j] == arr_colors[y+1][x+1]:
                    dq.append([i-2, j-1])
    else:
        player2_color = col
        for i in range(1, len(arr_colors)-1):
            for j in range(1, len(arr_colors[i])-1):
                if arr_step[i][j] == '2':
                    set_color1(i-1, j-1, col)
                if arr_step[i][j] == '2' and arr_step[i][j+1] == '0' and arr_colors[i][j+1] == arr_colors[y+1][x+1]:
                    dq.append([i-1, j])
                if arr_step[i][j] == '2' and arr_step[i][j-1] == '0' and arr_colors[i][j-1] == arr_colors[y+1][x+1]:
                    dq.append([i-1, j-2])
                if arr_step[i][j] == '2' and arr_step[i+1][j] == '0' and arr_colors[i+1][j] == arr_colors[y+1][x+1]:
                    dq.append([i, j-1])
                if arr_step[i][j] == '2' and arr_step[i-1][j] == '0' and arr_colors[i-1][j] == arr_colors[y+1][x+1]:
                    dq.append([i-2, j-1])
                   
    while len(dq) != 0:
        t = dq.popleft()
        string = 'red_bred' + str(t[0]) + '_' + str(t[1])
        
        if arr_colors[t[0]+1][t[1]+1] == '-1':
            continue

        if arr_colors[t[0]+1][t[1]+1] == arr_colors[t[0]+1][t[1]+2] and arr_step[t[0]+1][t[1]+2] == '0':
            dq.append([t[0], t[1]+1])
        if arr_colors[t[0]+1][t[1]+1] == arr_colors[t[0]+2][t[1]+1] and arr_step[t[0]+2][t[1]+1] == '0':
            dq.append([t[0]+1, t[1]])
        if arr_colors[t[0]+1][t[1]+1] == arr_colors[t[0]+1][t[1]] and arr_step[t[0]+1][t[1]] == '0':
            dq.append([t[0], t[1]-1])
        if arr_colors[t[0]+1][t[1]+1] == arr_colors[t[0]][t[1]+1] and arr_step[t[0]][t[1]+1] == '0':
            dq.append([t[0]-1, t[1]])

        if col == 'r':
            holst.itemconfigure(string, image=photo_red_1)
        elif col == 'b':
            holst.itemconfigure(string, image=photo_blue_1)
        elif col == 'p':
            holst.itemconfigure(string, image=photo_purple_1)
        elif col == 'g':
            holst.itemconfigure(string, image=photo_green_1)
        elif col == 's':
            holst.itemconfigure(string, image=photo_silver_1)
        else:
            holst.itemconfigure(string, image=photo_yellow_1)
        
        if player1:
            player1_score = int(player1_score)
            player1_score += 1
            arr_step[t[0]+1][t[1]+1] = '1'
        else:
            player2_score = int(player2_score)
            player2_score += 1
            arr_step[t[0]+1][t[1]+1] = '2'
        arr_colors[t[0]+1][t[1]+1] = '-1'
        
    if player1:
        holst2.delete(p1)
        holst2.delete(p2)
        holst2.delete(sc1)
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        p2 = holst2.create_text(700, 10, text=player2_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
        sc1 = holst2.create_text(100, 35, text=str(player1_score), fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        
        player1 = False
        player2 = True
    else:
        holst2.delete(p1)
        holst2.delete(p2)
        holst2.delete(sc2)
        p1 = holst2.create_text(100, 10, text=player1_name, fill="Blue", font=('Harlow Solid Italic', 16, 'normal'))
        p2 = holst2.create_text(700, 10, text=player2_name, fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        sc2 = holst2.create_text(700, 35, text=str(player2_score), fill="Black", font=('Harlow Solid Italic', 16, 'normal'))
        
        player1 = True
        player2 = False

    if computer != 0 and computer != 4 and player2 and arr_colors[17][26] == '-1':
        step_computer(computer)
    if computer == 4 and player1:
        step_computer(computer)
    

def check_next(y, x):
    global arr_colors
    global arr_step
    global player1
    global player2
    global player1_color
    global player2_color
    cord_j = int(x)+1
    cord_i = int(y)+1
    
    if player1 and arr_colors[cord_i][cord_j] == player2_color:
        return False
    if player2 and arr_colors[cord_i][cord_j] == player1_color:
        return False
    
    if  arr_colors[cord_i][cord_j] != '-1' and \
       (arr_colors[cord_i][cord_j-1] == '-1' or \
        arr_colors[cord_i][cord_j+1] == '-1' or \
        arr_colors[cord_i-1][cord_j] == '-1' or \
        arr_colors[cord_i+1][cord_j] == '-1'):
        if player1 and \
           (arr_step[cord_i][cord_j-1] == '1' or \
            arr_step[cord_i][cord_j+1] == '1' or \
            arr_step[cord_i+1][cord_j] == '1' or \
            arr_step[cord_i-1][cord_j] == '1'):
            return True
        elif player2 and \
           (arr_step[cord_i][cord_j-1] == '2' or \
            arr_step[cord_i][cord_j+1] == '2' or \
            arr_step[cord_i+1][cord_j] == '2' or \
            arr_step[cord_i-1][cord_j] == '2'):
            return True
    return False
        
def game_over():
    global arr_step
    for i in range(1, len(arr_step)-1):
        for j in range(1, len(arr_step[i])-1):
            if arr_step[i][j] == '0' and check_next(i-1, j-1):
                return False
    return True

def click(event):
    global arr_colors
    global player1
    global player2
    global player1_score
    global player2_score
    global player1_name
    global player2_name
    global computer
    global string_ip
    
    cord_j = str(int((event.x-10)/30))
    cord_i = str(int((event.y-14)/30))

    if computer == -1:
        string  = f'get_click {cord_i} {cord_j}'
        
        sock2 = socket.socket()
        sock2.connect((string_ip, 9090))
        sock2.send(string.encode('ascii'))
        
        data2 = sock2.recv(2048)
        sock2.close()
        
        updat_screen()
    else:
        tmp_col = arr_colors[int(cord_i)+1][int(cord_j)+1]
        if check_next(cord_i, cord_j):
            chang_photo(int(cord_i), int(cord_j), tmp_col)
    if game_over():
        if player1_score == player2_score:
            mb.showinfo(title='Игра окончена', message='Ничья')
        elif player1_score > player2_score:
            if computer == 3:
                score = read_file_score()
                for i in range(len(score)):
                    if int(score[i][0]) <= player1_score:
                        if int(score[i][0]) == player1_score and score[i][1] == player1_name:
                            break
                        tmp_s = score[i][0]
                        tmp_n = score[i][1]
                        score[i][0] = str(player1_score)
                        score[i][1] = player1_name
                        for j in range(i+1, len(score)):
                            tmp2_s = score[j][0]
                            tmp2_n = score[j][1]
                            score[j][0] = tmp_s
                            score[j][1] = tmp_n
                            tmp_s = tmp2_s
                            tmp_n = tmp2_n
                        break
                write_file_score(score)
            mb.showinfo(title='Игра окончена', message=f'{player1_name} выиграл!')
        else:
            mb.showinfo(title='Игра окончена', message=f'{player2_name} выиграл!')

def create():
    global arr_colors
    global arr_step
    global player1
    global player2
    global string_color
    global player1_color
    global player2_color
    global player1_score
    global player2_score
    player1_score = 0
    player2_score = 0
    player1 = True
    player2 = False
    player1_color = '-1'
    player2_color = '-1'
    arr_colors = []
    arr_step = []
    for i in range(0, 17+2):
        ans = []
        ans2 = []
        for j in range(0, 26+2):
            ans.append('*')
            ans2.append('-1')
        arr_colors.append(ans)
        arr_step.append(ans2)
    
        
    cord_y = 30
    for i in range(0, 17):
        cord_x = 25
        for j in range(0, 26):
            string = string_tag + str(i) + '_' + str(j)
            rnd = int(random.random()*100) % 6
            if rnd == 0:
                holst.create_image(cord_x, cord_y, image=photo_red_0, tag=string)
            elif rnd == 1:
                holst.create_image(cord_x, cord_y, image=photo_blue_0, tag=string)
            elif rnd == 2:
                holst.create_image(cord_x, cord_y, image=photo_purple_0, tag=string)
            elif rnd == 3:
                holst.create_image(cord_x, cord_y, image=photo_green_0, tag=string)
            elif rnd == 4:
                holst.create_image(cord_x, cord_y, image=photo_silver_0, tag=string)
            else:
                holst.create_image(cord_x, cord_y, image=photo_yellow_0, tag=string)
            holst.tag_bind(string, '<Button-1>', click)
            cord_x += 30
            arr_colors[i+1][j+1] = string_color[rnd][0]
            arr_step[i+1][j+1] = '0'
        cord_y += 30

    for q in range(0, 43):
        for i in range(0, 17):
            for j in range(0, 26):
                if i + j > q:
                    break
                if i + j == q:
                    rnd = int(random.random()*100) % 6
                    set_color0(i, j, string_color[rnd][0])
    
    while arr_colors[1][1] == arr_colors[17][26]:
        rnd = int(random.random()*100) % 6
        set_color0(0, 0, string_color[rnd][0])

    while arr_colors[1][2] == arr_colors[2][1]:
        rnd = int(random.random()*100) % 6
        set_color0(0, 1, string_color[rnd][0])

    while arr_colors[-2][-3] == arr_colors[-3][-2]:
        rnd = int(random.random()*100) % 6
        set_color0(len(arr_colors)-3, len(arr_colors[0])-4, string_color[rnd][0])

##    for i in range(len(arr_colors)):
##        print(arr_colors[i])
##    print()
    arr_step[1][1] = '1'
    arr_step[17][26] = '2'
    player1_color = arr_colors[1][1]
    player2_color = arr_colors[17][26]
    chang_photo(0, 0, arr_colors[1][1])
    chang_photo(16, 25, arr_colors[17][26])
    arr_colors[1][1] = '-1'
    arr_colors[17][26] = '-1'
    

draw_menu()  
create()
set_name()


root.mainloop()
