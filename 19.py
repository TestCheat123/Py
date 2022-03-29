def check_password(password):
    def wrapper(func):
        def wrap(*args, **kwargs):
            if input('Пароль: ') != password:
                print('Неверный пароль')
                return
            return func(*args, **kwargs)

        return wrap

    return wrapper


@check_password('password')
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print('make burgeeeeeeeeer 🍔')


make_burger(1)
