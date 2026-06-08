import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма заявки")
root.geometry("620x550")
root.configure(bg="black")

# Главный контейнер с белыми границами
main_frame = tk.Frame(root, bg="#f0f0f0", bd=4, relief="ridge")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Шапка
header = tk.Label(main_frame, text="Форма заявки", bg="#009663", fg="white", font=("Arial", 14, "bold"), pady=5)
header.pack(fill="x")

# Информационный блок
info_text = (
    "Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
    "Макс. размер каждого файла: 1024kb.\n"
    "Макс. общий размер файла: 2048kb."
)
info_label = tk.Label(main_frame, text=info_text, bg="#f0f0f0", justify="left", font=("Arial", 10, "bold"), anchor="w", padx=10, pady=5)
info_label.pack(fill="x")

# Сетка для полей ввода
grid_frame = tk.Frame(main_frame, bg="#f0f0f0", padx=10, pady=5)
grid_frame.pack(fill="x")

grid_frame.columnconfigure(0, weight=1)
grid_frame.columnconfigure(1, weight=2)
grid_frame.columnconfigure(2, weight=1)

fields = ["Ваше имя:", "Ваш Email:", "Тема письма:"]
entries = {}

for i, field in enumerate(fields):
    lbl = tk.Label(grid_frame, text=field, bg="#f0f0f0", font=("Arial", 11), anchor="w")
    lbl.grid(row=i, column=0, sticky="we", pady=5)
    
    # Контейнер для поля и звездочки
    entry_container = tk.Frame(grid_frame, bg="#f0f0f0")
    entry_container.grid(row=i, column=1, columnspan=2, sticky="we", pady=5)
    
    ent = tk.Entry(entry_container, font=("Arial", 11), bd=1, relief="solid")
    ent.pack(side="left", fill="x", expand=True)
    entries[field] = ent
    
    if field in ["Ваше имя:", "Ваш Email:"]:
        star = tk.Label(entry_container, text="*", fg="red", bg="#f0f0f0", font=("Arial", 12, "bold"))
        star.pack(side="left", padx=5)

# Поля прикрепления файлов
for i in range(3):
    row_idx = len(fields) + i
    lbl = tk.Label(grid_frame, text="Прикрепить файл:", bg="#f0f0f0", font=("Arial", 11), anchor="w")
    lbl.grid(row=row_idx, column=0, sticky="we", pady=5)
    
    ent = tk.Entry(grid_frame, font=("Arial", 11), bd=1, relief="solid")
    ent.grid(row=row_idx, column=1, sticky="we", pady=5, padx=(0, 5))
    
    btn = tk.Button(grid_frame, text="Обзор...", font=("Arial", 10), bd=2, relief="raised")
    btn.grid(row=row_idx, column=2, sticky="we", pady=5)

# Сообщение
msg_label_frame = tk.Frame(main_frame, bg="#f0f0f0", padx=10)
msg_label_frame.pack(fill="x")

msg_lbl = tk.Label(msg_label_frame, text="Ваше сообщение:", bg="#f0f0f0", font=("Arial", 11))
msg_lbl.pack(side="left")
msg_star = tk.Label(msg_label_frame, text="*", fg="red", bg="#f0f0f0", font=("Arial", 12, "bold"))
msg_star.pack(side="left")

text_frame = tk.Frame(main_frame, bg="#f0f0f0", padx=10, pady=5)
text_frame.pack(fill="both", expand=True)

text_area = tk.Text(text_frame, bd=1, relief="solid", highlightcolor="#00a8e8", highlightbackground="#00a8e8", highlightthickness=1)
text_area.pack(fill="both", expand=True)

# Нижняя панель с кнопками
button_frame = tk.Frame(main_frame, bg="#009663", pady=8)
button_frame.pack(fill="x", side="bottom")

btn_send = tk.Button(button_frame, text="Отправить Email", font=("Arial", 11), bd=2, relief="raised")
btn_send.pack(side="left", padx=(130, 10), ipadx=10)

btn_clear = tk.Button(button_frame, text="Отчистить", font=("Arial", 11), bd=2, relief="raised")
btn_clear.pack(side="left", ipadx=15)

root.mainloop()
