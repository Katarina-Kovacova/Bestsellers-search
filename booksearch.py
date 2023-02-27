def loadBooks():

	with open('C:/Users/Kate/Desktop/Python/bestsellers/bestsellers_list.txt', 'r') as file:
		books = file.read()
		# print(type(books))
		# print(books)
		booklist = []
		books = books.split('\n')
			# print(books)
		for item in books:
			item_split = item.split('\t')
			booklist.append(item_split)
		# print(booklist)

		for item in booklist:
			item[3] = item[3].split('/')
		return booklist

booklist = loadBooks()
print(booklist)
print()	

def Choose_search_option():
	what_do_you_want = ('What would you like to do?')
	option_one = ('1. Search books by years')
	option_two = ('2. Search books by month and year')
	option_three = ('3. Search books by author')
	option_four = ('4. Search books by title')
	option_five = ('5. Exit')
	
	print(what_do_you_want)
	print(option_one)
	print(option_two)
	print(option_three)
	print(option_four)
	print(option_five)

	def searchByTitle():
		searched_title = input('Enter the title or part of the title: ')
		number_of_books_found_by_title = []
		for item in booklist:
			title = item[0]
			if searched_title in title:
				print(item)
				number_of_books_found_by_title.append(item)
		print('Number of books found: ', len(number_of_books_found_by_title))
		print()	
		Choose_search_option()

	def searchByAuthor():
		searched_author = input('Enter the author name or part of author name: ')
		number_of_books_found_by_author = []
		for item in booklist:
			author = item[1]
			if searched_author in author:
				print(item)
				number_of_books_found_by_author.append(item)
		print('Number of books found: ', len(number_of_books_found_by_author))
		print()		
		Choose_search_option()

	def searchByYears():
		start_year = input('Enter start year: ')
		end_year = input('Enter end year: ')
		number_of_books_found_by_year = []
		for item in booklist:
			year = item[3][2]
			if start_year <= year <= end_year:
				print(item)
				number_of_books_found_by_year.append(item)
		print('Number of books found: ', len(number_of_books_found_by_year))
		print()	
		Choose_search_option()

	def searchByMonthAndYear():
		user_month = input('Enter month as number 1-12: ')
		user_year = input ('Enter year: ')
		number_of_books_found_by_month_and_year = []
		for item in booklist:
			month = item[3][0]
			year = item [3][2]
			if user_month == month and user_year == year:
				print(item)
				number_of_books_found_by_month_and_year.append(item)
		print('Number of books found: ', len(number_of_books_found_by_month_and_year))
		print()	
		Choose_search_option()

	def exit():
		print('Thank you for using my first ever programme! Bye :-) ')
		quit()
		
	user_selection = int(input('Enter number between 1-5: '))
	if user_selection == 1:
		searchByYears()

	if user_selection == 2:
		searchByMonthAndYear()

	if user_selection == 3:
		searchByAuthor()

	if user_selection == 4:
		searchByTitle()

	if user_selection == 5:
		exit()
	# return?	

Choose_search_option()

