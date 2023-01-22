# import os
# os.system("clear")

# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# list_1 = "пав пвр ап абв вавы АБВ АВвв абв"

# data = open('file_1_1', 'a')
# data.writelines(list_1)
# data.close

# list_2 = list(filter(lambda i: "абв" not in i.lower(), list_1.split()))

# data = open('file_1_2', 'a')
# data.writelines(list_2)
# data.close

# print(list_2)



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# x = 2021
# game_stop = False

# player_1 = str(input("Игрок 1, представьтесь: "))
# player_2 = str(input("Игрок 2, представьтесь: "))
# print("Система производит жеребьёвку...")
# print("...")
# print("...")

# import random
# from random import randint
# z = random.randint(1, 2)
# if z == 1:
#     print(f"Первым играет {player_1}")
# else:
#     print(f"Первым играет {player_2}")
#     z = player_1
#     player_1 = player_2
#     player_2 = z

# def player_1_move():
#     global x
#     a = int(input(f"{player_1} берёт: "))
#     if a > 28:
#         print("Вы пытаетесь нарушить правила - нельзя брать более 28 конфет! Пропустите ход.")
#     else:
#         x = x - a
#     return x

# def player_2_move():
#     global x
#     a = int(input(f"{player_2} берёт: "))
#     if a > 28:
#         print("Вы пытаетесь нарушить правила - нельзя брать более 28 конфет! Пропустите ход.")
#     else:
#         x = x - a
#     return x

# def check_game():
#     global game_stop
#     global x
#     if x > 0:
#         print(f"Конфет на столе: {x}")
#     else:
#         game_stop = True
#         print("Конфеты на столе закончились")

# check_game()
# while not game_stop:
#     player_1_move()
#     check_game()
#     if game_stop == True:
#         print(f"Победил {player_1}, все конфеты достаются ему :)")
#         break
#     player_2_move()
#     check_game()
#     if game_stop == True:
#         print(f"Победил {player_2}, все конфеты достаются ему :)")
#         break


# Создайте программу для игры в ""Крестики-нолики"".

# print("Нумерация позиций от 1 до 9 слева направо. Игроку 1 достались крестики, игроку 2 нолики")
# print("Для того чтобы сделать ход, нужно просто выбрать позицию элемента.")
# print("Убедитесь, что вводите только корректные значения, согласно правилам игры крестики-нолики")

# list_1 = ["-","-","-"]
# list_2 = ["-","-","-"]
# list_3 = ["-","-","-"]
# game_stop = False
    
# def check_game():
#     print(list_1)
#     print(list_2)
#     print(list_3)
#     global game_stop
#     if list_1 == ['x', 'x', 'x'] or list_2 == ['x', 'x', 'x'] or list_3 == ['x', 'x', 'x']:
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1[0] == "x" and list_2[0] == "x" and list_3[0] == "x":
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1[1] == "x" and list_2[1] == "x" and list_3[1] == "x":
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1[2] == "x" and list_2[2] == "x" and list_3[2] == "x":
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1[0] == "x" and list_2[1] == "x" and list_3[2] == "x":
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1[2] == "x" and list_2[1] == "x" and list_3[0] == "x":
#         game_stop = True
#         print("Игрок 1 выиграл!!!")
#     elif list_1 == ['0', '0', '0'] or list_2 == ['0', '0', '0'] or list_3 == ['0', '0', '0']:
#         game_stop = True
#         print("Игрок 2 выиграл!!!")
#     elif list_1[0] == "0" and list_2[0] == "0" and list_3[0] == "0":
#         game_stop = True
#         print("Игрок 2 выиграл!!!")
#     elif list_1[1] == "0" and list_2[1] == "0" and list_3[1] == "0":
#         game_stop = True
#         print("Игрок 2 выиграл!!!")
#     elif list_1[2] == "0" and list_2[2] == "0" and list_3[2] == "0":
#         game_stop = True
#         print("Игрок 2 выиграл!!!")
#     elif list_1[0] == "0" and list_2[1] == "0" and list_3[2] == "0":
#         game_stop = True
#         print("Игрок 2 выиграл!!!")
#     elif list_1[2] == "0" and list_2[1] == "0" and list_3[0] == "0":
#         game_stop = True
#         print("Игрок 2 выиграл!!!")

# def player_1_move():
#     a = int(input("Ход игрока 1: "))
#     if a == 1:
#         if list_1[0] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_1[0] = "x"
#     elif a == 2:
#         if list_1[1] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_1[1] = "x"
#     elif a == 3:
#         if list_1[2] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_1[2] = "x"
#     elif a == 4:
#         if list_2[0] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_2[0] = "x"
#     elif a == 5:
#         if list_2[1] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_2[1] = "x"
#     elif a == 6:
#         if list_2[2] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_2[2] = "x"
#     elif a == 7:
#         if list_3[0] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_3[0] = "x"
#     elif a == 8:
#         if list_3[1] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_3[1] = "x"
#     elif a == 9:
#         if list_3[2] == "0":
#             print("Это поле уже заполнено")
#         else:
#             list_3[2] = "x"
#     else:
#         print("позиции не существует")

# def player_2_move():
#     a = int(input("Ход игрока 2: "))
#     if a == 1:
#         if list_1[0] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_1[0] = "0"
#     elif a == 2:
#         if list_1[1] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_1[1] = "0"
#     elif a == 3:
#         if list_1[2] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_1[2] = "0"
#     elif a == 4:
#         if list_2[0] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_2[0] = "0"
#     elif a == 5:
#         if list_2[1] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_2[1] = "0"
#     elif a == 6:
#         if list_2[2] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_2[2] = "0"
#     elif a == 7:
#         if list_3[0] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_3[0] = "0"
#     elif a == 8:
#         if list_3[1] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_3[1] = "0"
#     elif a == 9:
#         if list_3[2] == "x":
#             print("Это поле уже заполнено")
#         else:
#             list_3[2] = "0"
#     else:
#         print("позиции не существует")

# print(list_1)
# print(list_2)
# print(list_3)

# while not game_stop:
#     player_1_move()
#     check_game()
#     if game_stop == True:
#         break
#     player_2_move()
#     check_game()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
