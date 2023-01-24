""" Колбэк функции """


def print_number_info(num):                 # callback-функция №1
    if (num % 2) == 0:
        print("Entered number is even")     # число парное/чётное
    else:
        print("Entered number is odd")      # число непарное/нечётное


def print_square_num(num):                  # callback-функция №2
    print("Square of the number is", num**2)


# функция вызывает другую функцию, получая как аргумент её название
def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number: '))
# entered_num = 4
process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)
