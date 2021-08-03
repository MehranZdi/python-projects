from os import path
import json


def existence_checking(phone_book, name):
    try:
        existence_checker = phone_book[name]
        flag = True

    except KeyError:
        flag = False

    return flag


def add_number(phone_book):

    full_name = input("Enter the full name: \n")
    # print(f'Phone Book looks like this: {phoneBook_dict}')
    boolean_result = existence_checking(phone_book, full_name)

    if boolean_result:
        print(f' {full_name} already exists.')

    else:
        while True:
            try:
                phone_number = int(input("Enter the phone number: \n"))
                phone_book[full_name] = phone_number
                break

            except ValueError:
                print(" ---- Oops! You entered a wrong phone number, please try again:")

    return phone_book


def search():
    pass


def modify_contact():
    pass


def show_contacts(phone_book):

    for key in phone_book:
        print(f' {key}: {phone_book[key]} \n ')



''' Test Cases'''


if __name__ == "__main__":

    phone_book_path = '/home/mehranz/PycharmProjects/Personal_Projects/Phone_Book.txt'  # my local system path

    if path.exists(phone_book_path):

        with open("Phone_Book.txt") as file:
            d = file.read()
        phone_book_ = json.loads(d)
        phone_book_dict = phone_book_

    else:
        phone_book_dict = dict()

    keep_doing = 'yes'

    while keep_doing == 'yes':
        phone_book_dict = add_number(phone_book_dict)

        keep_doing = input("If you want to keep adding, type 'YES', otherwise type 'NO'.  ").lower()

        while True:
            if (keep_doing != 'yes') and (keep_doing != 'no'):
                print("---- Oops! You entered wrong answer. Just answer the question with 'Yes' or 'No'. ----")
                keep_doing = input("If you want to keep adding, type 'YES', otherwise type 'NO':  ").lower()
            else:
                break

    with open('Phone_Book.txt', 'w') as file:
        file.write(json.dumps(phone_book_dict))

    show_contacts(phone_book_dict)