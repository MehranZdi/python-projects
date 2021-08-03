from collections import defaultdict
from os import path
import json


# class PhoneBook():
#     def __init__(self):
#
#
def existence_checking(phone_book, name):

    existence_checker = phone_book[name]

    if existence_checker != "Not Exist.":
        existence_checker = True
    else:
        existence_checker = False

    return existence_checker


def add_number(phone_book_dict):

    full_name = input("Enter the full name: \n")

    boolean_result = existence_checking(phone_book_dict, full_name)

    if boolean_result == True:
        print(f' {full_name} already exists.')
    else:
        phone_number = int(input("Enter the phone number: \n"))
        phone_book_dict[full_name] = phone_number

    return phone_book_dict


def search():
    pass



''' Test Cases'''


if __name__ == "__main__":

    phone_book_dict = defaultdict(lambda: "Not Exist.")
    keep_doing = 'yes'

    while keep_doing == 'yes':
        phone_book_dict = add_number(phone_book_dict)
        keep_doing = input("If you want to keep adding, type 'YES', otherwise type 'NO'.").lower()

    with open('Phone_Book.txt', 'w') as file:
        file.write(json.dumps(phone_book_dict))