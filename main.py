import csv
import re
from os import path

from pypass import EntryType, PasswordStore


def parse(pass_entry, store):
    name = path.basename(pass_entry)

    # Use the parsers from pypass
    username = store.get_decypted_password(pass_entry, EntryType.username)
    password = store.get_decypted_password(pass_entry, EntryType.password)

    # Parse more data from the entry
    entry_text = store.get_decypted_password(pass_entry)
    url = parse_url(entry_text)
    hostname = parse_host(entry_text)
    notes = parse_notes(entry_text)
    return [name, username, password, hostname, url, notes]


def parse_url(pass_text):
    url = re.search('(?i:url): (.+)', pass_text)
    if url:
        return url.groups()[0]


def parse_host(pass_text):
    "Polyfill for the host parse function of pypass because there is a bug in it"
    hostname = re.search('(?:host|hostname): (.+)', pass_text)
    if hostname:
        return hostname.groups()[0]


def parse_notes(pass_text):
    lines = pass_text.splitlines(keepends=True)

    # Remove first line if it is the password
    if not re.search('(?:password|pass): (.+)', pass_text):
        lines = lines[1:]

    regx = re.compile('(?i:user|username|login|pass|password|host|hostname|url): (.+)')
    lines = [line for line in lines if not regx.match(line)]
    return ''.join(lines)


def main():
    store = PasswordStore()
    entries = store.get_passwords_list()
    with open('pass.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for entry in entries:
            csvwriter.writerow(parse(entry, store))


if __name__ == '__main__':
    main()
