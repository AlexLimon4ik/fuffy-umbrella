import tkinter as tk
import random
import time
import calendar
import logging

# Налаштування логування
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_action(action):
    logging.info(action)

class Contact:
    def __init__(self, name, id, online_status):
        self.name = name
        self.id = id
        self.online_status = online_status

def open_chat_with_contact(frame, time_frame, contact):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    tk.Label(frame, text=f"Чат з {contact.name} (ID: {contact.id})").pack()
    chat_log = tk.Text(frame)
    chat_log.pack()
    message_entry = tk.Entry(frame)
    message_entry.pack()
    tk.Button(frame, text="Надіслати", command=lambda: chat_log.insert(tk.END, f"Ви: {message_entry.get()}\n")).pack()
    tk.Button(frame, text="O", command=lambda: create_messenger_app(frame, time_frame)).pack(side='bottom')

def create_messenger_app(frame, time_frame):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    names = ["Сашко", "Артем", "Данилко", "Маша", "Катерина", "Микола", "Петро", "Олег", "Яна", "Андрій"]
    contacts = [Contact(name, i+1, random.choice([True, False])) for i, name in enumerate(names)]
    for contact in contacts:
        status = "Онлайн" if contact.online_status else "Офлайн"
        tk.Button(frame, text=f"{contact.name} (ID: {contact.id}) - {status}", command=lambda contact=contact: open_chat_with_contact(frame, time_frame, contact)).pack()

    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

def create_music_app(frame, time_frame):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    tk.Label(frame, text="Відтворення музики...").pack()
    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

def create_calendar_app(frame, time_frame):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    year = 2024  # Змініть рік на потрібний вам
    month = 5  # Травень
    cal = calendar.month(year, month)

    tk.Label(frame, text=cal, font=("Courier", 12)).pack()

    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')


def create_weather_app(frame, time_frame):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    weather_conditions = ["Сонячно", "Хмарно", "Дощ", "Сніг", "Туманно"]
    days_of_week = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

    for day in days_of_week:
        weather = random.choice(weather_conditions)
        temperature = random.randint(-10, 30)
        tk.Label(frame, text=f"{day}: {weather}, {temperature}°C").pack()

    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

class Note:
    def __init__(self, id, content):
        self.id = id
        self.content = content

def create_notes_app(frame, time_frame, notes):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    def add_note():
        note_content = note_entry.get()
        if note_content:
            note_id = len(notes) + 1
            notes.append(Note(note_id, note_content))
            tk.Label(frame, text=f"Нотатка {note_id}: {note_content}").pack()
            note_entry.delete(0, tk.END)

    def delete_note():
        note_id_to_delete = note_entry.get()
        if note_id_to_delete:
            note_id_to_delete = int(note_id_to_delete)
            notes[:] = [note for note in notes if note.id != note_id_to_delete]
            create_notes_app(frame, time_frame, notes)

    note_entry = tk.Entry(frame)
    note_entry.pack()
    tk.Button(frame, text="Додати нотатку", command=add_note).pack()
    tk.Button(frame, text="Видалити нотатку за ID", command=delete_note).pack()

    for note in notes:
        tk.Label(frame, text=f"Нотатка {note.id}: {note.content}").pack()

    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

def create_calculator_app(frame, time_frame):
    for widget in frame.winfo_children():
        widget.destroy()
    time_frame.pack_forget()

    def evaluate(event):
        try:
            result = eval(entry.get())
            label.config(text = "Результат: " + str(result))
        except:
            label.config(text = "Неправильний вираз")

    entry = tk.Entry(frame)
    entry.bind("<Return>", evaluate)
    entry.pack(side='top')

    label = tk.Label(frame)
    label.pack(side='top')

    tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

