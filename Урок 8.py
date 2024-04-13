import logging

# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
# logging.debug('debug message')
# logging.info('info message')

# з використанням параметру форматування 
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
# logging.debug('debug')
# logging.info('info')

# try:
#     print(10/10)
# except Exception:
#     logging.exception("Exception occurred")


# Завдання: Записати повідомленя рівня іnfо у файл i за допомогою модуля Logging, що повідомляє користувача про успішний запуск програми

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
logging.info('The program is working')