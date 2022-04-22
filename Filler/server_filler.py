import os
import random
import math
from collections import deque
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2) # Сколько человек?

player1_name = 'Player1'
player2_name = 'Player2'

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
    
def restart_game():
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

def set_color0(y, x, col):
    global arr_colors
    cord_j = str(x)
    cord_i = str(y)
    arr_colors[int(cord_i)+1][int(cord_j)+1] = col

def chang_photo(y, x, col):
    global arr_colors
    global arr_step
    global player1
    global player2
    global player1_color
    global player2_color
    global player1_score
    global player2_score
    cord_j = str(x)
    cord_i = str(y)
    string = 'red_bred' + cord_i + '_' + cord_j
    dq = deque()
    dq.appendleft([y, x])
    if player1:
        player1_color = col
        for i in range(1, len(arr_colors)-1):
            for j in range(1, len(arr_colors[i])-1):
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
        
        if player1:
            player1_score += 1
            arr_step[t[0]+1][t[1]+1] = '1'
        else:
            player2_score += 1
            arr_step[t[0]+1][t[1]+1] = '2'
        arr_colors[t[0]+1][t[1]+1] = '-1'
        
    if player1:
        player1 = False
        player2 = True
    else:
        player1 = True
        player2 = False
    

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

def click(y, x):
    global arr_colors
    global player1
    global player2
    global player1_score
    global player2_score
    
    cord_j = x
    cord_i = y
    tmp_col = arr_colors[int(cord_i)+1][int(cord_j)+1]
    if check_next(cord_i, cord_j):
        chang_photo(int(cord_i), int(cord_j), tmp_col)
    
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
            rnd = int(random.random()*100) % 6
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

    arr_step[1][1] = '1'
    arr_step[17][26] = '2'
    player1_color = arr_colors[1][1]
    player2_color = arr_colors[17][26]
    chang_photo(0, 0, arr_colors[1][1])
    chang_photo(16, 25, arr_colors[17][26])
    arr_colors[1][1] = '-1'
    arr_colors[17][26] = '-1'
    
restart_game()

def get_click(data):
    yx = data.split(' ')
    click(yx[1], yx[2])

def get_arr_colors():
    global arr_colors
    ans = ''
    for i in range(len(arr_colors)):
        for j in range(len(arr_colors[i])):
            ans += arr_colors[i][j] + ', '
        ans = ans[:len(ans)-2]
        ans += '\n'
    return ans.encode('ascii')
    
def get_arr_step():
    global arr_step
    ans = ''
    for i in range(len(arr_step)):
        for j in range(len(arr_step[i])):
            ans += arr_step[i][j] + ', '
        ans = ans[:len(ans)-2]
        ans += '\n'
    return ans.encode('ascii')

def get_player1():
    global player1
    return str(int(player1)).encode('ascii')

def get_player2():
    global player2
    return str(int(player2)).encode('ascii')

def get_player1_color():
    global player1_color
    return player1_color.encode('ascii')

def get_player2_color():
    global player2_color
    return player2_color.encode('ascii')

def get_player1_score():
    global player1_score
    return str(player1_score).encode('ascii')

def get_player2_score():
    global player2_score
    return str(player2_score).encode('ascii')

while True:
    conn, addr = sock.accept()
    #print('conn:', addr)
    data = conn.recv(2048)
    if not data:
        break
    tmp = data.decode('utf-8').split(' ')[0]
    if tmp == 'get_click':
        get_click(data.decode('utf-8'))
        conn.send(b'Click ispolnen')
    if tmp == 'get_arr_colors':
        conn.send(get_arr_colors())
    if tmp == 'get_arr_step':
        conn.send(get_arr_step())
    if tmp == 'get_player1':
        conn.send(get_player1())
    if tmp == 'get_player2':
        conn.send(get_player2())
    if tmp == 'get_player1_color':
        conn.send(get_player1_color())
    if tmp == 'get_player2_color':
        conn.send(get_player2_color())
    if tmp == 'get_player1_score':
        conn.send(get_player1_score())
    if tmp == 'get_player2_score':
        conn.send(get_player2_score())
    if tmp == 'restart_game':
        restart_game()
        conn.send(b'Game restart')
    else:
        conn.send(b'Oshibka Brat xz chto delat...')
    #print(data.decode('utf-8'))
        
conn.close()
