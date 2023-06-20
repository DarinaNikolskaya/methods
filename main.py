import socket
import PySimpleGUI as sg
import os
import requests
from winreg import *
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

result = ''
sg.theme('LightGreen5')
layout = [  [sg.Button('Проверка подключения к интернету'), sg.Output(key = 1,)],
            [sg.Button('Проверка наличия межсетевого экрана'), sg.Output(key = 2)],
            [sg.Button('Проверка работоспособности межсетевого экрана'), sg.Output(key = 3)],
            [sg.Button('Проверка наличия антивируса'), sg.Output(key = 4)],
            [sg.Button('Проверка работоспособности антивируса'), sg.Output(key = 5)],
            [sg.Text('Вывод результата тестирования ')],
            [sg.Output(key = 6,size=(88, 20))],
            [sg.Button('Вывести результаты тестирования'),sg.Button('Сохранить результаты тестирования'),sg.Button('Выход')]
            ]
window = sg.Window('Проверка работоспособности средств безопасности ПК', layout)




while True:
    event, values = window.read()
    if event in (None, 'Выход'):
        break
    if event == 'Проверка подключения к интернету':
            try:
                socket.gethostbyaddr('www.google.com')
            except socket.gaierror:
                window[1].update('Нет подключения')
                result = '1.Данный компьютер не подключен к интернету\n'
            else:
                window[1].update('Есть подключение')
                result = '1.Данный компьютер подключен к интернету\n'
    if event == 'Проверка наличия межсетевого экрана':
        test_path = r"C:\Users\Darina\zafwSetupWeb.exe"

        if os.path.exists(test_path):
            window[2].update('Межсетевой экран установлен')
            result = result + '2.На данном компьютере межсетевой экран установлен\n'
        else:
            window[2].update('Межсетевой экран не установлен')
            result = result + '2.На данном компьютере межсетевой экран не установлен\n'
    if event == 'Проверка работоспособности межсетевого экрана':
        req = Request("https://learndb.ru//")
        response = urlopen(req).status
        if response == 200:
            window[3].update('Межсетевой экран работает')
            result = result + '3.На данном компьютере межсетевой экран работает верно\n'
        else:
            window[3].update('Межсетевой экран не работает')
            result = result + '3.На данном компьютере межсетевой экран не работает\n'

    if event == 'Проверка наличия антивируса':
        try:
            aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            aKey = OpenKey(aReg, r"SOFTWARE\KasperskyLab")
        except IOError as e:
            window[4].update("Антивирус не установлен")
            result = result + '4.На данном компьютере антивирус не установлен\n'
        else:
            window[4].update("Антивирус установлен")
            result = result + '4.На данном компьютере антивирус установлен\n'
    if event == 'Проверка работоспособности антивируса':
        try:
            my_file = open("antiv.txt", "w+")
            my_file.write("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
            my_file.readline('antiv.txt')
        except IOError as e:
            window[5].update("Антивирус работает")
            result = result + '5.На данном компьютере антивирус работает верно\n'
        else:
            window[5].update("Антивирус не работает")
            result = result + '5.На данном компьютере антивирус работает неисправно\n'
    if event == 'Вывести результаты тестирования':
        window[6].update(result)
    if event == 'Сохранить результаты тестирования':
        my_file = open("result.txt", "w+")
        my_file.write(result)

















