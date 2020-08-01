# Journal

This Journal allows the user to add journal entries and view their titles. Implemented with Python and used JSON to save journal entries.

## Getting Started
Download journal.py and in your terminal go to the folder where you saved it.

### Adding An Entry
In your terminal, run the following to add a new entry to your journal
```console
foo@bar:~$ ./journal.py --create "Stephen Hawking was one of the most well known physicists in the world, and was diagnosed with ALS when he was 21" --title "Stephen Hawking"
```

### Listing Entry Titles

In your terminal run the following to view all the titles of your journal entries
```console
foo@bar:~$ ./journal.py --list

Your Entry Titles:
==================
1. Stephen Hawking

```
