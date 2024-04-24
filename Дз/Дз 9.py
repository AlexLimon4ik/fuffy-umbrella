# Завдання 1 Нейросіть допомогла

# import requests

# class CurrencyConverter:
#     def __init__(self):
#         self.url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
#         self.data = requests.get(self.url).json()
#         self.usd_rate = self.get_usd_rate()

#     def get_usd_rate(self):
#         for currency in self.data:
#             if currency['cc'] == 'USD':
#                 return currency['rate']

#     def convert_to_usd(self, amount):
#         return amount / self.usd_rate

# converter = CurrencyConverter()
# amount = float(input("Enter the amount in UAH: "))
# print(f"The equivalent amount in USD is {converter.convert_to_usd(amount)}")


# Завдання 2
# import requests
# from tkinter import Tk, Label, Entry, Button, StringVar

# class CurrencyConverter:
#     def __init__(self):
#         self.url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
#         self.data = requests.get(self.url).json()
#         self.usd_rate = self.get_usd_rate()

#     def get_usd_rate(self):
#         for currency in self.data:
#             if currency['cc'] == 'USD':
#                 return currency['rate']

#     def convert_to_usd(self, amount):
#         return amount / self.usd_rate

# def convert():
#     amount = float(amount_entry.get())
#     result.set(f"The equivalent amount in USD is {converter.convert_to_usd(amount)}")

# converter = CurrencyConverter()

# root = Tk()
# root.title("Currency Converter")

# amount_label = Label(root, text="Enter the amount in UAH:")
# amount_label.pack()

# amount_entry = Entry(root)
# amount_entry.pack()

# result = StringVar()
# result_label = Label(root, textvariable=result)
# result_label.pack()

# convert_button = Button(root, text="Convert", command=convert)
# convert_button.pack()

# root.mainloop()
