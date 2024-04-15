import webbrowser

def validator(func):
    def wrapper(url):
        print("Код до виконання функції")
        func(url)
        print("Код після виконання функції")
    return wrapper

@validator
def hehehe(url):
    webbrowser.open(url)

hehehe("https://www.youtube.com/shorts/eAaTVhxZEJk")


