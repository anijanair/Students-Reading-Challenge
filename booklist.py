# make a list
# add a 'HELP' command
# add a 'SHOW' command

book_list = []

print("What is the title of the book that you want to add to the list?")

# add book to the list


def add_book(book):
    book_list.append(book)
    print("Added '{}' to your reading list. You have read {} books so far".format(book, len(book_list)))

# Instruction to the user


def show_help():
    print("""
    Enter 'HELP' for help
    Enter 'SHOW' to see the list
    Enter 'DONE' when done with adding books""")

show_help()

# print the book list


def show_list():
    print("Here is the list of books you've read so far: ")
    for book in book_list:
        print(book)

# ask for item to be added
while True:
    new_book = input("> ")

    # be able to quit
    if new_book.lower() == 'done':
        break
    elif new_book.lower() == 'help':
        show_help()
        continue
    elif new_book.lower() == 'show':
        show_list()
        continue
    else:
        add_book(new_book)