def load_books():
    with open('bestsellers_list.txt', 'r') as file:
        books = file.read()
        book_list = []
        books = books.split('\n')
        for item in books:
            item_split = item.split('\t')
            book_list.append(item_split)

        for item in book_list:
            item[3] = item[3].split('/')
        return book_list


def search_by_title(book_list):
    searched_title = input('Enter the title or part of the title: ')
    number_of_books_found_by_title = []
    for item in book_list:
        title = item[0]
        if searched_title in title:
            print(item)
            number_of_books_found_by_title.append(item)
    print('Number of books found: ', len(number_of_books_found_by_title))
    print()


def search_by_author(book_list):
    searched_author = input('Enter the author name or part of the author name: ')
    number_of_books_found_by_author = []
    for item in book_list:
        author = item[1]
        if searched_author in author:
            print(item)
            number_of_books_found_by_author.append(item)
    print('Number of books found: ', len(number_of_books_found_by_author))
    print()


def search_by_years(book_list):
    start_year = input('Enter start year: ')
    end_year = input('Enter end year: ')
    number_of_books_found_by_year = []
    for item in book_list:
        year = item[3][2]
        if start_year <= year <= end_year:
            print(item)
            number_of_books_found_by_year.append(item)
    print('Number of books found: ', len(number_of_books_found_by_year))
    print()


def search_by_month_and_year(book_list):
    user_month = input('Enter month as a number (1-12): ')
    user_year = input('Enter year: ')
    number_of_books_found_by_month_and_year = []
    for item in book_list:
        month = item[3][0]
        year = item[3][2]
        if user_month == month and user_year == year:
            print(item)
            number_of_books_found_by_month_and_year.append(item)
    print('Number of books found: ', len(number_of_books_found_by_month_and_year))
    print()


def exit_program():
    print('Thank you for using my program! Bye :-) ')
    quit()


book_list = load_books()
print()

while True:
    menu = '''
    What would you like to do?
    1. Search books by year
    2. Search books by month and year
    3. Search books by author
    4. Search books by title
    5. Exit
    '''

    print(menu)

    user_selection = input('Enter a number between 1-5: ')

    if user_selection == '1':
        search_by_years(book_list)
    elif user_selection == '2':
        search_by_month_and_year(book_list)
    elif user_selection == '3':
        search_by_author(book_list)
    elif user_selection == '4':
        search_by_title(book_list)
    elif user_selection == '5':
        exit_program()
    else:
        print('Invalid option. Please choose a number between 1 and 5.')
