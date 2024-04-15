# import logging

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
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
# logging.info('The program is working')


# if 2+2 == 4:
#     print("In fact, 2+2 equals 4")

# assert 2 + 2 == 5, "wrong assert"


# """
# >>> assertion
# result
# """
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


# переходить у файл тест
# def adder(*args, **kwagrs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwagrs.values():
#         result += _
#         return result