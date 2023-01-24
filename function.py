from datetime import date


def increase_person_age(person):
    """ Изменение параметра в изменяемом объекте.
        При использовании функции и локальной перемнной, 
        на самом деле изменяется и глобальная переменная.
        ВНУТРИ ФУНКЦИИ НЕ РЕКОМЕНДУЕТЬСЯ ИЗМЕНЯТЬ ВНЕШНИЕ ОБЪЕКТЫ.
    """
    print('Funcrion increase_person_age(person)         ')
    print('person                                       ', person)
    print('person id                                    ', id(person))
    person['age'] += 1
    return person


def increase_person_age_copy(person):
    """ Изменение параметра в изменяемом объекте путём создания её локальной копии.
        Создаём новый объект, изменяем его и возвращаем.
        Оригинальный объект при этом не изменяеться.
    """
    print('Funcrion increase_person_age_copy(person)    ')
    print('person                                       ', person)
    print('person id                                    ', id(person))
    person_copy = person.copy()

    person_copy['age'] += 1
    return person_copy


def merge_list_to_dict(list1, list2):
    """ Функция объединения двух списков в один словарь
    """
    ziped_tuple = zip(list1, list2)
    merged_dict = dict(ziped_tuple)
    return merged_dict


def sum_nums(*args):
    """ Функция, котороую можно вызвать с любым количеством аргументов.
        Аргументы переадются в виде кортежа.
    """
    print(args)
    print(type(args))
    for i, n in enumerate(args):
        print(f'args[{i}]={args[i]}')
    return sum(args)

# from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 234,
    'author': 'Roman',
}


fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]


person_one = {
    'name': 'Roman',
    'age': 30
}


print('person_one                                   ', person_one)
print('person_one id                                ', id(person_one))

increase_person_age(person_one)
print('person_one                                   ', person_one)


print('increase_person_age_copy(person_one)         ',
      increase_person_age_copy(person_one))
print('person_one                                   ', person_one)

print()
print("fruits = ['apple', 'banana', 'lime']     -> ", fruits)
print("quantities = [100, 70, 50]               -> ", quantities)
print("merge_list_to_dict(list1, list2)         -> ",
      merge_list_to_dict(fruits, quantities))
print()
print('sum_nums()=', sum_nums(2, 3, 7, 9, 5, 1, 8))

print()
post_with_weekday = create_new_post(initial_post)
print('post_with_weekday = create_new_post(initial_post) ', post_with_weekday)
print()
print(dir(date))
