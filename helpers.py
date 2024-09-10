from faker import Faker

fakeRU = Faker(locale='ru_RU')


def email_generator():
    fake = Faker()
    return fake.email()


def password_generator():
    fake = Faker()
    return fake.password(10, True, True, True, True)


def create_random_name():
    username = fakeRU.first_name()
    return username
