from faker import Faker

fake = Faker()


def get_random_username():
    username = fake.first_name()
    return username


def get_random_password():
    password = fake.password(length=6)
    return password


def get_random_email():
    email = fake.free_email()
    return email
