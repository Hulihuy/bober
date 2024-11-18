import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        password_var.set("Введите положительное число")
        return

    use_lower = True  # Всегда используем строчные буквы
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        password_var.set("Выберите хотя бы один тип символов")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Обновить состояние буфера обмена
        status_var.set("Скопировано в буфер обмена")
    else:
        status_var.set("Нет пароля для копирования")

root = tk.Tk()
root.title("Генератор паролей")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Настройка длины пароля
ttk.Label(frame, text="Длина пароля:").grid(row=0, column=0, sticky=tk.W, pady=5)
length_var = tk.StringVar(value='12')
length_entry = ttk.Entry(frame, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

# Кнопка для переключения верхнего регистра
upper_var = tk.BooleanVar(value=True)
upper_button = ttk.Checkbutton(
    frame,
    text="Использовать заглавные буквы",
    variable=upper_var
)
upper_button.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

# Кнопка для переключения цифр
digits_var = tk.BooleanVar(value=True)
digits_button = ttk.Checkbutton(
    frame,
    text="Использовать цифры",
    variable=digits_var
)
digits_button.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

# Кнопка для переключения специальных символов
special_var = tk.BooleanVar(value=True)
special_button = ttk.Checkbutton(
    frame,
    text="Использовать специальные символы",
    variable=special_var
)
special_button.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)

# Кнопка генерации пароля
generate_button = ttk.Button(frame, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Поле для отображения сгенерированного пароля
password_var = tk.StringVar()
password_entry = ttk.Entry(frame, textvariable=password_var, width=30, state='readonly')
password_entry.grid(row=5, column=0, columnspan=2, pady=5)

# Кнопка копирования в буфер обмена
copy_button = ttk.Button(frame, text="Копировать", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=5)

# Поле для отображения статуса
status_var = tk.StringVar()
status_label = ttk.Label(frame, textvariable=status_var, foreground='green')
status_label.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
