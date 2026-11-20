from functools import wraps

# Декоратор для обробки помилок
def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ZeroDivisionError:
            print("Помилка: ділення на нуль!")

        except Exception:
            print("Помилка! Перевірте правильність виразу.")

    return wrapper


# Функція калькулятора
@error_handler
def calculate(expression):
    return eval(expression, {"__builtins__": {}})


# Перевірка калькулятора
print(calculate("10 + 5"))
print(calculate("20 / 4"))
print(calculate("10 / 0"))
print(calculate("abc + 5"))
