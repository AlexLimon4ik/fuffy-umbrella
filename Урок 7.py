
# my_list = [1, 2, 3]
# iterator = iter(my_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for elem in iterator:
#     print(elem)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number

#     def __iter__(self):
#         self.i = 0
#         return self
    
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
    
# count = Counter(5)
# for elem in count:
#     print(elem)
  
# def raise_to_the_degress(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**1
#         i+=1
# res = raise_to_the_degress(122345, 500)
# print(res)
# for _ in res:
#     print(_)

# class Helper:
#     def __init__(self, work):
#         self.work = work
    
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help with {work}"
    
# helper = Helper("pomenat podguznik")
# print(helper("homework"))

# import webbrowser

# def validator(func):
#     def wrapper(url):
#         if "https://" in url:
#             func(url)
#         else:
#             print("В посиланні помилка")
#     return wrapper

# @validator
# def open_url(url):
#     webbrowser.open(url)

# open_url("https://itstep.org/uk")