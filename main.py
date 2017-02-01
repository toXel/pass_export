import csv
from pypass import PasswordStore, EntryType


def main():
    store = PasswordStore()
    passwords = store.get_passwords_list()
    with open('pass.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for pw in passwords:
            csvwriter.writerow([store.get_decypted_password(pw, EntryType.password), store.get_decypted_password(pw)])


if __name__ == '__main__':
    main()