def create_app_window(app_name, frame, time_frame):
    log_action(f"Відкрито додаток {app_name}")
    for widget in frame.winfo_children():
        widget.destroy()

    time_frame.pack_forget()
    # Приховати віджет часу
    time_frame.pack_forget()

    if app_name == "Phone":
        number_entry = tk.Entry(frame)
        number_entry.pack()
        tk.Button(frame, text="Звонити", command=lambda: tk.Label(frame, text="Телефон поза досяжності" if number_entry.get() else "Введіть номер").pack()).pack()
        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')
    elif app_name == "Bank":
        balance = random.randint(0, 10000)
        balance_label = tk.Label(frame, text="Ваш баланс: " + str(balance) + " грн")
        balance_label.pack()
        
        amount_entry = tk.Entry(frame)
        amount_entry.pack()
        
        def deposit():
            nonlocal balance
            amount = int(amount_entry.get())
            balance += amount
            balance_label.config(text="Ваш баланс: " + str(balance) + " грн")
        
        def withdraw():
            nonlocal balance
            amount = int(amount_entry.get())
            if amount <= balance:
                balance -= amount
                balance_label.config(text="Ваш баланс: " + str(balance) + " грн")
            else:
                tk.Label(frame, text="Недостатньо коштів!").pack()
        
        tk.Button(frame, text="Внести гроші", command=deposit).pack()
        tk.Button(frame, text="Зняти гроші", command=withdraw).pack()
        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')
    elif app_name == "Minesweeper":
        def create_minesweeper_grid(row=10, col=10, mines=10):
            # Create the grid with 0's
            grid = [[0 for _ in range(col)] for _ in range(row)]

            # Add mines to the grid
            for _ in range(mines):
                while True:
                    x, y = random.randint(0, row - 1), random.randint(0, col - 1)
                    if grid[y][x] == 0:
                        grid[y][x] = 'X'
                        break

            # Calculate numbers
            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    if cell != 'X':
                        values = [grid[i][j] for i in range(y - 1, y + 2)
                                for j in range(x - 1, x + 2)
                                if 0 <= i < len(grid) and 0 <= j < len(row) and grid[i][j] == 'X']
                        grid[y][x] = len(values)

            return grid

        def cell_clicked(event):
            # Get rectangle diameters
            col_width = c.winfo_width() / COLS
            row_height = c.winfo_height() / ROWS
            # Calculate column and row number
            col = int(event.x // col_width)
            row = int(event.y // row_height)
            # If the tile is not clicked, reveal the tile
            if (row, col) not in revealed:
                draw_a_cell(row, col)
                revealed.add((row, col))
                # If the cell is a mine, end the game
                if grid[row][col] == 'X':
                    tk.Label(frame, text="ВИ ПРОГРАЛИ", font=("Arial", 24)).pack()
                elif len(revealed) == ROWS * COLS - MINES:
                    tk.Label(frame, text="ВИ ВИГРАЛИ", font=("Arial", 24)).pack()

        def draw_a_cell(row, col):
            # Get rectangle diameters
            col_width = c.winfo_width() / COLS
            row_height = c.winfo_height() / ROWS
            x1 = col * col_width
            y1 = row * row_height
            x2 = x1 + col_width
            y2 = y1 + row_height
            # Draw the rectangle
            c.create_rectangle(x1, y1, x2, y2, fill="yellow")
            # Draw the text
            if grid[row][col] == 'X':
                c.create_text(x1 + col_width / 2, y1 + row_height / 2, text=grid[row][col])
            else:
                c.create_text(x1 + col_width / 2, y1 + row_height / 2, text=grid[row][col])

        ROWS, COLS, MINES = 10, 10, 10
        grid = create_minesweeper_grid(ROWS, COLS, MINES)
        revealed = set()

        c = tk.Canvas(frame, width=200, height=200)
        c.pack()

        c.bind("<Button-1>", cell_clicked)

        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')
    elif app_name == "Pizza Maker":
        tk.Label(frame, text="Ваша піцца: " + random.choice(["Маргарита", "Пеппероні", "Гавайська", "Вегетаріанська"])).pack()
        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')
    elif app_name == "Clock":
        time_label = tk.Label(frame)
        time_label.pack()
        def update_time():
            time_label.config(text="Поточний час: " + time.strftime('%H:%M:%S'))
            frame.after(1000, update_time)
        update_time()
        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')
    elif app_name == "Netflix":
        tk.Label(frame, text="Йди краще книжку почитай").pack()
        tk.Button(frame, text="O", command=lambda: create_phone_simulator(frame, time_frame)).pack(side='bottom')

def create_button(frame, text, command, app_name, time_frame):
    button = tk.Button(frame, text=text, command=command, bg='white', fg='black', width=8, height=4)
    button.grid(row=frame.row, column=frame.column, padx=5, pady=5)
    label = tk.Label(frame, text=app_name, bg='white', fg='black')
    label.grid(row=frame.row+1, column=frame.column)
    frame.column += 1
    if frame.column > 3:
        frame.column = 0
        frame.row += 2
    return button

def create_phone_simulator(frame=None, time_frame=None):
    if frame is None:
        root = tk.Tk()
        root.geometry("300x600")
        # Заборонити масштабування вікна
        root.resizable(False, False)
        frame = tk.Frame(root, bg='white')
        frame.pack()
    else:
        for widget in frame.winfo_children():
            widget.destroy()

    # Віджет часу
    if time_frame is None:
        time_frame = tk.Frame(frame, bg='white')
        time_frame.pack(side='top', fill='x', pady=100)  # Відстань в один додаток
        time_label = tk.Label(time_frame, font=("Arial", 50))  # Збільшено розмір шрифту
        time_label.pack()
        def update_time():
            time_label.config(text=time.strftime('%H:%M'))  # Показує тільки години та хвилини
            time_frame.after(60000, update_time)  # Оновлюється кожну хвилину
        update_time()
    else:
        time_frame.pack(side='top', fill='x', pady=100)  # Показати віджет часу

    # Додатки
    apps_frame = tk.Frame(frame, bg='white')
    apps_frame.pack(side='bottom', fill='both', expand=True)
    apps_frame.row = 0
    apps_frame.column = 0

    create_button(apps_frame, "📞", lambda: create_app_window("Phone", apps_frame, time_frame), "Phone", time_frame)
    create_button(apps_frame, "💰", lambda: create_app_window("Bank", apps_frame, time_frame), "Bank", time_frame)
    create_button(apps_frame, "💣", lambda: create_app_window("Minesweeper", apps_frame, time_frame), "Minesweeper", time_frame)
    create_button(apps_frame, "🍕", lambda: create_app_window("Pizza Maker", apps_frame, time_frame), "Pizza Maker", time_frame)
    create_button(apps_frame, "⏱️", lambda: create_app_window("Clock", apps_frame, time_frame), "Clock", time_frame)
    create_button(apps_frame, "💬", lambda: create_messenger_app(apps_frame, time_frame), "Messenger", time_frame)
    create_button(apps_frame, "N", lambda: create_app_window("Netflix", apps_frame, time_frame), "Netflix", time_frame)
    create_button(apps_frame, "🎵", lambda: create_music_app(apps_frame, time_frame), "Music", time_frame)
    create_button(apps_frame, "📅", lambda: create_calendar_app(apps_frame, time_frame), "Calendar", time_frame)
    create_button(apps_frame, "☀️", lambda: create_weather_app(apps_frame, time_frame), "Weather", time_frame)
    notes = []
    create_button(apps_frame, "📝", lambda: create_notes_app(apps_frame, time_frame, notes), "Notes", time_frame)
    create_button(apps_frame, "=", lambda: create_calculator_app(apps_frame, time_frame), "Calculator", time_frame)
    
    # Додайте більше кнопок тут...

    if 'root' in locals():
        root.mainloop()

create_phone_simulator()