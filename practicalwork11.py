# -*- coding: utf-8 -*-

import requests
import json
import tkinter as tk

def get_data():
    username = entry.get()

    url = f"https://api.github.com/users/{username}"

    user_data = requests.get(url).json()

    data = {
        "company": user_data["company"],
        "created_at": user_data["created_at"],
        "email": user_data["email"],
        "id": user_data["id"],
        "name": user_data["name"],
        "url": user_data["url"]
    }

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    result_label.config(text="Данные сохранены в data.json")

window = tk.Tk()
window.title("Получение данных GitHub")
window.geometry("400x200")

label = tk.Label(window, text="Введите имя пользователя GitHub:")
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

entry.insert(0, "ansible")

button = tk.Button(window, text="Получить данные", command=get_data)
button.pack(pady=15)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()