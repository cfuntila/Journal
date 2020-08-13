# Journal

This Journal allows the user to add journal entries and view their titles. Implemented with Python and used JSON to save journal entries.

## Getting Started
Download journal.py and in your terminal go to the folder where you saved it.

### Adding an entry
In your terminal, run the following to add a new entry to your journal.
```console
foo@bar:~$ ./journal.py --create "Stephen Hawking was one of the most well known physicists in the world, and was diagnosed with ALS when he was 21" --title "Stephen Hawking"


```

### Listing entry titles

In your terminal run the following to view all the titles of your journal entries.
```console
foo@bar:~$ ./journal.py --list

Your Entry Titles:
==================
1. Stephen Hawking

```


### Deleting an entry

In your terminal run the following to delete an entry. You must enter the number that corresponds to the entry you want to delete, use the "-l" flag to figure out which number of the entry you want to delete.
```console
foo@bar:~$ ./journal.py --delete 1
foo@bar:~$ ./journal.py -l

Your Entry Titles:
==================

```

### Update title for a specific entry

In your terminal run the following to update the title of an entry. You must enter the entry id (shown when you list out the entries "entry id") that corresponds to the entry you want to update. You must also include the new title.
```console
foo@bar:~$ ./journal.py -l

Your Entry Titles:
==================
1. Stephen Hawking, entry id: 1

foo@bar:~$ ./journal.py --changeTitle 1 --new "Stephen William Hawking"
foo@bar:~$ ./journal.py -l

Your Entry Titles:
==================
1. Stephen William Hawking, entry id: 1

```

### Search for an entry with a specific string

In your terminal run the following to search for all the entries that have a string provided by you. You must include the new title.
```console
foo@bar:~$ ./journal.py --search "Stephen"

Your Entries:
==================
1. Title: Stephen William Hawking
   Content: Stephen Hawking was one of the most well known physicists in the world, and was diagnosed with ALS when he was 21
   Entry id: 1

```


### List out both the title and content of all entries

In your terminal run the following to list all details of your entries.
```console
foo@bar:~$ ./journal.py -v

Your Entries:
==================
1. Title: Stephen William Hawking
   Content: Stephen Hawking was one of the most well known physicists in the world, and was diagnosed with ALS when he was 21
   Entry id: 1

```


