import tkinter as tk
from tkinter import messagebox

def calculate_thousands():
    try:
        num = int(entry_num.get())
        if num <= 999:
            messagebox.showerror("Ошибка", "Число должно быть больше 999!")
            return
        
        
        result = (num // 1000) % 10
        
        label_result.config(text=f"Цифра в разряде тысяч: {result}", fg="green")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число!")


window = tk.Tk()
window.title("Вариант 23 — Разряд тысяч")
window.geometry("400x200")
window.configure(padx=20, pady=20)


label_instruction = tk.Label(window, text="Введите целое число (> 999):", font=("Arial", 11))
label_instruction.pack(pady=5)

entry_num = tk.Entry(window, font=("Arial", 12), justify="center")
entry_num.pack(pady=5, fill="x")

btn_calc = tk.Button(window, text="Вычислить разряд", font=("Arial", 11, "bold"), bg="#009663", fg="white", command=calculate_thousands)
btn_calc.pack(pady=15)

label_result = tk.Label(window, text="Цифра в разряде тысяч: -", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

window.mainloop()
