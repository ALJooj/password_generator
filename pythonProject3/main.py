import random
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import Dict, Any
import string
import sqlite3


app = FastAPI()

# ul_set = string.ascii_letters
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

# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()

# Создаем таблицу Users
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# password TEXT NOT NULL,
# name TEXT NOT NULL
# )
# ''')

# Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()




@app.get('/api')
def hello_world():
    return {"answer": "hello world"}

@app.post('/api')
def post_method(event: Dict[Any, Any]):
    return {"answer": "hello world"}



# @app.post('/api')
# def hello_world(event: Dict[Any, Any]):
#     password = generate_password(event['len'], event['useNumbers'], event['useSpec'])
#     store_password_to_paper(password, event['name'])
#     return password


@app.get('/all_passwords')
def send_all_passes():
    data = ['hello']
    return {'all_data': data}

