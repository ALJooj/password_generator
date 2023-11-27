import random
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import Dict, Any
import string
import sqlite3


app = FastAPI()

ul_set = string.ascii_letters
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
password TEXT NOT NULL,
name TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()




@app.get('/api')
def hello_world():
    return {"answer": "hello world"}


@app.post('/api')
def hello_world(event: Dict[Any, Any]):
    password = generate_password(event['len'], event['useNumbers'], event['useSpec'])
    store_password_to_paper(password, event['name'])
    return password


@app.get('/get_from_db')
def return_last_generated_pass():
    connection_local = sqlite3.connect('data.db')
    cursor_local = connection_local.cursor()
    cursor_local.execute('SELECT MAX(id), password FROM Users')
    password = cursor_local.fetchone()
    connection_local.commit()
    connection_local.close()

    return {"id": password[0], "password": password[1]}


@app.get('/all_passwords')
def send_all_passes():
    data = get_all_passwords()
    return {'all_data': data}


def get_all_passwords():
    connection_local = sqlite3.connect('data.db')
    cursor_local = connection_local.cursor()
    cursor_local.execute('SELECT * FROM Users')
    users = cursor_local.fetchall()
    print('users', users)
    connection_local.commit()
    connection_local.close()
    return users


def store_password_to_paper(data: str, name: str):
    connection_local = sqlite3.connect('data.db')
    cursor_local = connection_local.cursor()
    cursor_local.execute('INSERT INTO Users (password, name) VALUES (?, ?)', (data, name))

    connection_local.commit()
    connection_local.close()


def generate_password(length, use_number, use_spec):
    full_list = ul_set[:]
    if use_number:
        full_list += string.digits
    if use_spec:
        full_list += '!@#$%^&*?'
    answer = ''

    for i in range(length):
        answer += random.choice(full_list)
    return answer
