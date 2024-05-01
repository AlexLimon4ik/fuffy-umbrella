import tkinter as tk
import random
import time
import logging

# Налаштування логування
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_action(action):
    logging.info(action)

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

    # Додайте більше кнопок тут...

    if 'root' in locals():
        root.mainloop()

create_phone_simulator()