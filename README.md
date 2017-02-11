# pass_export
**WORK IN PROGRESS**

This little tool exports passwords from [pass](http://passwordstore.org) to other password managers.

At the moment it spits out a CSV file with the following columns:

| Group | Title | Username | Password | Hostname | URL | Notes |
| ----- | ----- | -------- | -------- | -------- | --- | ----- |

The resulting file could for example used with the generic CSV import from Enpass.

**WARNING!** This decrypts all your pass entries and writes them into a plain CSV file so use it with caution!
