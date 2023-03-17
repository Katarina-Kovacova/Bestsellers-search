def create_dictionaries(b):
    books_by_year = {}
    books_by_month_year = {}
    books_by_author = {}
    books_by_title = {}

    for book in b:

        date_list_obj = book[3].split("/")

        month = str(date_list_obj[0])
        year = str(date_list_obj[2])

        # convert month to int, prefix a 0 if month is only one digit then add "-" and year.
        # ex month_year: "01-1976"
        month_year = f"{int(month):02}-{year}"

        author = book[1]
        title = book[0]

        if year in books_by_year:
            books_by_year[year].append(book)
        else:
            books_by_year[year] = [book]

        if month_year in books_by_month_year:
            books_by_month_year[month_year].append(book)
        else:
            books_by_month_year[month_year] = [book]

        if author in books_by_author:
            books_by_author[author].append(book)
        else:
            books_by_author[author] = [book]

        if title in books_by_title:
            books_by_title[title].append(book)
        else:
            books_by_title[title] = [book]

    return books_by_year, books_by_month_year, books_by_author, books_by_title


def load_books():
    with open('C:/Users/katek/Desktop/python/booksearch/bestsellers_short.txt', 'r') as file:
        lines_from_file = file.read().split('\n')

        booklist = []
        for line in lines_from_file:
            booklist.append(line.split('\t'))

    # result book[0] => ['1876', 'Gore Vidal', 'Random House', '4/11/1976', 'Fiction']
    # book[0][0] Title
    # book[0][1] Author
    # book[0][2] Publisher
    # book[0][3] Published Date
    # book[0][4] Category

    return booklist


def display_search_option_menu():
    print("""What would you like to do?
    1. Search books by years
    2. Search books by month and year
    3. Search books by author
    4. Search books by title
    5. Exit""")


def search_by_title(books):
    searched_title = input('Enter the title or part of the title: ').lower()
    books_found_by_title = []
    for book in books:
        title = book[0].lower()
        if searched_title in title:
            print(book)
            books_found_by_title.append(book)
    print('Number of books found: ', len(books_found_by_title))


def search_by_title_dict(title_dict):
    searched_title = input('Enter the title or part of the title: ')
    # tmp = {}
    # if searched_title in tmp.values():
    #
    # for title_dict
    if searched_title not in title_dict:
        print("None found.")
    else:
        found_books = title_dict[searched_title]
        print(found_books)
        print('Number of books found: ', len(found_books))


def search_by_author(books):
    searched_author = input('Enter the author name or part of author name: ')
    books_found_by_author = []
    for item in books:
        author = item[1]
        if searched_author.lower() in author:
            print(item)
            books_found_by_author.append(item)
    print('Number of books found: ', len(books_found_by_author))


def search_by_years(books):
    start_year = input('Enter start year: ')
    end_year = input('Enter end year: ')
    books_found_by_year = []
    for item in books:
        # item[3] is date "03/14/1976", grab year with code in next line
        year = item[3].split("/")[2]
        if start_year <= year <= end_year:
            print(item)
            books_found_by_year.append(item)
    print('Number of books found: ', len(books_found_by_year))


def search_by_years_in_dict(books_by_year):
    # This is the search by "field" dictionary function that is currently working.
    # The others are in various states, some might be just a copy of the non-dict version.
    # For testing, I created a shorter version of the input file.
    # The first 50 lines and called it bestsellers_short.txt.
    # With those 50 books there are 6 books published between 2001 (4 books) and 2002 (2 books).
    start_year = int(input('Enter start year: '))
    end_year = int(input('Enter end year: '))
    books_found_by_year = []
    years = list(range(start_year, end_year+1))
    print(years)
    for year in years:
        yr_str = str(year)
        if yr_str in books_by_year:
            books_found_by_year.extend(books_by_year[yr_str])
    print(books_found_by_year)
    print('Number of books found: ', len(books_found_by_year))


def search_by_month_and_year(books):
    user_month = input('Enter month as number 1-12: ')
    user_year = input('Enter year: ')
    books_found_by_month_and_year = []
    for item in books:
        month = item[3][0]
        year = item[3][2]
        if user_month == month and user_year == year:
            print(item)
            books_found_by_month_and_year.append(item)
    print('Number of books found: ', len(books_found_by_month_and_year))


def main():
    booklist = load_books()
    by_year_dict, by_month_year_dict, by_author_dict, by_title_dict = create_dictionaries(booklist)
    # # pprint(by_month_year_dict)
    # quit()

    while True:
        print()
        display_search_option_menu()
        user_selection = int(input('Enter number between 1-5: '))
        print()

        # YEARS
        if user_selection == 1:
            # search_by_years(booklist)
            search_by_years_in_dict(by_year_dict)

        # MONTH-YEAR
        if user_selection == 2:
            search_by_month_and_year(booklist)
            # search_by_month_and_year_dict(booklist)

        # AUTHOR
        if user_selection == 3:
            search_by_author(booklist)
            # search_by_author_dict(booklist)

        # TITLE
        if user_selection == 4:
            search_by_title(booklist)
            # search_by_title_dict(booklist)

        # BYE
        if user_selection == 5:
            break

    print('Thank you for using my first ever programme! Bye :-) ')


if __name__ == '__main__':
    main()
