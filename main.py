from pypass import PasswordStore


def main():
    store = PasswordStore()
    passwords = store.get_passwords_list()
    for pw in passwords:
        print(store.get_decypted_password(pw))


if __name__ == '__main__':
    main()
